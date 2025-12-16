import yt_dlp
import os

def download_tiktok_channel(channel_url, cookie_file='cookies.txt'):
    # Tạo thư mục tên là 'downloads' để chứa video
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    # Cấu hình cho yt-dlp
    ydl_opts = {
        # Đường dẫn file cookie bạn đã lấy
        'cookiefile': "D:\tool tiktok\tải vd hàng loạt\cookies.txt", 
        
        # Bỏ qua lỗi (ví dụ video bị xóa hoặc lỗi mạng) để chạy tiếp video sau
        'ignoreerrors': True,
        
        # Định dạng tên file: Tên người dùng - Ngày upload - ID video
        'outtmpl': 'downloads/%(uploader)s - %(upload_date)s - %(id)s.%(ext)s',
        
        # Tự động chọn chất lượng tốt nhất
        'format': 'bestvideo+bestaudio/best',
        
        # Giả lập trình duyệt để tránh bị chặn
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    print(f"--- Đang bắt đầu quét kênh: {channel_url} ---")
    print("Quá trình này có thể mất thời gian tùy vào số lượng video...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # yt-dlp tự động nhận diện link kênh và quét toàn bộ video
            ydl.download([channel_url])
            
        print("\n--- Hoàn tất tải xuống! ---")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# --- CẤU HÌNH CHẠY TOOL ---
if __name__ == "__main__":
    # Link kênh bạn muốn tải
    link_kenh = input("Nhập link kênh TikTok (ví dụ https://www.tiktok.com/@vtv24news): ")
    
    # Kiểm tra xem file cookie có tồn tại không
    if os.path.exists('cookies.txt'):
        download_tiktok_channel(link_kenh, 'cookies.txt')
    else:
        print("CẢNH BÁO: Không tìm thấy file 'cookies.txt'.")
        print("TikTok có thể chặn nếu tải nhiều video mà không có cookie.")
        choice = input("Bạn có muốn thử chạy không cần cookie? (y/n): ")
        if choice.lower() == 'y':
            download_tiktok_channel(link_kenh, None)