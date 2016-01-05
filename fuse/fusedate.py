#!/usr/bin/env python
'''Simplest custom FS hierarchy with a file(date) within a root
directory(fuse-test/)
'''
import datetime

from fuse import FUSE, Operations, LoggingMixIn
from stat import S_IFDIR, S_IFREG
from sys import argv
from time import time


class Context(LoggingMixIn, Operations):
    '''Basically we need three actions
    1. getattr - Get/Set file and directory attributes
    2. read - Returns a date string when file(date) is read
    3. readdir - a directory structure
    .. rest all are set to None

    Current system time is set as create-time, modified-time and
    access-time
    '''
    def getattr(self, path, fh=None):
        if path == '/':
            attr = dict(st_mode=(S_IFDIR | int('0750', 8)), st_nlink=2)
        elif path == '/date':
            attr = dict(st_mode=(S_IFREG | int('0755', 8)), st_size=30)

        attr['st_ctime'] = attr['st_mtime'] = attr['st_atime'] = time()
        return attr

    def read(self, path, size, offset, fh):
        if path == '/date':
            return datetime.datetime.now().strftime('%B %d, %Y') + '\n'

    def readdir(self, path, fh):
        return ['.', '..', 'date']

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

    PY_FUSE = FUSE(Context(), argv[1], foreground=True, ro=True)
