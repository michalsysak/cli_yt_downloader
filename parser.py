import re
import os

class Parser:
    def __init__(self,link):
        self.link = link
        self.is_valid = self.valid_link(link)
        self.source = self.define_source(link)

    def valid_link(self,link):
        if re.search(r"^(https?)*://(www\.)",link):
            return True
        else:
            return False

    def define_source(self,link):
        if  re.search(r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$",link):
            return "youtube"
        else:
            return None



    def split_filename(self, name):
        name, format = os.path.splitext(name)
        return name, format[1:]


    def valid_resolution(self, res):
        #supported resolutions for downloader
        if res.strip() in ["240p","360p","480p","720p","1080p","1440p","2160p","4320p"]:
            return True
        else:
            return False
