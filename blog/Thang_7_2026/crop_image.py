import os
import sys
from PIL import Image

def crop_to_16_9(image_path, output_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # Calculate target dimensions for 16:9 ratio
        target_ratio = 16 / 9
        current_ratio = width / height
        
        if current_ratio > target_ratio:
            # Image is wider than 16:9, crop width evenly from both sides (center)
            new_width = int(height * target_ratio)
            left = (width - new_width) / 2
            top = 0
            right = (width + new_width) / 2
            bottom = height
        else:
            # Image is taller than 16:9, crop height evenly from top and bottom (center)
            new_height = int(width / target_ratio)
            left = 0
            top = (height - new_height) / 2
            right = width
            bottom = (height + new_height) / 2
            
        # Crop keeping exactly the center
        cropped_img = img.crop((left, top, right, bottom))
        
        # Save output
        cropped_img.save(output_path, quality=95)
        print(f"✅ Đã cắt ảnh thành 16:9 và lưu thành công tại:\n{output_path}")
        
    except Exception as e:
        print(f"❌ Lỗi khi xử lý ảnh: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python crop_image.py <đường_dẫn_ảnh_gốc>")
        sys.exit(1)
        
    input_image = sys.argv[1]
    
    # Đường dẫn thư mục và tên file đầu ra theo yêu cầu
    base_dir = "/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/blog/Thang_7_2026"
    output_name = "long_article_72_dedicated_development_team_async_standup_pic.jpg"
    output_path = os.path.join(base_dir, output_name)
    
    if not os.path.exists(input_image):
        print(f"❌ Không tìm thấy file ảnh gốc: {input_image}")
        sys.exit(1)
        
    crop_to_16_9(input_image, output_path)
