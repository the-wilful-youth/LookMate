"""
AR Overlay Module for LookMate
Handles virtual try-on of hairstyles and beards using facial landmarks
"""

import cv2
import numpy as np
import os


class AROverlay:
    """Manages AR overlay rendering for hairstyles and beards"""
    
    def __init__(self, assets_path='assets'):
        self.assets_path = assets_path
        self.overlay_cache = {}
        
    def load_overlay_image(self, overlay_path):
        """Load overlay image with alpha channel (cached in RAM)"""
        if overlay_path in self.overlay_cache:
            return self.overlay_cache[overlay_path]
        
        if not os.path.exists(overlay_path):
            return None
        
        overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
        if overlay is not None:
            self.overlay_cache[overlay_path] = overlay
        
        return overlay
    
    def apply_overlay(self, frame, landmarks, overlay_type, gender, style_name=None):
        """
        Apply AR overlay to frame based on facial landmarks
        
        Args:
            frame: Video frame (BGR)
            landmarks: Facial landmark points from MediaPipe
            overlay_type: 'hairstyle' or 'beard'
            gender: 'Male' or 'Female'
            style_name: Optional specific style name
        
        Returns:
            frame: Frame with overlay applied
        """
        if landmarks is None:
            return frame
        
        forehead_top = landmarks[10]
        chin = landmarks[152]
        left_face = landmarks[234]
        right_face = landmarks[454]
        
        face_width = int(np.linalg.norm(left_face - right_face))
        face_height = int(np.linalg.norm(forehead_top - chin))
        
        if overlay_type == 'hairstyle':
            overlay_path = self._get_hairstyle_path(gender, style_name)
            if overlay_path and os.path.exists(overlay_path):
                overlay = self.load_overlay_image(overlay_path)
                if overlay is not None:
                    if gender == 'Female':
                        # Women's hair: Increased width back to 2.3 based on "more widh" feedback
                        hair_width = int(face_width * 2.3) 
                        hair_height = int(face_height * 1.4)
                        # Offset higher to sit on top of head and flow down
                        offset = -int(face_height * 0.65)
                    else:
                        # Men's settings
                        hair_width = int(face_width * 1.6)
                        hair_height = int(face_height * 0.9)
                        offset = -int(face_height * 0.5)
                    
                    frame = self._blend_overlay(
                        frame, overlay, 
                        forehead_top, 
                        hair_width, 
                        hair_height,
                        offset_y=offset
                    )
        
        elif overlay_type == 'beard':
            if gender == 'Male':
                overlay_path = self._get_beard_path(style_name)
                if overlay_path and os.path.exists(overlay_path):
                    overlay = self.load_overlay_image(overlay_path)
                    if overlay is not None:
                        mouth_center = landmarks[13]
                        
                        # Adjusted for better fit: Wider to cover jaw
                        beard_width = int(face_width * 1.1)
                        beard_height = int(face_height * 0.6)
                        
                        # Offset moved UP (negative) to fix "coming down" issue
                        # User requested "more up" -> increased to 0.25
                        offset = -int(face_height * 0.25)
                        
                        frame = self._blend_overlay(
                            frame, overlay,
                            mouth_center,
                            beard_width,
                            beard_height,
                            offset_y=offset
                        )
        
        return frame
    
    def _blend_overlay(self, frame, overlay, anchor_point, width, height, offset_y=0):
        """Blend overlay onto frame at specified position"""
        try:
            # Resize overlay
            overlay_resized = cv2.resize(overlay, (width, height))
            
            # Calculate position (centered on anchor point)
            x = int(anchor_point[0] - width // 2)
            y = int(anchor_point[1] + offset_y)
            
            # Ensure overlay fits within frame
            h, w, _ = frame.shape
            if x < 0:
                overlay_resized = overlay_resized[:, -x:]
                width += x
                x = 0
            if y < 0:
                overlay_resized = overlay_resized[-y:, :]
                height += y
                y = 0
            if x + width > w:
                overlay_resized = overlay_resized[:, :w-x]
                width = w - x
            if y + height > h:
                overlay_resized = overlay_resized[:h-y, :]
                height = h - y
            
            if width <= 0 or height <= 0:
                return frame
            
            # Extract alpha channel if present
            if overlay_resized.shape[2] == 4:
                overlay_rgb = overlay_resized[:, :, :3]
                overlay_alpha = overlay_resized[:, :, 3] / 255.0
                
                # Blend using alpha channel
                roi = frame[y:y+height, x:x+width]
                for c in range(3):
                    roi[:, :, c] = (overlay_alpha * overlay_rgb[:, :, c] + 
                                   (1 - overlay_alpha) * roi[:, :, c])
                frame[y:y+height, x:x+width] = roi
            else:
                # No alpha channel, direct overlay
                frame[y:y+height, x:x+width] = overlay_resized
            
        except Exception as e:
            print(f"Overlay blending error: {e}")
        
        return frame
    
    def _get_hairstyle_path(self, gender, style_name=None):
        """Get path to hairstyle overlay image"""
        gender_folder = 'Men' if gender == 'Male' else 'Women'
        base_path = os.path.join(self.assets_path, gender_folder, 'hairstyles')
        
        if not os.path.exists(base_path):
            return None
        
        if style_name:
            return os.path.join(base_path, f"{style_name}.png")
        
        files = [f for f in os.listdir(base_path) if f.endswith('.png')]
        if files:
            return os.path.join(base_path, files[0])
        
        return None
    
    def _get_beard_path(self, style_name=None):
        """Get path to beard overlay image"""
        base_path = os.path.join(self.assets_path, 'Men', 'beards')
        
        if not os.path.exists(base_path):
            return None
        
        if style_name:
            return os.path.join(base_path, f"{style_name}.png")
        
        # Return first available beard
        files = [f for f in os.listdir(base_path) if f.endswith('.png')]
        if files:
            return os.path.join(base_path, files[0])
        
        return None
    
    def get_available_overlays(self, overlay_type, gender):
        """
        Get list of available overlay styles
        
        Args:
            overlay_type: 'hairstyle' or 'beard'
            gender: 'Male' or 'Female'
        
        Returns:
            list: Available overlay file names (without extension)
        """
        if overlay_type == 'hairstyle':
            gender_folder = 'Men' if gender == 'Male' else 'Women'
            path = os.path.join(self.assets_path, gender_folder, 'hairstyles')
        else:
            if gender != 'Male':
                return []
            path = os.path.join(self.assets_path, 'Men', 'beards')
        
        if not os.path.exists(path):
            return []
        
        files = [os.path.splitext(f)[0] for f in os.listdir(path) if f.endswith('.png')]
        return files


def create_sample_overlays():
    """Create sample overlay placeholders (for demonstration)"""
    import os
    
    dirs = [
        'assets/Men/hairstyles',
        'assets/Men/beards',
        'assets/Women/hairstyles'
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    
    print("✓ Directory structure created for AR overlays")
    print("Note: Add PNG images with transparency for hairstyles and beards to:")
    print("  - assets/Men/hairstyles/")
    print("  - assets/Men/beards/")
    print("  - assets/Women/hairstyles/")


if __name__ == "__main__":
    create_sample_overlays()
