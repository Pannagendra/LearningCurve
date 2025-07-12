#create s3 bucket using aws
resource "aws_s3_bucket" "ml_models" {
  bucket = "citiustech-ml-models"
  versioning {
    enabled = true
  }
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
  tags = {
    Environment = "prod"
    Team        = "mlops"
  }
}
