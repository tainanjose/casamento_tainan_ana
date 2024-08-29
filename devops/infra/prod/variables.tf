
# GERAL
variable "environment" {
  type    = string
  default = "prod"
}

variable "region" {
  type = string
  default = "sa-east-1"
}

variable "availability_zone" {
  type = string
  default = "sa-east-1a"
}

# EC2
variable "instance_type" {
  type = string
  default = "t2.micro"
}

variable "ami" {
  type = string
  default = "ami-04716897be83e3f04"
}

variable "volume_size" {
  type = string
  default = "20"
}

variable "key_name" {
  type = string
  default = "tainan_dev"
}

variable "backend_port" {
  type = number
  default = 8000
}

# DATABASE
variable "engine_version" {
  type = string
  default = "15"
}

variable "instance_class" {
  type = string
  default = "db.t3.micro"
}

variable "database_name" {
  type = string
  default = "djangodb"
}

variable "database_username" {
  type = string
  default = "djangodbuser"
}

variable "database_password" {
  type = string
  default = "---> ver na pasta ansible/group_vars"
}

variable "storage" {
  type = number
  default = 20
}
