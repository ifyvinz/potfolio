# Variables
variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "vpc_name" {
  type    = string
  default = "Portfolio-VPC"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "igw_name" {
  type    = string
  default = "Portfolio-IGW"
}

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

variable "public_rt_name" {
  type    = string
  default = "Portfolio-Public-Route-Table"
}

variable "sg_name" {
  type    = string
  default = "Portfolio-SG"
}

variable "allowed_cidr_blocks" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}

variable "ec2_name" {
  type    = string
  default = "Portfolio-EC2"
}

variable "ec2_ami" {
  type    = string
  default = "ami-0b5673b5f6e8f7fa7"
}

variable "ec2_instance_type" {
  type    = string
  default = "t2.micro"
}