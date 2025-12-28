# Xác Định Góc Quay Ảnh

Ứng dụng web đơn giản sử dụng Flask và OpenCV để xác định góc nghiêng/góc quay của ảnh thông qua thuật toán Hough Transform.

## 📋 Yêu cầu hệ thống

-   Python 3.8 trở lên
-   pip (Python package manager)
-   Trình duyệt web hiện đại (Chrome, Firefox, Edge)

## 🔧 Cài đặt

### 1. Clone hoặc download project về máy

### 2. Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv .venv
```

### 3. Kích hoạt môi trường ảo

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 4. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

## ⚠️ Chú ý về thư viện đặc biệt

### OpenCV (opencv-python)

-   **Kích thước lớn**: ~50-100MB, cần thời gian download
-   **Yêu cầu**: Có thể cần cài Visual C++ Redistributable trên Windows
-   **Lỗi thường gặp**: Nếu gặp lỗi import cv2, thử:
    ```bash
    pip uninstall opencv-python
    pip install opencv-python-headless
    ```

### Thư viện khác

-   **Flask**: Web framework nhẹ, dễ sử dụng
-   **NumPy**: Tính toán số học, đi kèm với OpenCV
-   **Werkzeug**: Xử lý file upload, tích hợp sẵn trong Flask

## 📂 Dataset

### Vị trí

Dataset nằm trong thư mục `HandWriting/`

### Cấu trúc

```
HandWriting/
├── image_4_rot60.jpg    # Ảnh quay 60 độ
├── image_4_rot90.jpg    # Ảnh quay 90 độ
├── image_4_rot160.jpg   # Ảnh quay 160 độ
└── data.json            # File metadata (nếu có)
```

### Định dạng ảnh hỗ trợ

-   PNG, JPG, JPEG, BMP
-   Kích thước tối đa: 16MB
-   Khuyến nghị: Ảnh tài liệu, form, bảng biểu có kẻ ô hoặc văn bản rõ ràng

### Thêm ảnh test

Bạn có thể thêm ảnh của mình vào thư mục `HandWriting/` hoặc upload trực tiếp qua web interface.

## 🚀 Chạy chương trình

### Chạy Web App (Khuyến nghị)

```bash
python src/app.py
```

Sau đó mở trình duyệt tại: **http://127.0.0.1:5000**

### Chạy Script Test (Command Line)

Để test nhanh thuật toán với 1 ảnh:

```bash
python src/bai1.py
```

**Lưu ý**: Cần sửa đường dẫn ảnh trong file `src/bai1.py` trước khi chạy:

```python
angle = get_skew_angle_hough('HandWriting/image_4_rot60.jpg')  # Thay đổi tên file ở đây
```

## 📖 Hướng dẫn sử dụng Web App

1. Truy cập http://127.0.0.1:5000
2. Click nút **"📁 Chọn Ảnh"**
3. Chọn file ảnh từ máy tính
4. Click **"Phân Tích Góc Quay"**
5. Xem kết quả:
    - Góc nghiêng phát hiện (độ)
    - Ảnh gốc
    - Ảnh với các đường thẳng phát hiện (màu xanh lá)

## 🧪 Kiểm tra chương trình

### Test cơ bản

```bash
# Chạy với ảnh mẫu
python src/bai1.py
```

Kết quả mong đợi:

-   Hiển thị 3 cửa sổ: Original, Canny Edges, Edges (với đường thẳng)
-   In ra góc nghiêng trên console

### Test web app

1. Chạy `python src/app.py`
2. Upload ảnh từ thư mục `HandWriting/`
3. Kiểm tra:
    - Góc hiển thị có hợp lý không
    - Đường thẳng được vẽ có đúng không
    - Thời gian xử lý (2-4 giây)

## 🛠️ Cấu trúc project

```
Bai1/
├── src/                            # Thư mục mã nguồn
│   ├── app.py                      # Flask server chính
│   ├── bai1.py                     # Script test thuật toán
│   └── templates/
│       └── index.html              # Giao diện web
├── HandWriting/                    # Dataset
├── uploads/                        # Thư mục lưu ảnh upload (tự tạo)
├── requirements.txt                # Danh sách thư viện
├── README.md                       # File này
└── BaoCao_XacDinhGocQuayAnh.docx   # Báo cáo chi tiết
```

## ⚙️ Cấu hình

Có thể tùy chỉnh trong `src/app.py`:

-   `MAX_CONTENT_LENGTH`: Kích thước file tối đa (mặc định 16MB)
-   `UPLOAD_FOLDER`: Thư mục lưu file upload
-   Tham số Hough Transform: `threshold`, `minLineLength`, `maxLineGap`
-   Tham số Canny: `threshold1`, `threshold2`

## 🐛 Xử lý lỗi thường gặp

### Lỗi: "No module named 'cv2'"

```bash
pip install opencv-python
```

### Lỗi: "Address already in use"

```bash
# Đổi port trong src/app.py
app.run(debug=True, host='0.0.0.0', port=5001)  # Đổi 5000 thành 5001
```

### Lỗi: "Không tìm thấy đường thẳng nào"

-   Ảnh có thể quá mờ hoặc không có đủ đường thẳng
-   Thử ảnh khác hoặc điều chỉnh tham số Canny/Hough

### Góc phát hiện không chính xác

-   Ảnh có nhiều đường kẻ dọc và ngang → thuật toán có thể nhầm
-   Thử ảnh có nội dung rõ ràng hơn

## 📝 Ghi chú

-   Web server chạy ở chế độ debug, **không dùng cho production**
-   File upload được lưu tạm trong thư mục `uploads/`
-   Thuật toán hoạt động tốt nhất với ảnh tài liệu, form, bảng có kẻ ô

## 📚 Tài liệu tham khảo

-   [OpenCV Hough Line Transform](https://docs.opencv.org/4.x/d9/db0/tutorial_hough_lines.html)
-   [Flask Documentation](https://flask.palletsprojects.com/)
-   [Canny Edge Detection](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)

---

**Tác giả**: Bài tập xử lý ảnh  
**Ngày**: 28/12/2025
