#!/usr/bin/env bash

set -euxo pipefail

# Deploy the Cloud Function
gcloud functions deploy health-check \
  --runtime=python313 \
  --region=${GCP_REGION} \
  --source=. \
  --entry-point=health_check \
  --trigger-http \
  --service-account=${SERVICE_ACCOUNT_EMAIL} \
  --set-env-vars "PPDB_CONFIG_URI=${PPDB_CONFIG_URI}" \
  --gen2 \
  --quiet
