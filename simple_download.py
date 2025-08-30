#!/usr/bin/env python3
"""
Simple YouTube Downloader - Minimal version
"""

import yt_dlp

def download_best_quality(url):
    """
    Simple function to download YouTube video with best quality
    """
    ydl_opts = {
        # Best quality: video + audio
        'format': 'best[ext=mp4]/best',
        
        # Save with video title
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading: {url}")
        ydl.download([url])
        print("Download completed!")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    download_best_quality(video_url)