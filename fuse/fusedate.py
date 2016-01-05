#!/usr/bin/env python

import datetime

from fuse import FUSE, Operations, LoggingMixIn
from stat import S_IFDIR, S_IFREG
from sys import argv, exit
from time import time


class Context(LoggingMixIn, Operations):
    def getattr(self, path, fh=None):
        pass

    def read(self, path, size, offset, fh):
        pass

    def readdir(self, path, fh):
        pass

    access = None
    flush = None
    getxattr = None
    listxattr = None
    open = None
    opendir = None
    release = None
    releasedir = None
    statfs = None


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: {} <mountpoint>'.format(argv[0]))
        exit(1)
