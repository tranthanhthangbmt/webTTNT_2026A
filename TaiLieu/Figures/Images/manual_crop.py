import cv2
import glob
import os

def run_manual_crop_tool():
    target_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\Figures\Images"
    backup_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\Figures\Images_backup"
    
    files = glob.glob(os.path.join(target_dir, "*.jpg"))
    if not files:
        print("Không tìm thấy ảnh nào.")
        return

    # Sắp xếp để hiển thị theo thứ tự tên file
    files.sort()

    print("=== CÔNG CỤ CẮT ẢNH THỦ CÔNG ===")
    print("- Dùng chuột TRÁI kéo từ góc trên-trái xuống góc dưới-phải để vẽ vùng chữ nhật.")
    print("- Nhấn 'c' để XÁC NHẬN CẮT phần trong khung đỏ và chuyển sang ảnh tiếp theo.")
    print("- Nhấn 'Enter' để BỎ QUA ảnh này (giữ nguyên không cắt) và chuyển sang ảnh tiếp theo.")
    print("- Nhấn 'b' để TẢI LẠI ẢNH GỐC từ thư mục backup (dùng khi ảnh hiện tại đã bị cắt hỏng/mất chi tiết).")
    print("- Nhấn 'r' để XÓA vùng chọn đỏ hiện tại (vẽ lại từ đầu).")
    print("- Nhấn 'q' hoặc 'ESC' để THOÁT chương trình.")
    print("=================================\n")

    i = 0
    while i < len(files):
        file_path = files[i]
        basename = os.path.basename(file_path)
        
        img = cv2.imread(file_path)
        if img is None:
            i += 1
            continue
            
        clone = img.copy()
        
        rect_pts = []
        drawing = False

        def draw_rect(event, x, y, flags, param):
            nonlocal rect_pts, drawing, clone, img
            
            if event == cv2.EVENT_LBUTTONDOWN:
                rect_pts = [(x, y)]
                drawing = True

            elif event == cv2.EVENT_MOUSEMOVE:
                if drawing:
                    temp_clone = img.copy()
                    cv2.rectangle(temp_clone, rect_pts[0], (x, y), (0, 0, 255), 2)
                    cv2.imshow("Crop Tool", temp_clone)

            elif event == cv2.EVENT_LBUTTONUP:
                drawing = False
                rect_pts.append((x, y))
                cv2.rectangle(clone, rect_pts[0], rect_pts[1], (0, 0, 255), 2)
                cv2.imshow("Crop Tool", clone)

        cv2.namedWindow("Crop Tool")
        cv2.setMouseCallback("Crop Tool", draw_rect)
        
        print(f"[{i+1}/{len(files)}] Đang hiển thị: {basename}")
        
        while True:
            if not drawing:
                cv2.imshow("Crop Tool", clone)
            
            key = cv2.waitKey(10) & 0xFF
            
            if key == 13: # Phím Enter
                print(f"  -> Đã bỏ qua: {basename}")
                i += 1
                break
                
            elif key == ord("c"): # Phím c
                if len(rect_pts) == 2:
                    x1, y1 = rect_pts[0]
                    x2, y2 = rect_pts[1]
                    
                    x_start, x_end = min(x1, x2), max(x1, x2)
                    y_start, y_end = min(y1, y2), max(y1, y2)
                    
                    if x_start < x_end and y_start < y_end:
                        cropped = img[y_start:y_end, x_start:x_end]
                        cv2.imwrite(file_path, cropped)
                        print(f"  -> ĐÃ CẮT VÀ LƯU THÀNH CÔNG: {basename}")
                        i += 1
                        break
                    else:
                        print("  -> Vùng chọn không hợp lệ, hãy kéo chuột chọn lại.")
                        clone = img.copy()
                        rect_pts = []
                else:
                    print("  -> Bạn chưa chọn vùng để cắt (hãy kéo chuột trên ảnh).")
            
            elif key == ord("b"): # Phím b
                backup_path = os.path.join(backup_dir, basename)
                if os.path.exists(backup_path):
                    img = cv2.imread(backup_path)
                    clone = img.copy()
                    rect_pts = []
                    print("  -> Đã tải lại ảnh gốc nguyên bản từ thư mục backup. Hãy vẽ lại vùng cắt.")
                else:
                    print("  -> Không tìm thấy ảnh này trong thư mục backup.")
            
            elif key == ord("r"): # Phím r
                clone = img.copy()
                rect_pts = []
                print("  -> Đã xóa khung đỏ.")
                
            elif key == ord("q") or key == 27: # Phím q hoặc ESC
                print("Đã thoát công cụ.")
                cv2.destroyAllWindows()
                return

    cv2.destroyAllWindows()
    print("Đã hoàn tất duyệt toàn bộ ảnh.")

if __name__ == "__main__":
    run_manual_crop_tool()
