from PIL import Image
import os

img_path = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy\assets\logo.png'
save_path = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy\assets\logo_transparent.png'

img = Image.open(img_path)
img = img.convert("RGBA")

datas = img.getdata()

newData = []
for item in datas:
    # If pixel is very close to white, make it transparent
    if item[0] > 230 and item[1] > 230 and item[2] > 230:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(save_path, "PNG")
print(f"Saved transparent logo to {save_path}")
