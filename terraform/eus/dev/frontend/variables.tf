variable "owner" {
  description = "Name of the owner of the workload and resources"
  type        = string
  default     = "OPRE"
}

variable "project" {
  description = "Project name that resources fall under"
  type        = string
  default     = "ops"
}

variable "environment" {
  description = "Environment tag for the resources"
  type        = string
  default     = "dev"
}

variable "location" {
  description = "Azure location for the resources"
  type        = string
  default     = "eastus"
}

### Container Details

variable "container_name" {
  description = "Name of the container"
  type        = string
  default     = "ops-frontend"
}

variable "container_image" {
  description = "Container image"
  type        = string
  default     = "ghcr.io/hhs/opre-ops/ops-frontend"
}

variable "container_tag" {
  description = "Container image tag"
  type        = string
  default     = "1a727b26bca88e34607355fd74e65d45165738de"
}

variable "cpu" {
  description = "CPU requirements. This has specific ration with memory... (beta)"
  type        = number
  default     = 0.25
}

variable "memory" {
  description = "Memory requirements. This has specific ration with cpu... (beta)"
  type        = string
  default     = "0.5Gi"
}

variable "port" {
  description = "Port for application"
  type        = number
  default     = 3000
}