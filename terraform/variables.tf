variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "S3 bucket name for the resume website"
  type        = string
  default     = "olerato-cloud-resume"
}

variable "lambda_function_name" {
  description = "Name of the visitor counter Lambda function"
  type        = string
  default     = "visitor-counter"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB visitor counter table"
  type        = string
  default     = "visitor-counter"
}