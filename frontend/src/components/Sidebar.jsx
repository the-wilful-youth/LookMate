import React from 'react';
import { Upload, Camera, Video, User, Sparkles } from 'lucide-react';

const Sidebar = ({ inputMode, setInputMode, gender, setGender, detailLevel, setDetailLevel }) => {
  return (
    <aside className="glass-panel" style={{ 
      width: '280px', 
      margin: '1rem', 
      padding: '1.5rem',
      display: 'flex',
      flexDirection: 'column',
      gap: '2rem',
      height: 'calc(100vh - 2rem)',
      position: 'sticky',
      top: '1rem'
    }}>
      <div className="logo-area" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
        <div style={{ 
          width: '40px', 
          height: '40px', 
          background: 'var(--accent-gradient)', 
          borderRadius: '10px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '1.5rem'
        }}>✨</div>
        <h2 style={{ fontSize: '1.25rem', fontWeight: '700' }}>LookMate</h2>
      </div>

      <div className="nav-section">
        <h4 style={{ color: 'var(--text-secondary)', fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '1rem' }}>
          Input Method
        </h4>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <NavButton 
            active={inputMode === 'upload'} 
            onClick={() => setInputMode('upload')}
            icon={<Upload size={18} />}
            label="Upload Photo"
          />
          <NavButton 
            active={inputMode === 'webcam'} 
            onClick={() => setInputMode('webcam')}
            icon={<Camera size={18} />}
            label="Use Webcam"
          />
          <NavButton 
            active={inputMode === 'live'} 
            onClick={() => setInputMode('live')}
            icon={<Video size={18} />}
            label="Live Detection"
          />
        </div>
      </div>

      <div className="nav-section">
        <h4 style={{ color: 'var(--text-secondary)', fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '1rem' }}>
          Profile
        </h4>
        <div className="glass-card" style={{ padding: '0.25rem', display: 'flex', background: 'rgba(0,0,0,0.2)' }}>
          <ToggleButton 
            active={gender === 'Male'} 
            onClick={() => setGender('Male')}
            label="Male"
          />
          <ToggleButton 
            active={gender === 'Female'} 
            onClick={() => setGender('Female')}
            label="Female"
          />
        </div>
      </div>

      <div className="nav-section">
        <h4 style={{ color: 'var(--text-secondary)', fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '1rem' }}>
          Recommendations
        </h4>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
            <input 
              type="radio" 
              name="detail" 
              checked={detailLevel === 'quick'} 
              onChange={() => setDetailLevel('quick')}
            />
            <span style={{ color: detailLevel === 'quick' ? 'white' : 'var(--text-secondary)' }}>Quick Overview</span>
          </label>
          <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
            <input 
              type="radio" 
              name="detail" 
              checked={detailLevel === 'detailed'} 
              onChange={() => setDetailLevel('detailed')}
            />
            <span style={{ color: detailLevel === 'detailed' ? 'white' : 'var(--text-secondary)' }}>Detailed Guide</span>
          </label>
        </div>
      </div>
    </aside>
  );
};

const NavButton = ({ active, onClick, icon, label }) => (
  <button 
    onClick={onClick}
    style={{
      display: 'flex',
      alignItems: 'center',
      gap: '0.75rem',
      width: '100%',
      padding: '0.75rem 1rem',
      background: active ? 'rgba(139, 92, 246, 0.15)' : 'transparent',
      border: active ? '1px solid var(--accent-primary)' : '1px solid transparent',
      borderRadius: '8px',
      color: active ? 'white' : 'var(--text-secondary)',
      cursor: 'pointer',
      transition: 'all 0.2s',
      textAlign: 'left'
    }}
  >
    <span style={{ color: active ? 'var(--accent-primary)' : 'inherit' }}>{icon}</span>
    {label}
  </button>
);

const ToggleButton = ({ active, onClick, label }) => (
  <button
    onClick={onClick}
    style={{
      flex: 1,
      padding: '0.5rem',
      background: active ? 'var(--bg-secondary)' : 'transparent',
      border: 'none',
      borderRadius: '8px',
      color: active ? 'white' : 'var(--text-secondary)',
      cursor: 'pointer',
      fontWeight: active ? '600' : '400',
      transition: 'all 0.2s'
    }}
  >
    {label}
  </button>
);

export default Sidebar;
