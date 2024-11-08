# IELTS Speaking Assistant 🎤

## 📖 Giới thiệu
**IELTS Speaking Assistant** là một ứng dụng Python hỗ trợ người dùng luyện tập kỹ năng nói IELTS. Ứng dụng cung cấp giao diện tương tác, đọc câu hỏi, nhận diện giọng nói và đánh giá câu trả lời dựa trên AI.

### Các tính năng:
- **Giao diện tương tác**: Được xây dựng bằng `tkinter` giúp dễ sử dụng.
- **Đọc câu hỏi bằng giọng nói**: Sử dụng Google Text-to-Speech (`gTTS`).
- **Nhận diện giọng nói**: Chuyển giọng nói của người dùng thành văn bản.
- **Đếm ngược thời gian thực**: Đếm ngược 45 giây cho mỗi câu trả lời.
- **Đánh giá tự động**: Sử dụng AI Generative của Google để đánh giá và đưa ra điểm số IELTS.

## 🛠️ Cài đặt

### Yêu cầu:
1. **Python 3.8+** đã cài đặt trên máy.
2. **API Key của Google Generative AI**: Lấy API key từ [Google Generative AI Studio](https://aistudio.google.com/app/apikey).

### Cài đặt các thư viện Python
Chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install gtts SpeechRecognition pyaudio google-generativeai pillow
Lưu ý: Nếu gặp lỗi khi cài đặt pyaudio, hãy thử:

- Trên macOS: brew install portaudio
- Trên Ubuntu/Linux: sudo apt install portaudio19-dev


---

### 3. **Configuration**
```markdown
## ⚙️ Cấu hình

### 1. Thay thế API Key
Mở file Python chính (`IELTS_Speaking_Assistant.py`) và thay thế API key ở **dòng 18**:

```python
# Thay "Your GenAI key" bằng API key của bạn
genai.configure(api_key="Your GenAI key")
