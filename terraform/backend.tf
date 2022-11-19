terraform {
  backend "s3" {
    key    = "bot/"
    region = "eu-central-1"

  }
}
