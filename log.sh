#!/bin/bash

set -euxo pipefail

# Default number of log lines to show
LIMIT=${1:-20}

gcloud functions logs read health-check --region=${GCP_REGION} --limit=${LIMIT}
