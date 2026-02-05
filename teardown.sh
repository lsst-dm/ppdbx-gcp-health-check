#!/usr/bin/env bash

set -euxo pipefail

# Delete Cloud Function
gcloud run services delete health-check \
  --region="${GCP_REGION}" \
  --project="${GCP_PROJECT}" \
  --quiet
