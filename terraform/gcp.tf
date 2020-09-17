# define the provider info
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_file)
  project = var.project_gcp
  region  = var.region_gcp
  zone    = var.zone_gcp
}

# create the compute engine instance
resource "google_compute_instance" "default" {
  name         = "project0"
  machine_type = "f1-micro"
  zone         = var.zone_gcp

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-bionic-v20200908"
    }
  }

  metadata_startup_script = "sudo apt-get update && sudo apt-get install virtualenv && sudo apt -y install python3-pip"

  network_interface {
    network = "default"

    access_config {
      // Include this section to give the VM an external ip address
    }
  }

  // Apply the firewall rule to allow external IPs to access this instance
  tags = ["http-server", "https-server"]
}

# allow traffic
resource "google_compute_firewall" "http-server" {
  name    = "default-allow-http"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "8000", "8080", "22", "443"]
  }

  // Allow traffic from everywhere to instances with an http-server tag
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-server"]
}

# allow traffic
resource "google_compute_firewall" "https-server" {
  name    = "default-allow-https"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "8000", "8080", "22", "443"]
  }

  // Allow traffic from everywhere to instances with an http-server tag
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["https-server"]
}

output "ip" {
  value = "${google_compute_instance.default.network_interface.0.access_config.0.nat_ip}"
}