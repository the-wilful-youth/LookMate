# AR Overlay Asset Guide for LookMate

## Current Asset Status

### ✅ Men's Hairstyles (6 overlays)
- **pompadour.png** - 413x605px, RGBA, 77.8% transparent ✓
- **quiff.png** - 404x613px, RGBA, 82.2% transparent ✓
- **side_part.png** - 417x598px, RGBA, 79.4% transparent ✓
- **textured_crop.png** - 425x586px, RGBA, 79.7% transparent ✓
- **messy_quiff.png** - 413x605px, RGBA, 77.8% transparent ✓
- **high_fade.png** - 404x613px, RGBA, 82.2% transparent ✓

**Status:** ✅ All properly formatted with transparency

### ⚠️ Men's Beards (3 overlays)
- **full_beard.png** - 585x540px, RGBA, 0% transparent ⚠️
- **stubble.png** - 512x435px, RGBA, 0% transparent ⚠️
- **goatee.png** - 511x460px, RGBA, 0% transparent ⚠️

**Status:** ⚠️ **NO TRANSPARENCY** - Will show as solid rectangles
**Action Needed:** Replace with properly transparent PNG files

### ✅ Women's Hairstyles (3 overlays)
- **long_layers.png** - 600x600px, RGBA, 99.7% transparent ✓
- **bob_cut.png** - 600x600px, RGBA, 99.8% transparent ✓
- **pixie.png** - 600x600px, RGBA, 99.8% transparent ✓

**Status:** ✅ All properly formatted with transparency

---

## Overlay Requirements

### File Format
- **Format:** PNG with alpha channel (RGBA)
- **Transparency:** Background MUST be fully transparent
- **Color Mode:** 8-bit RGBA

### Recommended Sizes
- **Hairstyles:** 400-600px wide, 500-700px tall
- **Beards:** 400-600px wide, 400-500px tall
- **Aspect Ratio:** Portrait orientation preferred

### Positioning Guidelines

#### Hairstyles
- Center the hair at the top-center of the image
- Leave transparent space around the hair
- Hair should cover the forehead area when applied
- Current positioning:
  - Width: Face width × 1.4
  - Height: Face height × 0.7
  - Offset: -35% above forehead

#### Beards
- Center the beard at the top-center of the image
- Beard should align with mouth/chin area
- Include transparent background above and below
- Current positioning:
  - Width: Face width × 0.9
  - Height: Face height × 0.5
  - Offset: +5% below mouth center

---

## File Naming Convention

### Men's Hairstyles
Required names (based on face shape recommendations):
- `pompadour.png`
- `quiff.png`
- `side_part.png`
- `textured_crop.png`
- `messy_quiff.png`
- `high_fade.png`
- `angular_fringe.png`
- `undercut.png`
- `side_swept.png`
- `medium_layers.png`
- `fringe.png`
- `wavy_medium.png`

### Men's Beards
Required names:
- `full_beard.png`
- `stubble.png`
- `goatee.png`
- `circle_beard.png`
- `chinstrap.png`
- `van_dyke.png`
- `mutton_chops.png`
- `extended_goatee.png`
- `rounded_beard.png`

### Women's Hairstyles
Required names:
- `long_layers.png`
- `bob_cut.png`
- `pixie.png`
- `angled_bob.png`
- `high_updo.png`
- `soft_waves.png`
- `layered_long.png`
- `side_swept_bangs.png`
- `shoulder_curls.png`
- `blunt_bangs.png`
- `shoulder_waves.png`
- `layered_bob.png`

---

## How to Create Proper Overlays

### Method 1: Using Photoshop/GIMP
1. Open your hairstyle/beard image
2. Remove background using Magic Wand or Lasso tool
3. Ensure background layer is transparent (checkered pattern)
4. Export as PNG with "Save Transparency" enabled
5. Verify alpha channel in export settings

### Method 2: Using Online Tools
1. Go to remove.bg or similar background removal tool
2. Upload your image
3. Download the PNG with transparent background
4. Verify transparency before using

### Method 3: Using Python (Automated)
```python
from rembg import remove
from PIL import Image

# Remove background
input_img = Image.open('input.png')
output_img = remove(input_img)
output_img.save('output.png')
```

---

## Testing Your Overlays

Run this script to verify your overlays:
```bash
cd /Users/Anurag/Anurag/Projects/LookMate
python << 'SCRIPT'
import cv2
import numpy as np

img = cv2.imread('assets/Men/beards/full_beard.png', cv2.IMREAD_UNCHANGED)
if img.shape[2] == 4:
    alpha = img[:, :, 3]
    transparent = np.sum(alpha < 255)
    print(f"Transparency: {(transparent/alpha.size)*100:.1f}%")
    if transparent == 0:
        print("⚠️  NO TRANSPARENCY - Fix required!")
    else:
        print("✓ Transparency OK")
SCRIPT
```

---

## Quick Fixes Needed

### Priority 1: Fix Beard Transparency
The current beard overlays (full_beard.png, stubble.png, goatee.png) have **no transparency** and will appear as solid rectangles. 

**Fix:** Replace these files with properly transparent versions where only the beard is visible and the background is fully transparent.

### Priority 2: Add Missing Styles
Add overlay files for:
- Additional hairstyles mentioned in recommendations
- Additional beard styles (chinstrap, van_dyke, mutton_chops, etc.)

---

## Integration with LookMate

### File Structure
```
assets/
├── Men/
│   ├── hairstyles/
│   │   ├── pompadour.png
│   │   ├── quiff.png
│   │   └── ...
│   └── beards/
│       ├── full_beard.png
│       ├── stubble.png
│       └── ...
└── Women/
    └── hairstyles/
        ├── long_layers.png
        ├── bob_cut.png
        └── ...
```

### How Overlays are Applied
1. Face detection identifies 468 facial landmarks
2. Key landmarks used for positioning:
   - Hairstyle: Forehead top (landmark 10)
   - Beard: Mouth center (landmark 13)
3. Overlay is resized based on face dimensions
4. Alpha blending applied for realistic appearance
5. Only visible pixels (alpha > 0) are blended

---

## Troubleshooting

### Overlay not showing
- Check file name matches exactly (case-sensitive)
- Verify file is in correct folder
- Ensure PNG has alpha channel

### Solid rectangle instead of overlay
- Image has no transparency
- Re-export with alpha channel enabled

### Overlay too big/small
- Adjust multipliers in `ar_overlay.py`
- Current: hairstyle 1.4x width, beard 0.9x width

### Misaligned overlay
- Check landmark positioning in code
- Adjust offset_y values for vertical alignment

---

## Next Steps

1. **Replace beard overlays** with transparent versions
2. **Add missing styles** from recommendation lists
3. **Test each overlay** in live preview mode
4. **Adjust sizing** if needed in ar_overlay.py
