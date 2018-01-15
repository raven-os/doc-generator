#!/usr/bin/env python3

"""
Python script to generate a pdf file from markdown.
"""

__author__ = "Benjamin Grange"

import argparse
import subprocess
import shutil
import sys
import os
import urllib.request
import random
import string

TMP_DIR='/tmp/doc-generator/'

class Build(object):
    def __init__(self, args):
        self.args = args

        if not os.path.exists(TMP_DIR):
            os.makedirs(TMP_DIR)

        self.path = None
        if self.args.url:
            self.path = gen_randpath()
            try:
                urllib.request.urlretrieve(self.args.url, self.path)
            except:
                print("Can't download \"" + self.args.url + "\". URL is probably wrong.", file=sys.stderr)
                sys.exit(1)
        else:
            self.path = self.args.file

        if self.path is None:
            print("You must specify either --file or --url.", file=sys.stderr)
            sys.exit(1)

    def run(self):
        cmd = [
            'pandoc',
            self.path,
            '-o',
            self.args.output,
            '--from=markdown',
            '--template=template/template.latex',
            '--filter=filters/pandoc-graphviz.py',
            '--filter=filters/pandoc-code.py',
            '--listings',
        ]
        self.exec_cmd(cmd)
        shutil.rmtree(TMP_DIR)

    def exec_cmd(self, cmd):
        if self.args.verbose:
            print("Command:", ' '.join(cmd))
        pipes = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out, std_err = pipes.communicate()

        if self.args.verbose or pipes.returncode != 0:
            sys.stdout.buffer.write(std_out)
            sys.stdout.buffer.write(std_err)

        if pipes.returncode != 0:
            print("An error occured while executing " + cmd[0] + ". Aborting", file=sys.stderr)
            sys.exit(1)

def gen_randpath():
    return TMP_DIR + ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.md'

def parse_args():
    """
    Parses the command line arguments.
    """
    parser = argparse.ArgumentParser(description='Build PDF documentation')
    parser.add_argument('output', help='Path to output')
    parser.add_argument('-f', '--file', help='Markdown file')
    parser.add_argument('-u', '--url', help='URL to markdown file')
    parser.add_argument('-v', '--verbose', help='Enable verbosity', action='store_true', default=False)
    return parser.parse_args()
    pass

def main():
    args = parse_args()
    Build(args).run()

if __name__ == '__main__':
    main()
