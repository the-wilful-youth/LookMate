# LookMate - User Guide

## Quick Start Guide

### 1. Launch the Application
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`

### 2. Select Your Gender
- Use the sidebar to choose **Male** or **Female**
- This ensures accurate face shape detection using the appropriate ML model

### 3. Choose Input Method

#### 📤 Upload Photo
- Click "Browse files" to select an image from your device
- Supported formats: JPG, JPEG, PNG
- Best results: Clear, front-facing photos with good lighting

#### 📸 Webcam
- Click "Capture your photo" to take a picture
- Position your face in the center
- Ensure good lighting for best detection

#### 🎥 Live Detection
- Click "Start Detection" to begin real-time analysis
- Your face shape will be detected continuously
- AR overlays update in real-time
- Click "Stop Detection" when finished

### 4. Enable AR Virtual Try-On (Optional)
- Check "Enable AR Overlays" in the sidebar
- Select hairstyle and/or beard style from dropdowns
- See the virtual style applied to your image or live feed

### 5. View Your Results
The app will display:
- ✅ Your detected face shape
- 💇 Personalized hairstyle recommendations
- ✨ Beard/makeup suggestions based on your gender
- 💡 Professional styling tips

---

## Face Shape Reference Guide

### Oval Face 🥚
**Characteristics:**
- Balanced proportions
- Gentle curves
- Slightly wider cheekbones
- Rounded jawline
- Length is about 1.5x width

**Celebrity Examples:**
- Male: George Clooney, Idris Elba
- Female: Beyoncé, Jessica Alba

**Style Tips:**
- Most versatile face shape
- Can wear almost any hairstyle
- Experiment freely!

---

### Round Face ⭕
**Characteristics:**
- Soft, curved features
- Full cheeks
- Equal width and length
- Minimal angles

**Celebrity Examples:**
- Male: Leonardo DiCaprio, Jack Black
- Female: Selena Gomez, Ginnifer Goodwin

**Style Tips:**
- Add height on top
- Keep sides shorter
- Create vertical lines
- Avoid blunt, horizontal cuts

---

### Square Face ⬜
**Characteristics:**
- Strong, angular jawline
- Broad forehead
- Similar width at forehead, cheeks, and jaw
- Defined features

**Celebrity Examples:**
- Male: Brad Pitt, Henry Cavill
- Female: Angelina Jolie, Olivia Wilde

**Style Tips:**
- Soften angles with curves
- Add texture and movement
- Rounded styles work best
- Avoid geometric cuts

---

### Heart Face 💖
**Characteristics:**
- Wider forehead
- High cheekbones
- Narrow, pointed chin
- Tapers from top to bottom

**Celebrity Examples:**
- Male: Ryan Gosling, Justin Timberlake
- Female: Reese Witherspoon, Scarlett Johansson

**Style Tips:**
- Add width at chin level
- Minimize forehead width
- Side-swept styles work well
- Fuller beards for men

---

### Oblong Face 📏
**Characteristics:**
- Longer than it is wide
- Elongated appearance
- Straight cheek line
- Ratio > 1.6 (length to width)

**Celebrity Examples:**
- Male: Adam Levine, Benedict Cumberbatch
- Female: Sarah Jessica Parker, Liv Tyler

**Style Tips:**
- Add width to sides
- Avoid height on top
- Horizontal lines preferred
- Bangs/fringe work well

---

## AR Virtual Try-On Guide

### Setting Up AR Overlays

1. **Enable AR in Sidebar**
   - Check the "Enable AR Overlays" box
   - AR controls will appear

2. **Choose a Hairstyle**
   - Select from available hairstyle options
   - Preview updates in real-time
   - Choose "None" to remove overlay

3. **Choose a Beard (Males Only)**
   - Select from available beard styles
   - Preview updates immediately
   - Mix and match with hairstyles

### Tips for Best AR Experience
- ✅ Face the camera directly
- ✅ Ensure even lighting
- ✅ Stay at a consistent distance
- ✅ Minimal head movement for best alignment
- ✅ Remove glasses for better detection

### Adding Custom AR Overlays

Want to try more styles? Add your own!

1. Create PNG images with **transparent backgrounds**
2. Place in the correct folder:
   - Male hairstyles: `assests/Men/hairstyles/`
   - Beards: `assests/Men/beards/`
   - Female hairstyles: `assests/Women/hairstyles/`
3. Restart the app
4. New styles appear in dropdowns

**Image Guidelines:**
- Format: PNG with alpha transparency
- Resolution: 500x500 to 1000x1000 pixels
- Center the hairstyle/beard in image
- Use professional photo editing software

---

## Troubleshooting

### Face Not Detected
**Possible Causes:**
- Poor lighting
- Face not centered
- Glasses or accessories blocking face
- Low image quality

**Solutions:**
- Ensure bright, even lighting
- Face camera directly
- Remove glasses
- Use high-quality images

### Webcam Not Working
**Solutions:**
- Grant camera permissions in browser
- Close other apps using camera
- Try different browser
- Restart application

### AR Overlays Not Appearing
**Check:**
- AR is enabled in sidebar
- Overlay files exist in assests folder
- PNG files have transparent backgrounds
- Files are named correctly

### Slow Performance
**Solutions:**
- Close other applications
- Use "Upload Photo" mode instead of live
- Reduce video resolution
- Ensure good system performance

---

## Advanced Features

### Downloading Facial Landmarks
- Detected landmarks can be exported as JSON
- Useful for developers and researchers
- Click "Download Landmarks" button in results

### Session Persistence
- Face shape saved in session state
- Recommendations persist across pages
- AR settings maintained during session

---

## Privacy & Data

### Data Collection
LookMate operates **100% locally**:
- ✅ No images uploaded to servers
- ✅ No data collected or stored
- ✅ All processing done on your device
- ✅ Complete privacy guaranteed

### Camera Access
- Used only for capture/detection
- Never recorded or transmitted
- Controlled by browser permissions

---

## Keyboard Shortcuts

- `R` - Refresh page
- `Ctrl/Cmd + R` - Hard refresh
- `Esc` - Stop webcam (in some browsers)

---

## Best Practices

### For Accurate Detection
1. Good, even lighting
2. Neutral expression
3. Hair pulled back (to see face shape clearly)
4. Front-facing position
5. High-resolution image

### For Best Recommendations
1. Select correct gender
2. Ensure accurate face shape detection
3. Consider multiple recommendations
4. Consult professional stylist for final decision

---

## FAQ

**Q: Which face shape is most common?**
A: Oval is considered the most balanced, but all shapes are equally beautiful!

**Q: Can my face shape change?**
A: Face shape is primarily determined by bone structure, but weight changes and aging can affect appearance.

**Q: How accurate is the detection?**
A: Our ML models achieve ~85-90% accuracy. For best results, use clear, front-facing photos.

**Q: Can I save my results?**
A: Take a screenshot or use your browser's save image function.

**Q: Does it work on all ages?**
A: Yes! Face shape detection works for adults of all ages.

**Q: What if I'm between two face shapes?**
A: Read recommendations for both shapes and choose styles you prefer!

---

## Support

For technical issues or questions:
- Email: anuragbhowmick1711@gmail.com
- GitHub: https://github.com/the-wilful-youth/LookMate

---

**Enjoy your personalized styling experience with LookMate!** ✨
