# LookMate - Quick Reference

## 🚀 Quick Start Commands

```bash
# Option 1: Using the start script (Recommended)
./start.sh

# Option 2: Manual start
source myenv/bin/activate
streamlit run app.py

# Option 3: Fresh install
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `face_shape_detector.py` | Face detection & classification |
| `recommendation_engine.py` | Style recommendations |
| `ar_overlay.py` | AR virtual try-on system |
| `generate_placeholders.py` | Generate sample overlays |
| `start.sh` | Quick start script |

## 📚 Documentation

| Document | Contents |
|----------|----------|
| `README.md` | Project overview & setup |
| `USER_GUIDE.md` | Complete user manual |
| `DEVELOPER_DOCS.md` | Technical documentation |
| `IMPLEMENTATION_SUMMARY.md` | Completion report |
| `CHECKLIST.md` | Feature verification |
| `CHANGELOG.md` | Changes log |
| `COMPLETION_SUMMARY.txt` | Executive summary |

## 🎨 AR Asset Locations

```
assests/
├── Men/
│   ├── hairstyles/    # Male hairstyle overlays (PNG)
│   └── beards/        # Beard style overlays (PNG)
└── Women/
    └── hairstyles/    # Female hairstyle overlays (PNG)
```

## 🤖 Model Locations

```
model/
├── men.keras      # Male face shape classifier
├── Female.h5      # Female face shape classifier
└── gender.keras   # Gender detection (optional)
```

## 🧪 Testing Commands

```bash
# Test module imports
python3 -c "from recommendation_engine import get_recommendations; print('✓ OK')"
python3 -c "from ar_overlay import AROverlay; print('✓ OK')"

# Run verification test
python3 << 'EOF'
from recommendation_engine import get_recommendations
from ar_overlay import AROverlay

print("Testing recommendations...")
recs = get_recommendations('Oval', 'Male')
print(f"✓ {len(recs['hairstyles'])} hairstyles found")

print("Testing AR overlays...")
ar = AROverlay()
styles = ar.get_available_overlays('hairstyle', 'Male')
print(f"✓ {len(styles)} overlays found")
print("All tests passed!")
EOF

# Generate new placeholder overlays
python3 generate_placeholders.py
```

## 🎯 Common Tasks

### Adding Custom AR Overlays

```bash
# 1. Create PNG with transparent background (use Photoshop/GIMP)
# 2. Save to appropriate folder:
#    - Male hairstyles: assests/Men/hairstyles/your_style.png
#    - Female hairstyles: assests/Women/hairstyles/your_style.png
#    - Beards: assests/Men/beards/your_style.png
# 3. Restart the app
```

### Checking Available Overlays

```bash
python3 -c "
from ar_overlay import AROverlay
ar = AROverlay()
print('Male hairstyles:', ar.get_available_overlays('hairstyle', 'Male'))
print('Female hairstyles:', ar.get_available_overlays('hairstyle', 'Female'))
print('Beards:', ar.get_available_overlays('beard', 'Male'))
"
```

### Getting Recommendations

```bash
python3 -c "
from recommendation_engine import get_recommendations
recs = get_recommendations('Oval', 'Male')
for style in recs['hairstyles']:
    print(f'  - {style}')
"
```

## 🔧 Troubleshooting

### Webcam Issues
```bash
# Check webcam availability
ls /dev/video*

# Test with OpenCV
python3 -c "import cv2; cap = cv2.VideoCapture(0); print('OK' if cap.isOpened() else 'FAIL'); cap.release()"
```

### Module Import Issues
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Port Already in Use
```bash
# Kill existing Streamlit process
pkill -f streamlit

# Or use different port
streamlit run app.py --server.port 8502
```

## 📊 Project Statistics

```bash
# Count Python lines
find . -name "*.py" -not -path "./myenv/*" | xargs wc -l

# Count documentation
wc -l *.md

# List all files
find . -type f -not -path "./myenv/*" -not -path "./.git/*" | sort
```

## 🎨 Face Shapes Reference

| Shape | Ratio | Key Features |
|-------|-------|--------------|
| Oval | 1.4-1.6 | Balanced, gentle curves |
| Round | 1.0-1.2 | Soft, full cheeks |
| Square | 1.0-1.3 | Strong jaw, angular |
| Heart | 1.4+ | Wide forehead, narrow chin |
| Oblong | 1.6+ | Long, narrow |

## 🚀 Deployment

### Streamlit Cloud
```bash
# 1. Push to GitHub
git add .
git commit -m "Complete implementation"
git push origin main

# 2. Deploy on streamlit.io
# - Connect repository
# - Set main file: app.py
# - Deploy
```

### Local Server
```bash
# Run on custom port
streamlit run app.py --server.port 8501

# Run in background
nohup streamlit run app.py &

# Stop background process
pkill -f streamlit
```

## 📝 Git Commands

```bash
# Status
git status

# Add all changes
git add .

# Commit
git commit -m "Your message"

# Push
git push origin main

# View changes
git diff

# View log
git log --oneline
```

## 💡 Tips

- For best results, use clear front-facing photos with good lighting
- AR overlays work best with neutral facial expressions
- Enable AR before starting live detection for real-time try-on
- Replace placeholder overlays with professional renders for realistic results
- Check DEVELOPER_DOCS.md for advanced customization

## 🆘 Getting Help

1. Check USER_GUIDE.md for usage questions
2. Check DEVELOPER_DOCS.md for technical questions
3. Review IMPLEMENTATION_SUMMARY.md for feature details
4. Email: anuragbhowmick1711@gmail.com

---

**LookMate v1.0** - Your AI-Powered Style Partner ✨
