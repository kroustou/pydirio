#!/usr/bin/env python
from __future__ import unicode_literals
import time
import os
import sys
import argparse

command = "lessc screen.less screen.css"
parser = argparse.ArgumentParser(description='Gimme a directory')
parser.add_argument('dir', metavar='directory', type=str, help='a directory to watch')

args = parser.parse_args()
directory = args.dir
if os.path.exists(directory):
    last = os.stat(directory)[-1]
    while True:
        time.sleep(1)
        for root, dirs, files in os.walk(directory):
            if os.stat(root)[-1] > last:
                print 'file changed in %s' % (root)
                last = os.stat(root)[-1]
                os.system(command)
else:
    print 'directory "%s" not found!\nExiting...' % (directory)
    sys.exit()
