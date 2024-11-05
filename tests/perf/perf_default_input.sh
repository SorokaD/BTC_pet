#!/bin/sh

set -e

SCRIPT_DIR=$(dirname "$0")

wrk -t 1 -c 10 -d 10s -s "$SCRIPT_DIR/default_input_payload.lua" http://135.148.34.150:8000/predict_default_input