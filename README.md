# YouTube Video Downloader

A powerful and user-friendly Python application for downloading YouTube videos and playlists with the best available quality (video + audio merged).

## Features

- 🎥 Download individual YouTube videos
- 📋 Download entire YouTube playlists
- 🎬 Automatically selects best available quality (video + audio)
- 📁 Custom output directory support
- 📝 Custom filename support
- 🖥️ Command-line interface with arguments
- 🔄 Interactive mode for easy use
- 📊 Real-time download progress tracking
- ⚡ Auto-installation of dependencies

## Requirements

- Python 3.6 or higher
- yt-dlp (automatically installed if missing)

## Installation & Setup

### 1. Create a Virtual Environment (Recommended)

Creating a virtual environment helps keep your system Python clean and avoids dependency conflicts:

#### On Windows:
```bash
# Create virtual environment
python -m venv youtube-downloader-env

# Activate virtual environment
youtube-downloader-env\Scripts\activate
```

#### On macOS/Linux:
```bash
# Create virtual environment
python3 -m venv youtube-downloader-env

# Activate virtual environment
source youtube-downloader-env/bin/activate
```

### 2. Install Dependencies

After activating your virtual environment, install the required dependencies:

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install yt-dlp directly
pip install yt-dlp
```

**Note:** The application will automatically install `yt-dlp` if it's not found, but it's recommended to install it manually in your virtual environment.

## Usage

### Command Line Interface

#### Basic Video Download
```bash
# Download a single video to current directory
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

#### Custom Output Directory
```bash
# Download to a specific directory
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -o ~/Downloads
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --output /path/to/downloads
```

#### Custom Filename
```bash
# Download with custom filename (without extension)
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -f "my_video"
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --filename "my_custom_name"
```

#### Playlist Download
```bash
# Download entire playlist
python youtube_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist

# Or let the script auto-detect playlist URLs
python youtube_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

#### Combined Options
```bash
# Download playlist to custom directory
python youtube_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist -o ~/Downloads/MyPlaylist
```

### Interactive Mode

If you run the script without arguments, it will start in interactive mode:

```bash
python youtube_downloader.py
```

The interactive mode will prompt you for:
- YouTube URL (video or playlist)
- Output directory (optional, defaults to current directory)
- Whether it's a playlist (y/n)

### Simple Download Script

For basic usage, you can also use the simplified version:

```bash
python simple_download.py
```

This script provides a minimal interface - just enter the YouTube URL when prompted.

## Command Line Arguments

| Argument | Short | Description | Example |
|----------|-------|-------------|---------|
| `url` | - | YouTube video or playlist URL | `"https://www.youtube.com/watch?v=dQw4w9WgXcQ"` |
| `--output` | `-o` | Output directory (default: current directory) | `-o ~/Downloads` |
| `--filename` | `-f` | Custom filename without extension | `-f "my_video"` |
| `--playlist` | - | Download entire playlist | `--playlist` |
| `--help` | `-h` | Show help message | `--help` |

## Examples

### Example 1: Single Video Download
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Example 2: Download with Custom Settings
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o ~/Videos -f "never_gonna_give_you_up"
```

### Example 3: Playlist Download
```bash
python youtube_downloader.py "https://www.youtube.com/playlist?list=PLrTrGOxObBMaUJYWfqCUMxWQp7xbYzaij" --playlist -o ~/Music
```

### Example 4: Using Interactive Mode
```bash
$ python youtube_downloader.py
🎥 YouTube Video Downloader
========================================
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter output directory (press Enter for current): ~/Downloads
Is this a playlist? (y/n): n
```

## Output Information

The downloader provides detailed information during the download process:

- 📹 Video title and details
- ⏱️ Video duration
- 🎬 Resolution information
- 📊 Quality details
- ⏬ Real-time progress (percentage, speed, ETA)
- 📁 Output directory path

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'yt_dlp'**
   - Make sure you've activated your virtual environment
   - Install dependencies: `pip install -r requirements.txt`

2. **Permission errors when downloading**
   - Make sure you have write permissions to the output directory
   - Try using a different output directory: `-o ~/Downloads`

3. **Invalid URL error**
   - Ensure the URL is a valid YouTube URL (contains 'youtube.com' or 'youtu.be')
   - Check that the video/playlist is publicly accessible

4. **Download errors**
   - The video might be region-blocked or private
   - Try updating yt-dlp: `pip install --upgrade yt-dlp`

### Getting Help

Use the help command to see all available options:
```bash
python youtube_downloader.py --help
```

## License

This project is open source and available under standard terms for educational and personal use.

## Contributing

Feel free to contribute improvements, bug fixes, or new features to this project.