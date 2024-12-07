# Output VPC ID
output "vpc_id" {
  value = aws_vpc.portfolio_vpc.id
}

# Output Public Subnet ID
output "public_subnet_id" {
  value = aws_subnet.public_subnet.id
}

# Output Security Group ID
output "security_group_id" {
  value = aws_security_group.portfolio_sg.id
}

# Output EC2 Public IP
output "ec2_public_ip" {
  value = aws_instance.portfolio_ec2.public_ip
}