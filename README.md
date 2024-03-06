# cli_yt_downloader
CLI YouTube downloader in python

#Summary:
The program utilizes command-line arguments to receive inputs such as the name of the file, format, resolution, and type of the media file to be downloaded. It supports downloading from YouTube links and can handle various download options based on the provided arguments.

Key components of the program include:

Parser: Parses the input link to determine its validity and source.
Downloader: Handles the download process based on the parsed input and provided arguments.
Download_from_yt: A subclass of Downloader specifically for downloading from YouTube.

#Documentation:
How to Use:
Execute the script with appropriate command-line arguments.
Provide a valid YouTube link when prompted.
Optionally provide additional arguments such as file name, format, resolution, and type.

Command-line Arguments:
-n: Specifies the name of the file (optional).
-f: Specifies the format of the file, overwriting the format declared by the -n parameter (optional).
-r: Specifies the resolution of the video (optional).
-t: Specifies the type of the file (optional).
-help: Displays avaliable command-line arguments with a brief description (optional).

Supported Formats:
The program supports downloading media files in the following formats (if available):

Video: mp4, mov, mpeg4, avi 
Audio: mp4, webm
Supported Resolutions: 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, and 4320p.

#Example Usage:

python program.py -n my_video -f mp4 -r 720p -t video
Gimme link: [YOUR_URL]

Notes:
Ensure you have the necessary dependencies installed (included in requirements.txt) .
The program provides progress bars during the download process.
Limitations:
Currently it doesn't work with outher sources than YouTube.
Error handling is limited and may not cover all possible edge cases.

