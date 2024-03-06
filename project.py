import sys
import argparse
from parser import Parser
from downloader import Downloader


def parse_arguments():
    #adding arguments using argsys
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="name of the file/can be used with .xyz format if supported")
    parser.add_argument("-f", help="format of the file/ it overwrites the format format declared by the -n parameter")
    parser.add_argument("-r", help="resolution the video/ eg. 360p , 720p... //default is the highest one")
    parser.add_argument("-t", help="type of the file/ eg. video, audio //default is video")
    return parser.parse_args()

def print_welcome_0args():
    print("Hello, i see you have no arguments :( but let me see what i can do ...")
def print_welcome_args():
    print("Hello, i see you have a lot of arguments :) im glad to help you download ...")




def main():
    args = parse_arguments()
    if args.n is None and args.f is None and args.r is None and args.t is None:
        print_welcome_0args()
    else:
        print_welcome_args()

    try:
        user_input = str(input("Gimme a link: ")).strip()
        parser = Parser(user_input)
        if parser.is_valid:
            downloader = Downloader(parser,args)
            downloader.download_from_link()

        else:
            raise ValueError

    except ValueError:
        sys.exit("Invalid link")


if __name__ == "__main__":
    main()
