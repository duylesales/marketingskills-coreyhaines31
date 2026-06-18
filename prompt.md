tạo ảnh cho ánh sáng và đổ màu nhìn thực tế như ảnh thật  [long_article_13_app_development_state_management.md](file;file:///Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/blog/long_article_13_app_development_state_management.md)  nội dung truyền đạt nên tập trung (nếu những ý tưởng hay content có thể nằm ở bên trái hoặc phải nhưng đảm bảo nằm giữa của khung hình) vào giữa ảnh sau đó thực hiện bước tiếp theo là crop ảnh thành kích thước 16:9 lấy phần giữa

[mô tả của Ai]

Quy trình tạo ảnh siêu thực (hyper-realistic) kết hợp bố cục dàn trải dọc (vertical center) đã được áp dụng mượt mà cho  **Bài số 22 (Web Application PWA)** !

Lần này, AI đã vẽ ra một bức ảnh đậm chất doanh nghiệp: Một phòng họp (boardroom) sang trọng với cửa sổ kính lớn nhìn ra thành phố. Vị CTO tự tin đứng ở bên trái (tay cầm chiếc điện thoại hiển thị PWA), trong khi vị CMO và CFO ngồi chăm chú ở phía bên phải.

Điểm mấu chốt là tất cả các nhân vật và đồ vật trên bàn đều được  **dàn trải ngang nhưng ép hoàn toàn vào phần dải giữa của chiều cao bức ảnh** . Nhờ vậy, khi đoạn script Python chạy ngầm và thực hiện thao tác  **xén bỏ phần thừa trên/dưới để lấy chuẩn 16:9** , không một nhân vật nào bị mất góc mặt hay bị cắt xén vô lý. Bố cục lên ảnh cực kỳ điện ảnh và cân đối.

---

**[MẪU CÂU LỆNH TẠO ẢNH CHUẨN 16:9 CHO BÀI VIẾT MỚI]**

Hãy đọc nội dung bài viết @[đường_dẫn_tới_file_bài_viết.md] và thực hiện chính xác các bước sau:

1. **Tạo ảnh phải đảm bảo chính xác siêu thực:** Sử dụng AI vẽ một bức ảnh minh họa nội dung bài viết với kỹ thuật nhiếp ảnh siêu thực (hyper-realistic), ánh sáng chân thực. Bố cục không gian (Ép trung tâm) chủ yếu dàn trải ngang (nhân vật/đồ vật có thể phân bổ từ trái sang phải).
2. **Cắt ảnh 16:9:** Sử dụng script (Python/Pillow) để tự động cắt ảnh gốc vừa tạo thành kích thước chuẩn 16:9, lấy chính xác phần giữa làm tâm để giữ nguyên trọn vẹn dàn ý chính mà không bị mất góc.
3. **Lưu file chuẩn xác:** Lưu kết quả ảnh đã cắt vào cùng thư mục với file bài viết, bắt buộc đặt tên file theo nguyên tắc: `[tên_file_bài_viết_không_có_đuôi_md]_pic.jpg` (Ví dụ: bài viết là `bai_viet_1.md` thì lưu ảnh thành `bai_viet_1_pic.jpg`).
