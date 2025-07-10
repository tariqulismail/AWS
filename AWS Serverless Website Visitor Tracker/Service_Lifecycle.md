# Visitor Tracking System – ITIL-Based Service Documentation

## 1. Service Strategy

- **Service Name**: Visitor Tracking System
- **Objective**: Monitor and store real-time visitor data for analytics, security, and operations.
- **Stakeholders**: Web team, marketing, product owners
- **Business Value**: Enables behavioral analytics, helps optimize site performance, supports compliance.

---

## 2. Service Design

- **Architecture Overview**:
  - AWS Lambda (event processing)
  - API Gateway (HTTP trigger)
  - DynamoDB (data store)
  - CloudWatch Logs (monitoring)

- **Availability Goal**: 99.9%
- **Security**:
  - IAM roles with least privilege
  - API Gateway with throttling
- **Backup**: DynamoDB point-in-time recovery enabled

---

## 3. Service Transition

- **Deployment Process**:
  - Code versioned in GitHub
  - IaC via Terraform (infra folder)
  - GitHub Actions for CI/CD

- **Change Management**:
  - All code changes via pull requests
  - Changes reviewed and approved before merging
  - Deployment log in each release

---

## 4. Service Operation

- **Monitoring**:
  - CloudWatch metrics: `Invocations`, `Errors`, `Duration`
  - Alarm on Lambda error count > 3 in 5 min

- **Logging**:
  - Lambda logs streamed to CloudWatch
  - Enable AWS X-Ray for tracing

- **Incident Handling**:
  - Errors go to DLQ (if configured)
  - Slack/email alerts via SNS (future scope)

---

## 5. Continual Service Improvement

- **Monthly Review Metrics**:
  - Request volume trends
  - Error rate trends
  - Latency spikes

- **Improvement Pipeline**:
  - Add geo-location enrichment
  - Integrate with QuickSight for dashboarding

---

## Appendix

- Terraform Infra: `infra/` folder
- Lambda Code: `src/` folder
- CI/CD Workflow: `.github/workflows/deploy.yml`
