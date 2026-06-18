from PIL import Image, ImageOps

# Load the image
img_path = "/Users/duyle/.gemini/antigravity-ide/brain/24deabcd-5daf-49ce-9101-7ed57277e8b6/tech_debt_thumbnail_16_9_1781684431587.png"
out_path = "/Users/duyle/.gemini/antigravity-ide/brain/24deabcd-5daf-49ce-9101-7ed57277e8b6/tech_debt_thumbnail_16_9_final.png"

try:
    img = Image.open(img_path)
    
    # Calculate 16:9 crop area
    width, height = img.size
    target_ratio = 16.0 / 9.0
    current_ratio = width / height
    
    if current_ratio > target_ratio:
        # Too wide
        new_width = int(target_ratio * height)
        left = (width - new_width) / 2
        top = 0
        right = (width + new_width) / 2
        bottom = height
    else:
        # Too tall
        new_height = int(width / target_ratio)
        left = 0
        top = (height - new_height) / 2
        right = width
        bottom = (height + new_height) / 2
        
    img_cropped = img.crop((left, top, right, bottom))
    
    # Add 30px white margin
    img_with_border = ImageOps.expand(img_cropped, border=30, fill='white')
    
    img_with_border.save(out_path)
    print("Success")
except Exception as e:
    print("Error:", e)
