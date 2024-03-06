import pytest
from unittest.mock import patch
from io import StringIO
import sys

from downloader import Downloader, Download_from_yt
from parser import Parser

def main():
    test_downloader()
    test_parser()


def test_downloader():
    ...

def test_parser():
    test_parser_valid_link()
    test_parser_invalid_link()
    test_parser_define_source_youtube()
    test_parser_define_source_none()
    test_parser_split_filename()
    test_parser_valid_resolution_true()
    test_parser_valid_resolution_false()

def test_parser_valid_link():
    parser = Parser("https://www.youtube.com/watch?v=YbJOTdZBX1g")
    assert parser.is_valid == True


def test_parser_invalid_link():
    parser = Parser("invalid_link")
    assert parser.is_valid == False

def test_parser_define_source_youtube():
    parser = Parser("https://www.youtube.com/watch?v=YbJOTdZBX1g")
    assert parser.source == "youtube"


def test_parser_define_source_none():
    parser = Parser("https://www.example.com")
    assert parser.source == None


def test_parser_split_filename():
    parser = Parser("https://www.youtube.com/watch?v=YbJOTdZBX1g")
    name, format_ = parser.split_filename("example.mp4")
    assert name == "example"
    assert format_ == "mp4"


def test_parser_valid_resolution_true():
    parser = Parser("https://www.youtube.com/watch?v=YbJOTdZBX1g")
    assert parser.valid_resolution("720p") == True

def test_parser_valid_resolution_false():
    parser = Parser("https://www.youtube.com/watch?v=YbJOTdZBX1g")
    assert parser.valid_resolution("499p") == False



if __name__ == "__main__":
    main()
