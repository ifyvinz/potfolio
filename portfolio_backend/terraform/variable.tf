# AWS Region
variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

# VPC Configuration
variable "vpc_name" {
  type    = string
  default = "Portfolio-VPC"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

# Internet Gateway
variable "igw_name" {
  type    = string
  default = "Portfolio-IGW"
}

# Subnet Configuration
variable "public_subnet_name" {
  type    = string
  default = "Portfolio-Public-Subnet"
}

variable "public_subnet_cidr" {
  type    = string
  default = "10.0.1.0/24"
}

variable "availability_zone" {
  type    = string
  default = "eu-central-1a"
}

# Route Table
variable "public_rt_name" {
  type    = string
  default = "Portfolio-Public-Route-Table"
}

# Security Group
variable "sg_name" {
  type    = string
  default = "Portfolio-SG"
}

variable "allowed_cidr_blocks" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}

# EC2 Instance
variable "ec2_name" {
  type    = string
  default = "Portfolio-EC2"
}

variable "ec2_ami" {
  type    = string
  default = "ami-0453ec754f44f9a4a" 
}

variable "ec2_instance_type" {
  type    = string
  default = "t2.micro"
}
