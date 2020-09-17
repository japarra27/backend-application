# Create a terraform file to deploy IaC inside AWS.
provider "aws" {
  region = var.region_aws
}

# configure the security group
resource "aws_security_group" "sg_project0" {
  
  ingress {
    description = "Open TCP port 22"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Open TCP port 443"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Port to connect to project0 app"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
   from_port = 0
   to_port = 0
   protocol = "-1"
   cidr_blocks = ["0.0.0.0/0"]
 }

  egress {
   from_port = 0
   to_port = 0
   protocol = "-1"
   cidr_blocks = ["0.0.0.0/0"]
 }
}

# Configure the ec2 instance
resource "aws_instance" "dsc_project0" {
  ami           = "ami-06b263d6ceff0b3dd"
  instance_type = "t2.micro"
  key_name      = "dsc_projects"

  tags = {
    Name = "dsc-project0"
  }

  vpc_security_group_ids = [aws_security_group.sg_project0.id]
}
