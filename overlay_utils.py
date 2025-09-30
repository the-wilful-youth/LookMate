import cv2

def overlay_image(background, overlay, x, y, scale=1.0):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape
    rows, cols, _ = background.shape

    for i in range(h):
        for j in range(w):
            if y+i >= rows or x+j >= cols:
                continue
            alpha = overlay[i][j][3] / 255.0
            if alpha > 0:
                background[y+i, x+j] = (1-alpha) * background[y+i, x+j] + alpha * overlay[i][j][:3]
    return background
