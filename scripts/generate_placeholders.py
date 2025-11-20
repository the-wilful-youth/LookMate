"""
Generate placeholder AR overlay images for demonstration
This creates simple colored rectangles with transparency to demonstrate the AR overlay system
"""

import cv2
import numpy as np
import os

def create_placeholder_hairstyle(filename, color, label):
    """Create a placeholder hairstyle overlay"""
    # Create image with alpha channel (RGBA)
    img = np.zeros((600, 600, 4), dtype=np.uint8)
    
    # Draw a simple shape representing hairstyle
    # Ellipse for hairstyle shape
    cv2.ellipse(img, (300, 200), (250, 180), 0, 180, 360, (*color, 200), -1)
    
    # Add text label
    cv2.putText(img, label, (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), 2)
    cv2.putText(img, "PLACEHOLDER", (180, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255, 200), 2)
    
    # Save image
    cv2.imwrite(filename, img)
    print(f"Created: {filename}")

def create_placeholder_beard(filename, color, label):
    """Create a placeholder beard overlay"""
    # Create image with alpha channel (RGBA)
    img = np.zeros((400, 600, 4), dtype=np.uint8)
    
    # Draw a simple shape representing beard
    # Rounded rectangle for beard
    pts = np.array([
        [150, 50],
        [450, 50],
        [470, 150],
        [450, 250],
        [300, 300],
        [150, 250],
        [130, 150]
    ], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(img, [pts], (*color, 200))
    
    # Add text label
    cv2.putText(img, label, (220, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
    cv2.putText(img, "PLACEHOLDER", (200, 210), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255, 200), 2)
    
    # Save image
    cv2.imwrite(filename, img)
    print(f"Created: {filename}")

def main():
    """Generate all placeholder overlays"""
    
    # Ensure directories exist
    os.makedirs('assets/Men/hairstyles', exist_ok=True)
    os.makedirs('assets/Men/beards', exist_ok=True)
    os.makedirs('assets/Women/hairstyles', exist_ok=True)
    
    print("Generating placeholder AR overlays...\n")
    
    # Male hairstyles
    print("Creating male hairstyle overlays...")
    create_placeholder_hairstyle(
        'assets/Men/hairstyles/pompadour.png',
        (139, 69, 19),  # Brown
        "Pompadour"
    )
    create_placeholder_hairstyle(
        'assets/Men/hairstyles/quiff.png',
        (70, 70, 70),  # Dark gray
        "Quiff"
    )
    create_placeholder_hairstyle(
        'assets/Men/hairstyles/side_part.png',
        (101, 67, 33),  # Dark brown
        "Side Part"
    )
    
    # Female hairstyles
    print("\nCreating female hairstyle overlays...")
    create_placeholder_hairstyle(
        'assets/Women/hairstyles/long_layers.png',
        (139, 69, 19),  # Brown
        "Long Layers"
    )
    create_placeholder_hairstyle(
        'assets/Women/hairstyles/bob_cut.png',
        (70, 70, 70),  # Dark gray
        "Bob Cut"
    )
    create_placeholder_hairstyle(
        'assets/Women/hairstyles/pixie.png',
        (160, 82, 45),  # Medium brown
        "Pixie"
    )
    
    # Beard styles
    print("\nCreating beard style overlays...")
    create_placeholder_beard(
        'assets/Men/beards/full_beard.png',
        (101, 67, 33),  # Dark brown
        "Full Beard"
    )
    create_placeholder_beard(
        'assets/Men/beards/goatee.png',
        (70, 70, 70),  # Dark gray
        "Goatee"
    )
    create_placeholder_beard(
        'assets/Men/beards/stubble.png',
        (90, 60, 40),  # Medium brown
        "Stubble"
    )
    
    print("\n✅ All placeholder overlays created successfully!")
    print("\nNote: These are simple placeholders for demonstration.")
    print("For realistic AR try-on, replace these with actual hairstyle/beard PNG images")
    print("with transparent backgrounds created in image editing software.")

if __name__ == "__main__":
    main()
