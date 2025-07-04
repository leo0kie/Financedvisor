#!/bin/bash

mkdir -p /app/.streamlit

echo "OPENAI_API_KEY = \"$OPENAI_API_KEY\"" >> /app/.streamlit/secrets.toml
echo "BASE_URL = \"$BASE_URL\"" >> /app/.streamlit/secrets.toml
echo "MODEL_NAME = \"$MODEL_NAME\"" >> /app/.streamlit/secrets.toml
echo "SUPABASE_URL = \"$SUPABASE_URL\"" >> /app/.streamlit/secrets.toml
echo "SUPABASE_KEY = \"$SUPABASE_KEY\"" >> /app/.streamlit/secrets.toml

streamlit run --server.port 5000 --server.address 0.0.0.0 --browser.serverAddress financedvisor.apps.informatik.uni-bremen.de --server.runOnSave=false --server.allowRunOnSave=false --server.fileWatcherType=none --browser.gatherUsageStats=false --global.developmentMode=false app.py