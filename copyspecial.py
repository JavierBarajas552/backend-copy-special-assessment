#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Javier Barajas"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    results = []
    for filenames in os.listdir(dirname):
        if re.search(r'__\w+__', filenames):
            results.append(os.path.abspath(filenames))
    return results


def copy_to(path_list, dest_dir):
    """"Given a list of files and a destination dir will copy all files to dir"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for paths in path_list:
        shutil.copy(paths, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """Given a list of files and a destination to make a zip will copy files and zip them"""
    print("Command I'm going to do:")
    command = 'zip -j ' + dest_zip + ' ' + ' '.join(path_list)
    print(command)
    subprocess.run(['zip', '-j', dest_zip, *path_list])
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='source dir for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    # print(os.path.abspath(ns[0]))
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions

    path_list = get_special_paths(ns.from_dir)
    if ns.todir != None:
        copy_to(path_list, ns.todir)
    elif ns.tozip != None:
        zip_to(path_list, ns.tozip)
    else:
        for path in path_list:
            print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
