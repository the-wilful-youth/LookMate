import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import ResultsView from './components/ResultsView';
import CameraCapture from './components/CameraCapture';
import { Upload, Camera, Video } from 'lucide-react';
import './index.css';

function App() {
  const [inputMode, setInputMode] = useState('upload'); // 'upload', 'webcam', 'live'
  const [gender, setGender] = useState('Male');
  const [detailLevel, setDetailLevel] = useState('quick');
  const [image, setImage] = useState(null);
  const [analysisResults, setAnalysisResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImage(reader.result);
        // Reset results when new image is uploaded
        setAnalysisResults(null); 
      };
      reader.readAsDataURL(file);
      
      // Trigger analysis (mock for now, will connect to backend)
      analyzeImage(file);
    }
  };

  const analyzeImage = async (file) => {
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    formData.append('gender', gender);

    try {
      const response = await fetch('http://localhost:8000/detect', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      if (data.success) {
        setAnalysisResults(data);
      } else {
        console.error('Analysis failed:', data.error);
      }
    } catch (error) {
      console.error('Error analyzing image:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <Sidebar 
        inputMode={inputMode} 
        setInputMode={setInputMode}
        gender={gender}
        setGender={setGender}
        detailLevel={detailLevel}
        setDetailLevel={setDetailLevel}
      />
      
      <main className="main-content">
        <header style={{ marginBottom: '2rem' }}>
          <h1 className="text-gradient" style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>LookMate AI</h1>
          <p style={{ color: 'var(--text-secondary)' }}>Discover your perfect style with AI-powered face shape analysis.</p>
        </header>

        {inputMode === 'upload' && (
          <div className="glass-panel" style={{ padding: '2rem', textAlign: 'center', marginBottom: '2rem' }}>
            {!image ? (
              <div 
                className="upload-zone"
                onClick={() => document.getElementById('file-upload').click()}
                style={{ 
                  border: '2px dashed var(--glass-border)', 
                  borderRadius: '12px', 
                  padding: '4rem',
                  cursor: 'pointer',
                  transition: 'border-color 0.2s'
                }}
              >
                <Upload size={48} color="var(--accent-primary)" style={{ marginBottom: '1rem' }} />
                <h3>Click to Upload Photo</h3>
                <p style={{ color: 'var(--text-secondary)' }}>JPG, PNG supported</p>
                <input 
                  id="file-upload" 
                  type="file" 
                  accept="image/*" 
                  onChange={handleImageUpload} 
                  style={{ display: 'none' }} 
                />
              </div>
            ) : (
              <div style={{ position: 'relative' }}>
                <img 
                  src={image} 
                  alt="Uploaded" 
                  style={{ maxHeight: '400px', borderRadius: '12px', maxWidth: '100%' }} 
                />
                <button 
                  className="btn-secondary"
                  onClick={() => setImage(null)}
                  style={{ position: 'absolute', top: '10px', right: '10px', background: 'rgba(0,0,0,0.5)' }}
                >
                  Change Photo
                </button>
              </div>
            )}
          </div>
        )}

        {inputMode === 'webcam' && (
          <CameraCapture onCapture={(imgSrc, blob) => {
            setImage(imgSrc);
            analyzeImage(blob);
          }} />
        )}

        {analysisResults && (
          <ResultsView 
            results={analysisResults} 
            gender={gender} 
            originalImage={image}
            detailLevel={detailLevel}
          />
        )}
      </main>
    </div>
  );
}

export default App;
