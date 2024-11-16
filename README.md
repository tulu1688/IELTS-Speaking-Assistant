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

### Cài đặt các thư viện Python
Chạy lệnh sau để cài đặt các thư viện cần thiết:

sudo apt install python3-tk
sudo apt-get install python3-pyaudio
sudo apt-get install portaudio19-dev

sudo apt-get install build-essential python3-dev libpq-dev
pip3 install --upgrade pip setuptools wheel

pip3 install gtts SpeechRecognition pyaudio google-generativeai pillow
pip3 install --upgrade Pillow

### 3. **Usage Instructions**
## 🚀 Hướng dẫn sử dụng

##### 1. Thay thế API Key

Mở file Python chính (`IELTS_Speaking_Assistant.py`) và thay thế API key ở **dòng 18**:
Lấy API key từ [Google Generative AI Studio](https://aistudio.google.com/app/apikey).

```python
# Thay "Your GenAI key" bằng API key của bạn
genai.configure(api_key="Your GenAI key")
```

##### 2. Chạy chương trình
Chạy ứng dụng bằng Python:

```bash
python IELTS_Speaking_Assistant.py
```
##### 3. Quy trình sử dụng
1. Nhấn Start để bắt đầu phiên luyện tập.
2. Ứng dụng sẽ đọc chủ đề và câu hỏi cho bạn.
3. Bắt đầu đếm ngược 45 giây để bạn trả lời.
4. Ứng dụng sẽ ghi âm câu trả lời của bạn, chuyển thành văn bản và đánh giá bằng AI.
5. Hiển thị kết quả đánh giá và điểm số trên màn hình.
6. Nhấn Next Question để chuyển sang câu hỏi tiếp theo.

### 4. **Project Structure**
```
📦 IELTS-Speaking-Assistant
├── IELTS-logo.png # Logo của ứng dụng
├── IELTS_Speaking_Assistant.py # File Python chính
├── IELTS_Speaking_Formatted_Final.txt # File câu hỏi
├── temp.mp3 # File âm thanh tạm thời
├── README.md # Tài liệu hướng dẫn
```

## 📜 Tác giả 

- **Long Data Analyst** - Tác giả và nhà phát triển của IELTS Speaking Assistant. Theo dõi kênh TikTok: [@vuthanhlong25aus](https://www.tiktok.com/@vuthanhlong25aus)
