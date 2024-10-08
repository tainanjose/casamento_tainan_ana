
#resource "aws_db_security_group" "default" {
#  name = "django_db_rds_sg"
#  ingress {
#    cidr = "10.0.0.0/24"
#  }
#}

#resource "aws_db_instance" "django_db" {
#  allocated_storage     = 50
#  max_allocated_storage = 100
#}

resource "aws_security_group" "default" {
  name        = "django-prod-rds-sg"
  description = "Allow all inbound traffic"
  # vpc_id      = var.vpc_id

  ingress {
    description = "Allow connections"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    # mydb-dev-sg # tem que mudar o security group :(
    # security_groups = ["sg-07b109cdf8982e64f"]
  }

  tags = {
    Name = "django-db-sg-prod"
    Environment = "${var.environment}"
  }

}

resource "aws_db_instance" "default" {
  depends_on              = [aws_security_group.default]
  identifier              = var.database_name
  storage_type            = "gp2"
  allocated_storage       = var.storage
  engine                  = "postgres"
  engine_version          = var.engine_version
  port                    = "5432"
  instance_class          = var.instance_class
  db_name                    = var.database_name
  username                = var.database_username
  password                = var.database_password
  publicly_accessible     = "false"
  # security_groups         = ["${aws_security_group.django-prod-rds-sg.name}"]
  # vpc_security_group_ids = ["${aws_security_group.default.id}"]
  # parameter_group_name = "default.mysql5.7"
  skip_final_snapshot     = "true"
  availability_zone       = var.availability_zone

  tags = {
    Name = "django-db-prod"
    Environment = "${var.environment}"
  }
}
