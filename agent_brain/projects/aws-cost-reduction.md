---
last_accessed: 2026-08-16
access_count: 1
created: 2026-08-16
---

# AWS Cloud Cost Reduction - Auto Toolchain H2/2026

Context: 20% cost reduction directive from Eitan's plan for H2/2026 across 3 ToolChain AWS accounts.

## Key Facts

- **Total July 2026 spend**: $26,347/month (32% over the $20k estimate)
- **20% reduction target**: $5,270/month reduction to reach $21,078
- **Primary cost driver**: EBS snapshots in ateam account ($12,048/month = 46% of total)
- **Secondary cost driver**: S3 storage in ateam ($6,198/month), specifically auto-product-build-downstream at 266 TB
- **Stage account surprise**: ROSA/OCP cluster is 79% of stage costs; provisioned IOPS at $968/month

## Account Summary

| Account | ID | July 2026 | Main Costs |
|---|---|---|---|
| it-cloud-aws-ateam | 587138297281 | $19,790 | EBS snapshots ($12k), S3 ($6.2k), EC2 ($941) |
| it-cloud-aws-internal-ateam | 339712814647 | $3,956 | EC2 runners ($2.9k), CloudFront ($192) |
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

Total potential: $8,228 - $14,757/month (if all items execute). 20% target ($5,270) likely achievable through snapshot cleanup alone.
