# -*- coding: utf-8 -*-

import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, 'r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, 'w') as f:
        f.writelines(['%s\n' % line for line in ls] )

def get_filename(path):
    return os.path.basename(path)

def get_basename(path):
    return os.path.splitext(get_filename(path))[0]

def get_extension(path):
    return os.path.splitext(get_filename(path))[1]

def dp(msg):
    if args.debug:
        print msg

def abort(msg):
    print 'Error: {:}'.format(msg)
    os.system('pause')
    exit(1)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--input', default=None, required=True,
        help='A input filename.')

    parser.add_argument('--debug', default=False, action='store_true',
        help='Debug mode. (Show information to debug.)')

    args = parser.parse_args()
    return args

args = parse_arguments()

MYDIR = os.path.abspath(os.path.dirname(__file__))
infile = args.input
if get_extension(infile)!='.lisna':
    abort('Not lista file "{:}".'.format(infile))

lines = file2list(infile)

logfile = os.path.join(MYDIR, 'lisna.log')
if not(os.path.exists(logfile)):
    # new file if does not exists.
    list2file(logfile, [])
loglines = file2list(logfile)

try:
    outfile = infile
    lines.sort()
    list2file(outfile, lines)
    exit(0)
except Exception as e:
    errmsg = 'Type:{:} Detail:{:}'.format(str(type(e)), str(e))
    creationdate = datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')
    logmsg = '{:} {:}'.format(creationdate, errmsg)
    loglines.insert(0, logmsg)
    list2file(logfile, loglines)
    # open logfile with system association.
    os.system('start "" "{:}"'.format(logfile))
    exit(1)
