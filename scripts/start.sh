#!/bin/bash
export PYTHONPATH=src

uvicorn prod_server.main:app \
  --host 0.0.0.0 \
  --port ${PORT:-10000}