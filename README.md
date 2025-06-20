pcap-analyser
we are making an AI that can parse and analyse network packets, detect anomalies and integrate it with a chatbot that can answer queries related to the network in human-readable language.

OGPW (Open Graph Packet Watcher)
Features
Upload and analyze .pcap files
Streamlit UI for visualization
FastAPI backend for processing
Setup
Clone the repo
pip install -r requirements.txt
Run backend: uvicorn backend.main:app --reload
Run frontend: streamlit run frontend/app.py
