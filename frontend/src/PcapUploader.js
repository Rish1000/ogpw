// frontend/src/PcapUploader.js
import React, { useState } from "react";
import axios from "axios";

function PcapUploader() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:8000/analyze/", formData);
      setResults(response.data);
    } catch (error) {
      alert("Error analyzing pcap: " + error.message);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Upload .pcap File</h2>
      <input type="file" accept=".pcap" onChange={handleFileChange} />
      <button onClick={handleUpload}>Analyze</button>

      {results && (
        <div>
          <h3>{results.summary}</h3>
          <ul>
            {results.anomalies.map((a, i) => (
              <li key={i}>
                <strong>{a.type}</strong> ({a.severity}): {a.explanation}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default PcapUploader;
