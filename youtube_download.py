from yt_dlp import YoutubeDL
import os

# 设置代理
PROXY = "http://127.0.0.1:7890"

def download_youtube_video(video_url, output_path="/Users/Daglas/Desktop"):
    """
    从给定的 YouTube 视频链接下载视频文件。

    参数：
    - video_url: str，YouTube 视频链接。
    - output_path: str，保存文件的路径（默认桌面）。
    """
    # 确保输出路径存在
    os.makedirs(output_path, exist_ok=True)

    # 配置 youtube-dl 选项
    ydl_opts = {
        'format': 'best',  # 下载最佳质量
        'outtmpl': f"{output_path}/%(title)s.%(ext)s",  # 直接使用绝对路径
        'proxy': PROXY,  # 设置代理
        'noplaylist': True,  # 不下载播放列表
        'quiet': False,  # 显示进度信息
        'no_warnings': False,  # 显示警告信息
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            # 开始下载
            info_dict = ydl.extract_info(video_url, download=True)
            print(f"视频已下载至: {output_path}/{info_dict['title']}.{info_dict['ext']}")
    except Exception as e:
        print(f"下载失败: {str(e)}")

if __name__ == "__main__":
    # 示例用法：将此脚本保存为 download.py 后，通过命令行执行：
    # python download.py <YouTube_URL> [download_path]
    import sys

    if len(sys.argv) < 2:
        print("用法：python download.py <YouTube_URL> [download_path]")
        sys.exit(1)
    
    # 从命令行参数中获取
    url = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "."

    download_youtube_video(url, path)