#!/usr/bin/env bash

set -euxo pipefail

gcloud functions call health-check --region=${GCP_REGION}
