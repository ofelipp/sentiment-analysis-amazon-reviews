#!/bin/bash

export MLFLOW_S3_ENDPOINT_URL=http://minio:9000
export AWS_ACCESS_KEY_ID=user
export AWS_SECRET_ACCESS_KEY=password

mlflow server \
  --backend-store-uri postgresql://user:password@postgres:5432/mlflowdb \
  --artifacts-destination s3://mlflow-artifacts \
  --host 0.0.0.0 \
  --port 5000