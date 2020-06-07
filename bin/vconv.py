#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Vicentini Leonardo"
__version__ = "01_01"


import os
import sys
import argparse
import ntpath
import shutil


boold = False


def convert_file(file_path, output_folder):
    """
    Uses 'ffmpeg' to convert the mkv file to mp4.
    :param file_path: str Relative file path path.
    :param output_folder: str Relative directory path for the output.
    :return: None.
    """
    global verbose, quiet, is_test

    cwd = os.getcwd()

    if not quiet and not verbose: print(f"Converting: {file_path} ...")

    dir_path = os.path.dirname(os.path.abspath(file_path))
    os.chdir(dir_path)
    file_name = ".".join(ntpath.basename(file_path).split(".")[:-1])

    info = "" if verbose else "-loglevel quiet "
    is_test = "-t 30 " if is_test else ""

    os.system(f'ffmpeg {info}-i "{file_name}.mkv" {is_test}"{file_name}.mp4"')
    
    if not os.path.isdir(output_folder): os.mkdir(output_folder)

    try:
        if output_folder != ".": shutil.move(f"{file_name}.mp4", output_folder)
    except shutil.Error:
        print(f"File {file_name}.mp4 already exists")

    os.chdir(cwd)


if __name__ == "__main__":

    if boold: print("Start main")

    parser = argparse.ArgumentParser(description="Program to convert mkv into mp4.", prog="vconv")
    parser.add_argument("--version", help="show program version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", help="verbose output.", action="store_true")
    parser.add_argument("-q", "--quiet", help="quiet output.", action="store_true")
    parser.add_argument("-f", "--file", help="specify the mkv fil path.", type=str)
    parser.add_argument("-d", "--dir", help="specify the path of the directory with mkv files.", type=str)
    parser.add_argument("-o", "--out", help="specify the output folder.", type=str)
    parser.add_argument("-t", "--test", help="convert only 30 sec of the video.", action="store_true")

    args = parser.parse_args()

    verbose = args.verbose
    quiet = args.quiet
    is_test = args.test

    output_dir = args.out if args.out else "."

    if args.file:
        convert_file(args.file, output_dir) if os.path.isfile(args.file) else print("404 File not found. LOL :-)")

    elif args.dir:
        if os.path.isdir(args.dir):
            for file in os.listdir(args.dir):
                if file.endswith(".mkv"):
                    file_name = ".".join(file.split(".")[:-1])
                    convert_file(f"{args.dir}/{file_name}.mkv", output_dir)
        else:
            print("404 Dir not found. LOL :-)")
    
    else:
        parser.print_help()

    if boold: print("End main")
