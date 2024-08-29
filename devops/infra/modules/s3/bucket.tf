# --> BUCKET USER to access the bucket and Policy (with write permissions)
resource "aws_iam_user" "bucket_user" {
  name = "django_s3bucketuser_${var.environment}"

  tags = {
    Name = "django-storage"
    Environment = "${var.environment}"
  }
}

resource "aws_iam_policy" "policy" {
  name = "django-${var.environment}-s3-access-policy"
  description = "django ${var.environment} policy"
  policy = templatefile("policy_bucket_s3_permissions.json", {BUCKET_NAME=var.django_aws_s3_bucket})
}

resource "aws_iam_user_policy_attachment" "policy-attach" {
  user       = aws_iam_user.bucket_user.name
  policy_arn = aws_iam_policy.policy.arn
}

resource "aws_iam_access_key" "user_access_key" {
  user = aws_iam_user.bucket_user.name
}


# --> BUCKET 2 for media (private)
resource "aws_s3_bucket" "django_s3_bucket_media" {
  bucket = var.django_aws_s3_bucket

  tags = {
    Name = "django-storage"
    Environment = "${var.environment}"
  }
}

resource "aws_s3_bucket_public_access_block" "django_s3_bucket_media" {
  bucket = aws_s3_bucket.django_s3_bucket_media.id

  block_public_acls   = true
  block_public_policy = true
}

resource "aws_s3_bucket_cors_configuration" "django_s3_bucket_media" {
  bucket = aws_s3_bucket.django_s3_bucket_media.id

  cors_rule {
    allowed_origins = ["https://${var.django_dns_url}", "http://${var.django_dns_url}"]
    allowed_methods = ["PUT", "POST", "DELETE", "GET"]
    expose_headers  = ["ETag", "Accept-Ranges", "Content-Encoding", "Content-Length", "Content-Range"]
    allowed_headers = ["*"]
    max_age_seconds = 86400
  }
}
