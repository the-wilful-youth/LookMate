import React, { useState, useEffect } from 'react';
import { Check, X } from 'lucide-react';

const ResultsView = ({ results, gender, originalImage, detailLevel }) => {
  const [recommendations, setRecommendations] = useState(null);
  const [selectedStyle, setSelectedStyle] = useState(null);

  useEffect(() => {
    if (results?.face_shape) {
      fetchRecommendations(results.face_shape);
    }
  }, [results, gender]);

  const fetchRecommendations = async (faceShape) => {
    try {
      const response = await fetch(`http://localhost:8000/recommendations/${faceShape}?gender=${gender}`);
      const data = await response.json();
      if (data.success) {
        setRecommendations(data.recommendations);
      }
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  if (!results) return null;

  return (
    <div className="results-container">
      <div className="grid-auto-fit" style={{ alignItems: 'start' }}>
        {/* Image Card */}
        <div className="glass-card" style={{ padding: '1rem' }}>
          <h3 style={{ marginBottom: '1rem' }}>Your Photo</h3>
          <div style={{ position: 'relative', borderRadius: '8px', overflow: 'hidden' }}>
            <img 
              src={originalImage} 
              alt="Analyzed" 
              style={{ width: '100%', display: 'block' }} 
            />
            {/* Overlay placeholder - In real app, we'd draw landmarks here */}
            <div style={{ 
              position: 'absolute', 
              bottom: '10px', 
              left: '10px', 
              background: 'rgba(0,0,0,0.7)', 
              padding: '0.5rem 1rem', 
              borderRadius: '20px',
              backdropFilter: 'blur(4px)'
            }}>
              <span style={{ color: '#4ade80', fontWeight: 'bold' }}>Face Shape: {results.face_shape}</span>
            </div>
          </div>
        </div>

        {/* Analysis Card */}
        <div className="glass-card" style={{ padding: '1.5rem' }}>
          <h3 style={{ marginBottom: '1.5rem' }}>Analysis Results</h3>
          
          <div style={{ marginBottom: '2rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1rem' }}>
              <div style={{ 
                width: '60px', 
                height: '60px', 
                borderRadius: '50%', 
                background: 'var(--accent-gradient)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '2rem'
              }}>
                {gender === 'Male' ? '👨' : '👩'}
              </div>
              <div>
                <h4 style={{ fontSize: '1.2rem' }}>{results.face_shape} Face Shape</h4>
                <p style={{ color: 'var(--text-secondary)' }}>Detected with high confidence</p>
              </div>
            </div>
            
            <div className="glass-panel" style={{ padding: '1rem', background: 'rgba(139, 92, 246, 0.1)' }}>
              <p>
                <strong>Characteristics:</strong> {getFaceShapeDescription(results.face_shape)}
              </p>
            </div>
          </div>

          {recommendations && (
            <div>
              <h4 style={{ marginBottom: '1rem' }}>Recommended Styles</h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                {recommendations.hairstyles.slice(0, 3).map((style, idx) => (
                  <div key={idx} style={{ display: 'flex', alignItems: 'start', gap: '0.5rem' }}>
                    <Check size={16} color="var(--accent-primary)" style={{ marginTop: '4px' }} />
                    <span style={{ color: 'var(--text-secondary)' }}>{style}</span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Recommendations Grid */}
      {recommendations && (
        <div style={{ marginTop: '2rem' }}>
          <h3 style={{ marginBottom: '1.5rem' }}>✨ Personalized Recommendations</h3>
          
          <div className="glass-panel" style={{ padding: '2rem' }}>
             {/* This would be a grid of images in a full implementation */}
             <div className="grid-auto-fit">
                {recommendations.hairstyles.map((style, idx) => {
                  // Clean style name for display and file path
                  const styleName = style.split(' - ')[0]; // Remove description if present
                  const fileName = styleName.replace(/ /g, '_'); // Replace spaces with underscores for file
                  const genderPath = gender === 'Male' ? 'Men' : 'Women';
                  const imageUrl = `http://localhost:8000/assets/${genderPath}/hairstyles/${fileName}.png`;

                  return (
                    <div key={idx} className="glass-card" style={{ padding: '1rem', cursor: 'pointer' }}>
                      <div style={{ 
                        height: '200px', 
                        background: 'var(--bg-secondary)', 
                        borderRadius: '8px', 
                        marginBottom: '1rem',
                        overflow: 'hidden',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center'
                      }}>
                        <img 
                          src={imageUrl} 
                          alt={styleName}
                          onError={(e) => {
                            e.target.onerror = null; 
                            e.target.src = 'https://via.placeholder.com/200x200?text=No+Image';
                          }}
                          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                        />
                      </div>
                      <h5 style={{ fontSize: '0.9rem' }}>{styleName}</h5>
                      <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                        {style.split(' - ')[1]}
                      </p>
                      <button className="btn-secondary" style={{ width: '100%', marginTop: '1rem', padding: '0.5rem' }}>
                        Try On
                      </button>
                    </div>
                  );
                })}
             </div>
          </div>
        </div>
      )}
    </div>
  );
};

const getFaceShapeDescription = (shape) => {
  const descriptions = {
    "Oval": "Balanced proportions with gentle curves. The most versatile face shape.",
    "Round": "Soft, curved features with full cheeks. Width and length are similar.",
    "Square": "Strong jawline with angular features. Forehead, cheekbones, and jaw are equal width.",
    "Heart": "Wider forehead tapering to a pointed chin. High cheekbones.",
    "Oblong": "Longer face with balanced width. Straight cheek line."
  };
  return descriptions[shape] || "Unique facial structure.";
};

export default ResultsView;
