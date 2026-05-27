output "cloudfront_url" {
  description = "Your resume website URL"
  value       = "https://${aws_cloudfront_distribution.resume.domain_name}"
}

output "api_gateway_url" {
  description = "Visitor counter API URL"
  value       = "${aws_apigatewayv2_stage.visitor_counter.invoke_url}/count"
}

output "s3_bucket_name" {
  description = "S3 bucket name"
  value       = aws_s3_bucket.resume.bucket
}