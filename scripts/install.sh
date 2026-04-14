#!/bin/bash
set -e
echo "👹 [SHADOW-INSTALLER] Initializing Void Protocol..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ [SHADOW-INSTALLER] Shadow successfully initialized."
