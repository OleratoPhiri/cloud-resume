# Cloud Resume Challenge

A fully serverless resume website built and deployed on AWS. Live site: [ d3qz0qm8gq8x91.cloudfront.net](https://d3qz0qm8gq8x91.cloudfront.net)

\---

## AWS Services Used

|Service|Purpose|
|-|-|
|**Amazon S3**|Hosts the static HTML/CSS resume files|
|**Amazon CloudFront**|CDN — delivers the site globally over HTTPS|
|**AWS Lambda**|Serverless Python function that reads and updates the visitor count|
|**Amazon DynamoDB**|NoSQL database that stores the visitor count|
|**Amazon API Gateway**|Exposes the Lambda function as a public HTTPS endpoint|
|**AWS IAM**|Manages permissions using the principle of least privilege|
|**Terraform**|Defines the entire infrastructure as code|
|**GitHub Actions**|CI/CD pipeline — auto-deploys the site on every git push|

\---

## How to Deploy

### Prerequisites

* AWS account with CLI configured (`aws configure`)
* Terraform installed
* Git installed

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/OleratoPhiri/cloud-resume.git
cd cloud-resume
```

**2. Deploy infrastructure with Terraform**

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

**3. Upload website files to S3**

```bash
aws s3 sync . s3://olerato-cloud-resume/ \\\\
  --exclude ".git/\\\*" \\\\
  --exclude "terraform/\\\*"
```

**4. Invalidate CloudFront cache**

```bash
aws cloudfront create-invalidation \\\\
  --distribution-id E24IHIG28RVRXW \\\\
  --paths "/\\\*"
```

**5. After first deploy, all future updates are automatic**

Push any change to the `main` branch and GitHub Actions will sync to S3 and invalidate CloudFront automatically.

```bash
git add .
git commit -m "the update"
git push
```

\---

## CI/CD Pipeline

The `.github/workflows/deploy.yml` workflow triggers on every push to `main` and:

1. Configures AWS credentials from GitHub Secrets
2. Syncs updated files to S3
3. Invalidates the CloudFront cache

AWS credentials are stored as GitHub Secrets (`AWS\\\_ACCESS\\\_KEY\\\_ID`, `AWS\\\_SECRET\\\_ACCESS\\\_KEY`) — never hardcoded in the codebase.

\---

## Project Structure

```
cloud-resume/
├── index.html              # Resume webpage
├── style.css               # Styling
├── counter.js              # Visitor counter JavaScript
├── lambda\\\_function.py      # Lambda function (Python)
├── bucket-policy.json      # S3 bucket policy
├── terraform/
│   ├── providers.tf        # AWS provider config
│   ├── variables.tf        # Reusable variables
│   ├── main.tf             # All AWS resources
│   └── outputs.tf          # Output values post-deploy
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions CI/CD pipeline
```

\---

## Part of a 3-Project Cloud Engineering Portfolio

|Project|Focus|
|-|-|
|✅ Cloud Resume Challenge|Serverless, CDN, IaC, CI/CD|
|🔄 Multi-Tier Web Architecture|VPC, EC2, RDS, Auto Scaling|
|🔄 Serverless Data Pipeline|S3 Events, Glue, Athena, CloudWatch|



