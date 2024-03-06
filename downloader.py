import sys
from parser import Parser
from pytube import YouTube

class Downloader:
    def __init__(self, parser, args):
        self.parser = parser
        self.args = args
        self.source = parser.source


    #defining the download method
    def download_from_link(self):
        if self.source == "youtube":

            #print(self.args, type(self.args))
            youtube = Download_from_yt(self.parser, self.args)

            if self.args.n is None and self.args.f is None and self.args.r is None and self.args.t is None:
                youtube.download_0args()

            else:
                #for args given
                youtube.download_arg()



class Download_from_yt(Downloader):
    def __init__(self, parser, args):
        super().__init__(parser, args)

        if not self.source:
            sys.exit("Download not supported")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        per = str((int(percentage_of_completion)))
        bar = "░" * int(per) + "-" * (100 - int(per))
        print(f"|{bar}| {per}%",end="\r")


    def download_0args(self):
        try:
            self.yt = YouTube(self.parser.link,on_progress_callback=self.on_progress)
            self.video = self.yt.streams.get_highest_resolution()
            self.video.download()
            print("Download finished!")

        except Exception as e:
            print(f"Error: {e}")
            sys.exit("Download failed")


    def download_arg(self, name_=None, format_=None, resolution_=None, type_="video"):
        self.supported_formats = ["mov","mpeg4","mp4","avi"]


        if self.args.t is not None:
            type_=self.args.t

        if type_ == "video":

            if self.args.n is not None:
                name_, format_ = self.parser.split_filename(self.args.n)

                if format_ == None or format_.strip() == "":
                    format_ = "mp4"

                if not format_.strip() in self.supported_formats:
                    sys.exit("Not supported format")


            if self.args.f is not None:
                if not format_.strip() in self.supported_formats:
                    sys.exit("Not supported format")
                format_=self.args.f

            if self.args.r is not None:
                if self.parser.valid_resolution(self.args.r):
                    resolution_= self.args.r
                else:
                    sys.exit("Invalid resolution")



        if type_ == "audio":
            self.supported_formats = ["mp4","webm"]

            if self.args.n is not None:
                name_, format_ = self.parser.split_filename(self.args.n)

                if format_ == None or format_.strip() == "":
                    format_ = "mp4"

                if not format_.strip() in self.supported_formats:
                    sys.exit("Not supported format")

            if self.args.f is not None:
                if not format_.strip() in self.supported_formats:
                    sys.exit("Not supported format")
                format_=self.args.f


        try:
            #Downloading the file
            self.yt = YouTube(self.parser.link, on_progress_callback=self.on_progress)
            stream = self.yt.streams.filter(res=resolution_, mime_type=f"{type_}/{format_}").first()

            if stream is None:
                sys.exit("No sources found")



            stream.download(filename=f"{name_}.{format_}")


            print("\nDownload finished! ")
        except AttributeError:
            sys.exit("Query not find ")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit("Download failed! ")
