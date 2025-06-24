# 🛰️ AWS Serverless Website Visitor Tracker

A lightweight, scalable, and cost-effective **serverless visitor tracking system** built with **AWS Lambda**, **API Gateway**, and **DynamoDB**. Designed to collect visitor logs from your website with zero infrastructure management.

---

<h3 align="left">Watch the video</h3>
<p align="left">
<a href="https://www.youtube.com/watch?v=-m55hW75DdI" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="YouTube" height="30" width="40" /></a>
</p>

## 📌 Features

- Serverless architecture with on-demand scalability
- Logs IP, location, browser agent, and timestamp
- Stores data in DynamoDB with real-time write access
- API Gateway exposes HTTP endpoints to integrate with frontend (JS, etc.)
- Easy-to-deploy with infrastructure-as-code (SAM or Terraform ready)
- Supports real-time monitoring via CloudWatch Metrics

---

## 🧱 Architecture

```text
Frontend (JS/AJAX) 
       │
       ▼
API Gateway ──▶ AWS Lambda ──▶ DynamoDB
                        │
                        ▼
              CloudWatch Logging
```

---

## 🚀 Deployment

### 1. Backend Setup (Lambda + API Gateway + DynamoDB)
Use AWS SAM or Terraform to deploy the stack. Example with SAM:

```bash
sam build
sam deploy --guided
```

### 2. DynamoDB Schema (Example)

- **Table Name:** `VisitorLogs`
- **Partition Key:** `visit_id` (string, UUID)
- Attributes:
  - `timestamp`
  - `ip_address`
  - `user_agent`
  - `page_visited`

### 3. Lambda Function (Python Example)

Parses request data, logs metadata, and stores it in DynamoDB.

### 4. Frontend Integration

Call the endpoint in your website JS:

```js
fetch("https://<your-api-id>.execute-api.<region>.amazonaws.com/prod/track", {
  method: "POST",
  body: JSON.stringify({
    page_visited: window.location.href
  })
})
```

---

## 📊 Monitoring

- CloudWatch Metrics for invocation, latency, error count
- CloudWatch Logs for detailed debugging

---

## 📂 Folder Structure

```
.
├── src/
│   └── handler.py
├── template.yaml  # SAM template
└── README.md
```

---

## 🧑‍💻 Author

Built by [Tariqul Ismail](https://www.tariqulismail.com) — Open for collaboration.

---

## 📃 License

MIT License. Use freely with attribution.
