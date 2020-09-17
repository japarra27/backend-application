# Configure the variables to use in the project

# aws
variable "region_aws" {
  description = "Name of the aws region"
  type        = string
  default     = "us-east-1"
}

# gcp
variable "credentials_file" {
  description = "Name of the credentials file"
  type        = string
  default     = ".terraform/gcpdatascientist-keys.json"
}

variable "project_gcp" {
  description = "Name of the GCP project"
  type        = string
  default     = "gcpdatascientist"
}

variable "region_gcp" {
  description = "Name of the GCP region"
  type        = string
  default     = "us-east1"
}

variable "zone_gcp" {
  description = "Name of the GCP zone"
  type        = string
  default     = "us-east1-b"
}