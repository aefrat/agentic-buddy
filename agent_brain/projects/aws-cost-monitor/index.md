---
last_accessed: 2026-08-17
access_count: 1
created: 2026-08-17
---

# AWS Cost Monitor - Agent Setup

Agent capability for monitoring ATC Toolchain AWS costs using the AWS Agent Toolkit MCP server and skills.

## Setup Status

- **AWS MCP Server**: Configured in `~/.claude.json` as `aws-mcp` (uvx mcp-proxy-for-aws, endpoint: us-east-1)
- **AWS Agent Toolkit**: Installed via `aws configure agent-toolkit --yes --region us-east-1`
- **Skills installed**: 22 total (18 default + 4 cost-specific additions)

## Installed Skills (Cost-Relevant)

| Skill | Purpose | Location |
|-------|---------|----------|
| aws-billing-and-cost-management | Cost Explorer, budgets, Savings Plans, right-sizing, CUR/Athena | `~/.agents/skills/aws-billing-and-cost-management/` |
| aws-observability | CloudWatch metrics, alarms, dashboards | `~/.agents/skills/aws-observability/` |
| querying-aws-cloudwatch | SQL queries on CloudWatch Logs (VPC Flow, WAF, CloudFront, S3 access) | `~/.agents/skills/querying-aws-cloudwatch/` |
| querying-aws-s3 | S3 metadata queries, storage lens, bucket activity audit | `~/.agents/skills/querying-aws-s3/` |
| securing-s3-buckets | S3 security audit and best practices | `~/.agents/skills/securing-s3-buckets/` |
| setting-up-cloudwatch-alarm-notifications | Budget alerts via SNS + CloudWatch | `~/.agents/skills/setting-up-cloudwatch-alarm-notifications/` |
| aws-compute | EC2 instance management, right-sizing | `~/.agents/skills/aws-compute/` |
| aws-security | IAM, security audits | `~/.agents/skills/aws-security/` |

## Accounts Monitored

| Account | ID | Alias | Primary Costs (Jul 2026) |
|---------|-----|-------|--------------------------|
| it-cloud-aws-ateam | 587138297281 | ateam | $14,245 (EBS snapshots, S3, EC2) |
| it-cloud-aws-internal-ateam | 339712814647 | internal-ateam | $3,009 (EC2 runners, Route53, CloudFront) |
| it-cloud-aws-ateam-stage | 203972369401 | stage | $2,601 (ROSA cluster, provisioned IOPS) |

**Total**: ~$19,855/month (Jul 2026, UnblendedCost)

## How to Use

### Quick cost check
```bash
# Authenticate first
aws login --region eu-west-1

# Current month costs by service
aws ce get-cost-and-usage \
  --time-period Start=$(date +%Y-%m-01),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics UnblendedCost \
  --group-by Type=DIMENSION,Key=SERVICE
```

### Cross-account comparison
Switch accounts by clearing the login session:
```bash
sed -i '/login_session/d' ~/.aws/config
aws login --region eu-west-1
```

### MCP server access
The aws-mcp server provides sandboxed access to 300+ AWS services with CloudTrail audit logging. It's configured globally in `~/.claude.json` and available to all Claude Code sessions.

## Key Metrics to Track

1. **Monthly total** (target: $15,884 = $19,855 - 20%)
2. **EBS snapshot spend** (was $9,156/month - cleanup should reduce)
3. **S3 storage growth** (auto-product-build-downstream at 266 TB)
4. **ROSA cluster cost** (stage account, $2,050/month)
5. **Provisioned IOPS** (stage, $968/month - GP3 migration candidate)

## Related

- [AWS Cost Reduction Project](../aws-cost-reduction.md) - Analysis, findings, recommendations
- [AWS Cost Analysis HTML](../../user/aws-cost-analysis.html) - Full report
- [Google Doc](https://docs.google.com/document/d/1h8QDtI_lIvskytBZ4uEoP5ZT6BbfMfGakDTjHKEeCRY/edit) - Shared version
