#!/usr/bin/env python3
"""
YouTube Video Downloader
Downloads YouTube videos with the best available quality (video + audio)
"""

import os
import sys
import argparse
from pathlib import Path

# Check if yt-dlp is installed
try:
    import yt_dlp
except ImportError:
    print("yt-dlp is not installed. Installing now...")
    os.system(f"{sys.executable} -m pip install yt-dlp")
    import yt_dlp


def download_video(url, output_path=".", filename=None):
    """
    Download a YouTube video with the best available quality
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the video (default: current directory)
        filename (str): Custom filename (optional)
    """
    
    # Create output directory if it doesn't exist
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        # Format selection: best video + best audio, merged into single file
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        
        # Output filename template
        'outtmpl': os.path.join(output_path, filename if filename else '%(title)s.%(ext)s'),
        
        # Post-processing options
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 if needed
        }],
        
        # Additional options
        'merge_output_format': 'mp4',  # Merge format
        'quiet': False,  # Show download progress
        'no_warnings': False,
        'ignoreerrors': False,
        
        # Progress hooks
        'progress_hooks': [progress_hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n📥 Downloading video from: {url}")
            print(f"📁 Output directory: {os.path.abspath(output_path)}")
            
            # Extract video info first
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            
            print(f"📹 Video: {video_title}")
            print(f"⏱️  Duration: {format_duration(duration)}")
            print(f"🎬 Resolution: {info.get('resolution', 'Unknown')}")
            print(f"📊 Quality: Best available (video + audio)")
            print("\nStarting download...\n")
            
            # Download the video
            ydl.download([url])
            
            print(f"\n✅ Download completed successfully!")
            
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Download error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


def progress_hook(d):
    """
    Hook to display download progress
    """
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        
        # Clear line and print progress
        print(f"\r⏬ Progress: {percent} | Speed: {speed} | ETA: {eta}", end='', flush=True)
    elif d['status'] == 'finished':
        print(f"\n✓ Download finished, processing...")


def format_duration(seconds):
    """
    Format duration from seconds to human-readable format
    """
    if not seconds:
        return "Unknown"
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def download_playlist(url, output_path="."):
    """
    Download all videos from a YouTube playlist
    """
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n📥 Downloading playlist from: {url}")
            print(f"📁 Output directory: {os.path.abspath(output_path)}\n")
            
            # Extract playlist info
            info = ydl.extract_info(url, download=False)
            playlist_title = info.get('title', 'Unknown Playlist')
            video_count = len(info.get('entries', []))
            
            print(f"📋 Playlist: {playlist_title}")
            print(f"📹 Videos: {video_count}\n")
            
            # Download the playlist
            ydl.download([url])
            
            print(f"\n✅ Playlist download completed successfully!")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Download YouTube videos with best quality (video + audio)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID -o ~/Downloads
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID -f "my_video.mp4"
  %(prog)s --playlist https://www.youtube.com/playlist?list=PLAYLIST_ID
        """
    )
    
    parser.add_argument('url', nargs='?', help='YouTube video or playlist URL')
    parser.add_argument('-o', '--output', default='.', help='Output directory (default: current directory)')
    parser.add_argument('-f', '--filename', help='Custom filename (without extension)')
    parser.add_argument('--playlist', action='store_true', help='Download entire playlist')
    
    args = parser.parse_args()
    
    # Interactive mode if no URL provided
    if not args.url:
        print("🎥 YouTube Video Downloader")
        print("=" * 40)
        args.url = input("Enter YouTube URL: ").strip()
        
        if not args.url:
            print("❌ No URL provided. Exiting.")
            sys.exit(1)
        
        custom_path = input("Enter output directory (press Enter for current): ").strip()
        if custom_path:
            args.output = custom_path
        
        is_playlist = input("Is this a playlist? (y/n): ").strip().lower() == 'y'
        args.playlist = is_playlist
    
    # Validate URL
    if not ('youtube.com' in args.url or 'youtu.be' in args.url):
        print("❌ Invalid URL. Please provide a valid YouTube URL.")
        sys.exit(1)
    
    # Download based on type
    if args.playlist or 'playlist' in args.url:
        download_playlist(args.url, args.output)
    else:
        download_video(args.url, args.output, args.filename)


if __name__ == "__main__":
    main()