import os
import shutil
import glob

backup_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\Figures\Images_backup"
target_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\Figures\Images"

files = glob.glob(os.path.join(backup_dir, "*.jpg"))
for f in files:
    filename = os.path.basename(f)
    shutil.copy(f, os.path.join(target_dir, filename))
print(f"Restored {len(files)} images from backup.")
