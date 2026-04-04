# Tư duy tính toán — Trường Đại học Công nghệ, ĐHQGHN

Tài liệu slide bài giảng cho môn **Tư duy tính toán** tại Viện Trí tuệ Nhân tạo (IAI), Trường Đại học Công nghệ (UET), ĐHQGHN.

Slide bài giảng được xây dựng bằng [Reveal.js](https://revealjs.com/).

## Các năm học

| Năm học | Học kì | Thư mục |
|---------|--------|---------|
| 2025-2026 | 1 | [`2526-1/`](2526-1/) |

> Mỗi năm học mới sẽ được thêm vào dưới dạng một thư mục riêng (ví dụ: `2627-1/`).

## Cấu trúc mỗi năm học

> Cấu trúc dưới đây chỉ mang tính khái quát; một số thư mục có thể có thêm tài nguyên, plugin hoặc file cấu hình phụ trợ.

```text
.
├── index.html                  # Trang chủ liệt kê các năm học
├── XXXX-X/
│   ├── index.html              # Trang chủ của năm học
│   ├── lecture-*.html          # Slide bài giảng (Reveal.js)
│   ├── lecture-style.css       # CSS dùng chung cho các slide
│   ├── lecture-template.html   # Mẫu để tạo bài giảng mới
│   ├── img/                    # Hình minh hoạ cho bài giảng
│   ├── plugin/                 # Plugin Reveal.js được dùng trực tiếp
│   ├── revealjs/               # Mã nguồn/tài nguyên Reveal.js được vendor
│   ├── package.json            # Cấu hình npm cho việc serve/build
│   └── gulpfile.js             # Tác vụ phục vụ slide cục bộ
```

## Thêm năm học mới

1. Tạo thư mục mới (ví dụ: `2627-1/`) bằng cách copy từ năm học gần nhất.
2. Cập nhật `index.html` ở root để thêm link tới năm học mới.
3. Bổ sung dòng tương ứng trong bảng "Các năm học" của file `README.md` này.
4. Cập nhật `README.md` trong thư mục năm học mới cho đúng lịch giảng dạy và hướng dẫn sử dụng.
