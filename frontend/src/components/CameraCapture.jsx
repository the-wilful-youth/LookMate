import React, { useRef, useCallback } from 'react';
import Webcam from 'react-webcam';
import { Camera } from 'lucide-react';

const CameraCapture = ({ onCapture }) => {
  const webcamRef = useRef(null);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    
    // Convert base64 to blob for upload
    fetch(imageSrc)
      .then(res => res.blob())
      .then(blob => {
        onCapture(imageSrc, blob);
      });
  }, [webcamRef, onCapture]);

  return (
    <div className="glass-panel" style={{ padding: '2rem', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <div style={{ 
        position: 'relative', 
        width: '100%', 
        maxWidth: '640px', 
        borderRadius: '12px', 
        overflow: 'hidden',
        border: '2px solid var(--glass-border)'
      }}>
        <Webcam
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width="100%"
          videoConstraints={{ facingMode: "user" }}
        />
      </div>
      
      <button 
        className="btn-primary" 
        onClick={capture}
        style={{ marginTop: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}
      >
        <Camera size={20} />
        Capture Photo
      </button>
    </div>
  );
};

export default CameraCapture;
