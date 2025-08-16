#!/bin/bash

uv init
uv sync
source .venv/bin/activate
uvicorn main:app --port 8000
