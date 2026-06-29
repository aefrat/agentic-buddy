#!/usr/bin/env python3
"""
Compute deterministic statistics from the AI methodology running tallies.

Reads the pipe-delimited ledger (running-tallies.md), filters by date
range, and produces a JSON file with counts, percentages, and trend
deltas. Standard library only - no LLM calls.

Usage:
    python3 compute_stats.py \
        --tallies path/to/running-tallies.md \
        --output path/to/period-stats.json \
        --period weekly|monthly \
        [--previous path/to/previous-stats.json]
"""

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timedelta


CATEGORIES = ["autonomous", "assisted", "enhanced", "human-only"]


def parse_tallies(filepath):
    """Parse the pipe-delimited tallies file into a list of dicts."""
    entries = []
    in_code_block = False
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            if not line or line.startswith("#") or line.startswith("-"):
                continue
            parts = line.split("|")
            if len(parts) < 5:
                continue
            try:
                date = datetime.strptime(parts[0].strip(), "%Y-%m-%d").date()
            except ValueError:
                continue
            entries.append({
                "date": date,
                "category": parts[1].strip().lower(),
                "domain": parts[2].strip().lower(),
                "label": parts[3].strip(),
                "confidence": parts[4].strip().lower(),
            })
    return entries


def filter_by_period(entries, period):
    """Filter entries to the specified period ending today."""
    today = datetime.now().date()
    if period == "weekly":
        cutoff = today - timedelta(days=7)
    elif period == "monthly":
        cutoff = today - timedelta(days=30)
    else:
        cutoff = today - timedelta(days=7)

    current = [e for e in entries if e["date"] > cutoff]

    if period == "weekly":
        prev_cutoff = cutoff - timedelta(days=7)
    else:
        prev_cutoff = cutoff - timedelta(days=30)

    previous = [e for e in entries if prev_cutoff < e["date"] <= cutoff]

    return current, previous


def compute_distribution(entries):
    """Compute category distribution with counts and percentages."""
    total = len(entries)
    counts = Counter(e["category"] for e in entries)

    distribution = {}
    for cat in CATEGORIES:
        count = counts.get(cat, 0)
        pct = round(count / total * 100, 1) if total > 0 else 0.0
        distribution[cat] = {"count": count, "percentage": pct}

    distribution["total"] = total
    return distribution


def compute_domain_breakdown(entries):
    """Compute per-domain counts and category breakdown."""
    domains = {}
    for e in entries:
        domain = e["domain"]
        if domain not in domains:
            domains[domain] = {"total": 0, "categories": Counter()}
        domains[domain]["total"] += 1
        domains[domain]["categories"][e["category"]] += 1

    result = {}
    for domain, data in sorted(domains.items(), key=lambda x: -x[1]["total"]):
        result[domain] = {
            "total": data["total"],
            "categories": dict(data["categories"]),
        }
    return result


def compute_trends(current_dist, previous_dist):
    """Compute trend deltas between current and previous period."""
    trends = {}
    for cat in CATEGORIES:
        curr_pct = current_dist.get(cat, {}).get("percentage", 0.0)
        prev_pct = previous_dist.get(cat, {}).get("percentage", 0.0)
        delta = round(curr_pct - prev_pct, 1)
        trends[cat] = {
            "current_pct": curr_pct,
            "previous_pct": prev_pct,
            "delta": delta,
            "direction": "up" if delta > 0 else "down" if delta < 0 else "flat",
        }
    return trends


def compute_confidence_breakdown(entries):
    """Compute classification confidence distribution."""
    counts = Counter(e["confidence"] for e in entries)
    total = len(entries)
    return {
        level: {
            "count": count,
            "percentage": round(count / total * 100, 1) if total > 0 else 0.0,
        }
        for level, count in counts.items()
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compute AI methodology statistics"
    )
    parser.add_argument(
        "--tallies", required=True, help="Path to running-tallies.md"
    )
    parser.add_argument(
        "--output", required=True, help="Path to output JSON file"
    )
    parser.add_argument(
        "--period",
        choices=["weekly", "monthly"],
        default="weekly",
        help="Analysis period (default: weekly)",
    )
    parser.add_argument(
        "--previous",
        help="Path to previous period stats for trend comparison",
    )
    args = parser.parse_args()

    entries = parse_tallies(args.tallies)

    if not entries:
        stats = {
            "period": args.period,
            "generated": datetime.now().isoformat(),
            "total_tasks": 0,
            "distribution": {cat: {"count": 0, "percentage": 0.0} for cat in CATEGORIES},
            "domains": {},
            "trends": {},
            "confidence": {},
            "note": "No tallies data available yet",
        }
        with open(args.output, "w") as f:
            json.dump(stats, f, indent=2)
        print(f"No data found. Empty stats written to {args.output}")
        return

    current, previous = filter_by_period(entries, args.period)

    if not current:
        print(f"No entries found for the current {args.period} period.")
        stats = {
            "period": args.period,
            "generated": datetime.now().isoformat(),
            "total_tasks": 0,
            "distribution": {cat: {"count": 0, "percentage": 0.0} for cat in CATEGORIES},
            "domains": {},
            "trends": {},
            "confidence": {},
            "note": f"No entries in current {args.period} period",
        }
        with open(args.output, "w") as f:
            json.dump(stats, f, indent=2)
        return

    current_dist = compute_distribution(current)
    domains = compute_domain_breakdown(current)
    confidence = compute_confidence_breakdown(current)

    trends = {}
    if previous:
        previous_dist = compute_distribution(previous)
        trends = compute_trends(current_dist, previous_dist)

    if args.previous:
        try:
            with open(args.previous, "r") as f:
                prev_stats = json.load(f)
            if not trends and "distribution" in prev_stats:
                trends = compute_trends(current_dist, prev_stats["distribution"])
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    date_range = {
        "start": min(e["date"] for e in current).isoformat(),
        "end": max(e["date"] for e in current).isoformat(),
    }

    stats = {
        "period": args.period,
        "generated": datetime.now().isoformat(),
        "date_range": date_range,
        "total_tasks": current_dist["total"],
        "distribution": {
            k: v for k, v in current_dist.items() if k != "total"
        },
        "domains": domains,
        "trends": trends,
        "confidence": confidence,
    }

    with open(args.output, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Stats for {args.period} period written to {args.output}")
    print(f"  Tasks: {current_dist['total']}")
    for cat in CATEGORIES:
        c = current_dist.get(cat, {})
        print(f"  {cat}: {c.get('count', 0)} ({c.get('percentage', 0)}%)")


if __name__ == "__main__":
    main()
