import cv2
import numpy as np
import math

def get_skew_angle_hough(image_path):
    # 1. Đọc và tiền xử lý
    img = cv2.imread(image_path)
    cv2.imshow("Original", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Dùng Canny để phát hiện biên (cạnh của chữ)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    cv2.imshow("Canny Edges", edges)
    # 2. Dùng HoughLinesP để tìm các đoạn thẳng

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, 
                            minLineLength=100, maxLineGap=10)
    
    if lines is None:
        print("Không tìm thấy đường thẳng nào!")
        return 0.0

    imcopy = img.copy()
    # Vẽ các đường thẳng tìm được lên ảnh gốc để kiểm tra
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(imcopy, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Hiển thị ảnh Line 
    cv2.imshow("Edges", imcopy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    angles = []
    # 3. Tính góc cho từng đường thẳng tìm được
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # Tính góc arctan((y2-y1)/(x2-x1))
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)
    
    # 4. Lọc góc (quan trọng)
    # Chỉ lấy các góc nằm trong khoảng nghiêng hợp lý (ví dụ -45 đến 45 độ)
    # để loại bỏ các đường kẻ dọc (nếu có)
    filtered_angles = angles
    
    if len(filtered_angles) == 0:
        return 0.0
        
    # 5. Lấy trung vị (Median) để loại bỏ ngoại lai (Outliers)
    skew_angle = np.median(filtered_angles)
    
    print(f"Góc nghiêng phát hiện (Hough): {skew_angle:.2f} độ")
    return skew_angle

angle = get_skew_angle_hough('HandWriting/image_4_rot160.jpg')
