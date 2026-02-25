#!/usr/bin/env bash

set -euxo pipefail

# Delete Cloud Function
gcloud functions delete health-check \
  --region="${GCP_REGION}" \
  --project="${GCP_PROJECT}" \
  --quiet || true
