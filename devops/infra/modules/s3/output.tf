output "access_key_id" {
  description = "The value to be stored into your app to access the new bucket"
  value = aws_iam_access_key.user_access_key.id
}

output "secret_access_key" {
  description = "The value to be stored into your app to access the new bucket"
  value = aws_iam_access_key.user_access_key.secret
  sensitive = true
}

output "bucket_2" {
    description = "Bucket private for django media files"
    value = aws_s3_bucket.django_s3_bucket_media.id
}
