#Terraform code to create a GKE cluster with autoscaling enabled.

provider "google" {
  project = "my-mlops-project"
  region  = "us-central1"
}

resource "google_container_cluster" "primary" {
  name               = "mlops-gke"
  location           = "us-central1"
  remove_default_node_pool = true
  initial_node_count = 1

  autoscaling {
    enable_node_autoprovisioning = true
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "primary-node-pool"
  cluster    = google_container_cluster.primary.name
  location   = "us-central1"

  node_config {
    machine_type = "e2-standard-4"
  }

  autoscaling {
    min_node_count = 1
    max_node_count = 5
  }

  initial_node_count = 1
}
