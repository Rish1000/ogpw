import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

function App() {
  const [anomalies, setAnomalies] = useState([]);
  const [summary, setSummary] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const onDrop = async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('pcap_file', file);

    try {
      setIsLoading(true);
      const response = await axios.post('http://127.0.0.1:8000/api/analyze/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      setAnomalies(response.data.anomalies || []);
      setSummary(response.data.summary || 'No summary');
    } catch (error) {
      console.error('Upload failed:', error);
      setSummary('Failed to analyze file.');
    } finally {
      setIsLoading(false);
    }
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>Packet Buddy - Anomaly Detection</h1>

      <div
        {...getRootProps()}
        style={{
          border: '2px dashed #999',
          padding: '2rem',
          textAlign: 'center',
          marginBottom: '1rem',
          cursor: 'pointer',
        }}
      >
        <input {...getInputProps()} />
        <p>Drag and drop a .pcap file here, or click to select one.</p>
      </div>

      {isLoading && <p>Analyzing...</p>}
      {summary && <h3>{summary}</h3>}

      {anomalies.length > 0 && (
        <ul>
          {anomalies.map((anomaly, index) => (
            <li key={index} style={{ marginBottom: '1rem' }}>
              <strong>Type:</strong> {anomaly.type} <br />
              <strong>Severity:</strong> {anomaly.severity} <br />
              <strong>Explanation:</strong> {anomaly.explanation} <br />
              <strong>Suggestion:</strong> {anomaly.suggestion || 'N/A'} <br />
              <strong>Packets:</strong> {anomaly.context.affected_packet_indices.join(', ')}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
