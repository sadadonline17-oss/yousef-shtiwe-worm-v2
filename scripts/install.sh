#!/bin/bash
echo "👹 [SHADOW-INSTALLER] Starting Supreme Installation..."
export PIP_DISABLE_PIP_VERSION_CHECK=1
pip install -r requirements.txt
echo "✅ [SHADOW-INSTALLER] Dependencies verified."
echo "🔗 [SHADOW-INSTALLER] Linking 'shadow' command..."
chmod +x shadow
echo "👹 SHADOW V15.5 'THE OVERLORD' IS LIVE."
