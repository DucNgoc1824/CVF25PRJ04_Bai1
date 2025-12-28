# Xác Định Góc Quay Ảnh

Ứng dụng web hiện đại sử dụng Streamlit và OpenCV để xác định góc nghiêng/góc quay của ảnh thông qua thuật toán Hough Transform.

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

### Streamlit

-   **Web framework hiện đại**: Tự động tạo giao diện đẹp, không cần HTML/CSS
-   **Hot reload**: Tự động cập nhật khi sửa code
-   **Tương thích tốt**: Với NumPy, Pandas, Matplotlib, OpenCV

## 📂 Dataset

### Vị trí

Dataset nằm trong thư mục `HandWriting/`

### Cấu trúc

```
HandWriting/
├── image_4_rot60.jpg    # Ảnh quay 60 độ
├── image_4_rot90.jpg    # Ảnh quay 90 độ
├── image_4_rot160.jpg   # Ảnh quay 160 độ
└── data.json            # File metadata với thông tin góc quay
```

### Định dạng ảnh hỗ trợ

-   PNG, JPG, JPEG, BMP
-   Kích thước tối đa: 200MB (Streamlit)
-   Khuyến nghị: Ảnh tài liệu, form, bảng biểu có kẻ ô hoặc văn bản rõ ràng

## 🚀 Chạy chương trình

### Chạy Web App

```bash
streamlit run src/app.py
```

Sau đó mở trình duyệt tại: **http://localhost:8501**

### Chạy Script Test (Command Line)

```bash
python src/bai1.py
```

**Lưu ý**: Cần sửa đường dẫn ảnh trong file `src/bai1.py` trước khi chạy.

## 📖 Hướng dẫn sử dụng Web App

1. Truy cập **http://localhost:8501**
2. Kéo thả ảnh vào vùng upload hoặc click **"Browse files"**
3. Chọn file ảnh từ máy tính
4. Kết quả hiển thị tự động:
    - 📊 Góc nghiêng phát hiện (độ)
    - 🖼️ Ảnh gốc
    - 🔍 Phát hiện cạnh (Canny)
    - 📐 Đường thẳng phát hiện (màu xanh lá)
5. Click **"⬇️ Tải ảnh kết quả"** để download

## 🎨 Tính năng nổi bật

✨ **Giao diện hiện đại**: Gradient màu sắc, layout responsive  
🎯 **Drag & Drop**: Kéo thả ảnh dễ dàng  
⚙️ **Tùy chỉnh tham số**: Slider điều chỉnh Hough Transform real-time  
📊 **4 view ảnh**: Original, Canny Edges, Lines Detection, Info  
💾 **Download kết quả**: Lưu ảnh đã phân tích  
📱 **Responsive**: Hoạt động tốt trên mobile/tablet  
🚀 **Nhanh**: Xử lý trong 1.5-4 giây

## 🛠️ Cấu trúc project

```
Bai1/
├── src/                            # Thư mục mã nguồn
│   ├── app.py                      # Streamlit app chính
│   └── bai1.py                     # Script test thuật toán
├── HandWriting/                    # Dataset
├── requirements.txt                # Danh sách thư viện
├── README.md                       # File này
├── .gitignore                      # Loại trừ file không cần
└── BaoCao_XacDinhGocQuayAnh.docx   # Báo cáo chi tiết
```

## 🐛 Xử lý lỗi thường gặp

### Lỗi: "No module named 'cv2'"

```bash
pip install opencv-python
```

### Lỗi: "No module named 'streamlit'"

```bash
pip install streamlit
```

### Lỗi: "Address already in use" (port 8501)

Streamlit tự động thử port khác (8502, 8503...)

### Lỗi: "Không tìm thấy đường thẳng nào"

-   Ảnh có thể quá mờ hoặc không có đủ đường thẳng
-   Thử ảnh khác hoặc điều chỉnh tham số qua sidebar

## 📚 Tài liệu tham khảo

-   [OpenCV Hough Line Transform](https://docs.opencv.org/4.x/d9/db0/tutorial_hough_lines.html)
-   [Streamlit Documentation](https://docs.streamlit.io/)
-   [Canny Edge Detection](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)

---

**Công nghệ**: Streamlit + OpenCV + NumPy  
**Ngày**: 28/12/2025
