---
last_accessed: 2026-08-16
access_count: 1
created: 2026-08-16
---

# AWS Cloud Cost Reduction - Auto Toolchain H2/2026

Context: 20% cost reduction directive from Eitan's plan for H2/2026 across 3 ToolChain AWS accounts.

## Key Facts

- **Total July 2026 spend**: $19,855/month (UnblendedCost, matching $20k estimate)
- **20% reduction target**: $3,971/month reduction to reach $15,884
- **Primary cost driver**: EBS snapshots in ateam account ($9,156/month = 46% of total)
- **Secondary cost driver**: S3 storage in ateam ($3,921/month), specifically auto-product-build-downstream at 266 TB
- **Stage account surprise**: ROSA/OCP cluster is 79% of stage costs; provisioned IOPS at $968/month
- **v1 report used BlendedCost (wrong)**: overstated all figures by ~25%. Corrected to UnblendedCost on Aug 17.

## Account Summary

| Account | ID | July 2026 | Main Costs |
|---|---|---|---|
| it-cloud-aws-ateam | 587138297281 | $14,245 | EBS snapshots ($9.2k), S3 ($3.9k), EC2 ($706) |
| it-cloud-aws-internal-ateam | 339712814647 | $3,009 | EC2 runners ($2.2k), Route53 ($150), CloudFront ($122) |
| it-cloud-aws-ateam-stage | 203972369401 | $2,601 | ROSA cluster ($2,050), provisioned IOPS ($968) |

## Eitan's Plan Status (as of Aug 16)

5/10 items done. Key pending: Pipe-x off-peak (#6), RHAS-CI cleanup (#7), S3 retention review (#10).
Snapshot cleanup (#4, done early Aug) expected to deliver $6-10k/month savings - verify August bill.

## New Findings (Not in Eitan's Plan)

1. auto-product-build-downstream: 266 TB, ~$6.1k/month - versioning + no lifecycle = unbounded growth
2. hstefans-test-bucket: 1.2 TB (ateam) + 3 test buckets (stage) - Hubert transitioning
3. Stage ROSA provisioned IOPS: $968/month - GP3 may suffice
4. 5 stopped instances in stage us-west-2 (autosd-ana-*, asa-dev-*) - likely orphaned
5. Unnamed t4g.2xlarge (ateam) running 10+ months
6. yuki-centos9-x86-flight-control (stage Tokyo) - $59/month test instance
7. 15 velero backup buckets (ateam), 12 personal test buckets (stage)

## Deliverables

- HTML report: `user/aws-cost-analysis.html`
- Google Doc: https://docs.google.com/document/d/1h8QDtI_lIvskytBZ4uEoP5ZT6BbfMfGakDTjHKEeCRY/edit
- Eitan's plan (reference): https://docs.google.com/document/d/1Dtjh49Ou_mlFLUEF5hAgfNC-TTmN4qW31LyKePWQNTo/edit

## Potential Savings

Total potential: $5,528 - $10,257/month (if all items execute). 20% target ($3,971) likely achievable through snapshot cleanup alone.
