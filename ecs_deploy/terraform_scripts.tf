provider "aws" {
  region = "us-west-2"
}

resource "aws_ecs_cluster" "llm_cluster" {
  name = "llmops-cluster"
}

resource "aws_ecs_task_definition" "llmops_task" {
  family                   = "llmops-semantic-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]

  container_definitions = jsonencode([{
    name      = "semantic-search"
    image     = "your-ecr-repo/semantic-search:latest"
    cpu       = 256
    memory    = 512
    essential = true
    portMappings = [{
      containerPort = 8080
      protocol      = "tcp"
    }]
  }])
}

resource "aws_lambda_function" "api_handler" {
  filename         = "lambda.zip"
  function_name    = "semantic-api-lambda"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "app.lambda_handler"
  runtime          = "python3.10"
  source_code_hash = filebase64sha256("lambda.zip")
}

resource "aws_apigatewayv2_api" "api" {
  name          = "semantic-search-api"
  protocol_type = "HTTP"
}
