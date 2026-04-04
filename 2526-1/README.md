# Tư duy tính toán — Học kì 1, năm học 2025-2026

**@Giảng viên:** Vui lòng cập nhật các file `lecture-*.html` cho từng buổi học khi cần. Có thể dùng `lecture-template.html` làm mẫu để giữ thống nhất về bố cục và phong cách trình bày.

## Nội dung học kì

| Tuần | Bài giảng | Ghi chú |
|------|-----------|---------|
| 1 | Bài 0: Giới thiệu; Bài 1: Giới thiệu về Tư duy tính toán | |
| 2 | Bài 2: AI hỗ trợ lập trình | |
| 3 | Bài 3: Toán tử, biểu thức, nhập - xuất | |
| 4 | Bài 4: Câu lệnh điều kiện | |
| 5 | Bài 5: Vòng lặp (Loops) | |
| 6–11 | Sinh viên đi học Giáo dục an ninh quốc phòng | |
| 12 | Bài 7: Hàm, đặc tả và kiểm thử | |
| 13 | Thi tiến độ lần 1; Bài 8: Lists, Tuples, Dictionaries; Bài 8a: Iterable và Sets | |
| 14 | Bài 9: Tìm kiếm và sắp xếp | |
| 15 | Bài 10: Lớp, phương thức và lớp con | |
| 16 | Bài 11: Đệ quy | |
| 17 | Bài 11a: Vòng lặp while; Bài 12: Ngoại lệ và gỡ lỗi | |
| 18 | Bài 13: Đọc/ghi tệp | |
| 19 | Thi tiến độ lần 2; Bài 15: Thư viện Python phổ biến | |

## Chạy slide

Thư mục này chứa slide bài giảng viết bằng Reveal.js, có thể serve qua GitHub Pages hoặc máy chủ web cục bộ.
Hai cách chạy dưới đây dùng hai cổng mặc định khác nhau theo cấu hình hiện tại: Node.js dùng `8000`, còn Python dùng `8765`.

### Cách 1: Node.js (hỗ trợ ghi chú giảng viên & tự động tải lại)

1. Cài [Node.js](https://nodejs.org/) (phiên bản `>= 18` theo `package.json`).
2. Trong thư mục `2526-1`, chạy `npm install` để cài dependencies nếu cần.
3. Chạy `npm start` để khởi động server (port 8000).
4. Mở trình duyệt và truy cập http://localhost:8000.

### Cách 2: Python (không cần cài thêm gì)

```bash
# Nếu đang ở thư mục gốc của repo
cd 2526-1
python3 -m http.server 8765
# Mở http://localhost:8765
```

### Serve qua GitHub Pages

Không cần cấu hình gì thêm. Chỉ cần push thay đổi lên nhánh `main`, GitHub Pages sẽ tự động serve nội dung.

## Tạo bài giảng mới

1. Copy `lecture-template.html` thành file mới đặt tên theo dạng `lecture-XX-ten-bai.html`.
2. Chỉnh sửa tiêu đề, ngày và nội dung trong file mới.
3. Commit và push file mới lên repository.

## Tài nguyên minh hoạ

Hình minh hoạ cho các bài giảng được lưu trong thư mục `img/lec*/`.
Khi cần cập nhật hình, hãy chỉnh sửa hoặc thay thế trực tiếp các file trong `img/`.
