# Code chạy web với Flask
from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import math
import os
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Tạo thư mục uploads nếu chưa tồn tại
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_skew_angle_hough(image_path):
    """Xác định góc nghiêng của ảnh sử dụng Hough Transform - Dựa trên bai1.py"""
    try:
        # 1. Đọc và tiền xử lý
        img = cv2.imread(image_path)
        if img is None:
            return None, None, "Không thể đọc ảnh"
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Dùng Canny để phát hiện biên (cạnh của chữ)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        
        # 2. Dùng HoughLinesP để tìm các đoạn thẳng
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, 
                                minLineLength=100, maxLineGap=10)
        
        if lines is None:
            return 0.0, None, "Không tìm thấy đường thẳng nào!"
        
        # Vẽ các đường thẳng tìm được lên ảnh gốc để kiểm tra
        img_with_lines = img.copy()
        angles = []
        
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img_with_lines, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 3. Tính góc cho từng đường thẳng tìm được
            # Tính góc arctan((y2-y1)/(x2-x1))
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            angles.append(angle)
        
        # 4. Lọc góc (quan trọng)
        # Chỉ lấy các góc nằm trong khoảng nghiêng hợp lý (ví dụ -45 đến 45 độ)
        # để loại bỏ các đường kẻ dọc (nếu có)
        filtered_angles = angles
        
        if len(filtered_angles) == 0:
            return 0.0, None, "Không có góc nào để tính"
        
        # 5. Lấy trung vị (Median) để loại bỏ ngoại lai (Outliers)
        skew_angle = np.median(filtered_angles)
        
        # Chuyển ảnh có đường thẳng sang base64
        _, buffer = cv2.imencode('.jpg', img_with_lines)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return round(skew_angle, 2), img_base64, None
        
    except Exception as e:
        return None, None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Không có file được tải lên'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Chưa chọn file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Xác định góc nghiêng
        angle, img_with_lines, error = get_skew_angle_hough(filepath)
        
        if error:
            return jsonify({'error': error}), 500
        
        # Đọc ảnh gốc và chuyển sang base64
        with open(filepath, 'rb') as f:
            original_img = base64.b64encode(f.read()).decode('utf-8')
        
        return jsonify({
            'angle': round(angle, 2),
            'original_image': f'data:image/jpeg;base64,{original_img}',
            'lines_image': f'data:image/jpeg;base64,{img_with_lines}' if img_with_lines else None
        })
    
    return jsonify({'error': 'Định dạng file không hợp lệ'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
