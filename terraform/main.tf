# Configure the AWS Provider
provider "aws" {
  region = var.aws_region
}

# Define the VPC
resource "aws_vpc" "portfolio_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = var.vpc_name
  }
}

# Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.portfolio_vpc.id

  tags = {
    Name = var.igw_name
  }
}

# Public Subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.portfolio_vpc.id
  cidr_block              = var.public_subnet_cidr
  map_public_ip_on_launch = true
  availability_zone       = var.availability_zone

  tags = {
    Name = var.public_subnet_name
  }
}

# Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.portfolio_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = var.public_rt_name
  }
}

# Route Table Association
resource "aws_route_table_association" "public_rt_assoc" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

# Security Group
resource "aws_security_group" "portfolio_sg" {
  vpc_id = aws_vpc.portfolio_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidr_blocks
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidr_blocks
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidr_blocks
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = var.sg_name
  }
}

# EC2 Instance
resource "aws_instance" "portfolio_ec2" {
  ami                         = var.ec2_ami
  instance_type               = var.ec2_instance_type
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.portfolio_sg.id]
  associate_public_ip_address = true

  key_name = "Portfolio_Key"

  tags = {
    Name = var.ec2_name
  }

  # Install Docker, create .env, and run the application
  user_data = <<-EOF
              #!/bin/bash
              # Update system and install Docker
              sudo yum update -y
              sudo amazon-linux-extras enable docker
              sudo yum install -y docker git
              sudo systemctl start docker
              sudo systemctl enable docker

              # Clone the repository
              git clone https://github.com/ifyvinz/portfolio.git /home/ec2-user/app
              cd /home/ec2-user/app

              # Create the .env file
              cat <<EOT >> .env
              # PostgreSQL database configuration
              POSTGRES_DB=portfolio_db
              POSTGRES_USER=portfolio_user
              POSTGRES_PASSWORD=showtime22
              POSTGRES_PORT=5432
              POSTGRES_HOST=db

              # Email server credentials
              EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
              EMAIL_HOST=smtp.gmail.com
              EMAIL_PORT=587
              EMAIL_USE_TLS=True
              EMAIL_HOST_USER=ifyvinz@gmail.com
              EMAIL_HOST_PASSWORD=dgbt lpll ivyk viwz
              DEFAULT_FROM_EMAIL=\$EMAIL_HOST_USER

              # Django Create Super User
              DJANGO_SUPERUSER_EMAIL=ifyvinz@gmail.com
              DJANGO_SUPERUSER_USERNAME=ifyvinz
              DJANGO_SUPERUSER_PASSWORD=showtime22

              SECRET_KEY=django-insecure-ray=q=pn3re_h547_lkla&8%m3eenx5r=4=ec&=&yj=n^-*)l7
              DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 www.ifyvinz.com ifyvinz.com localhost 127.0.0.1 app 0.0.0.0 [::1]
              EOT

              # Start the application using Docker Compose
              docker-compose up -d
              EOF
}



# TLS RSA Algorithm (still generating local private key, but no AWS key pair resource)
resource "tls_private_key" "generated" {
  algorithm = "RSA"
}

# Save the private key locally
resource "local_file" "private_key_pem" {
  content  = tls_private_key.generated.private_key_pem
  filename = "MyAWSKey.pem"
}

resource "aws_key_pair" "generated" {
  key_name   = "MyAWSKey"
  public_key = tls_private_key.generated.public_key_openssh

  lifecycle {
    ignore_changes = [key_name]
  }
}
