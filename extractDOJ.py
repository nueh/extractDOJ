#!/usr/bin/env python
# encoding: utf-8

'''
extractDOJ.py
Created by Niklas Hennigs on 2011-05-08.
'''

import sys
import os
import locale
import time
import argparse
import plistlib

from operator import itemgetter

entries = []

locale.setlocale(locale.LC_ALL, "")

def extractPlainText(arg, path, file_list):
    global entries

    for file_name in file_list:
        # We need the full path to locate the file
        file_path = os.path.join(path, file_name)

        pl = plistlib.readPlist(file_path)

        EntryDate = pl["Creation Date"]
        EntryText = pl["Entry Text"]

        entries.append([EntryDate, EntryText])

def main():
    global entries

    parser = argparse.ArgumentParser(description=
                                     'Extracts plain text from '
                                     'your Day One journal '
                                     '(http://dayoneapp.com/).'
                                    )

    parser.add_argument('journal_bundle',
                        metavar='/Path/to/Journal.dayone',
                        help='Your journal file (bundle, actually)')
    parser.add_argument('outfile',
                        nargs='?',
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='save output to file OUTFILE')
    parser.add_argument('-d',
                        dest='date_format',
                        default='%A, %x, %H:%M',
                        help='format of date (google \'strftime python\')')
    parser.add_argument('-c',
                        '--csv',
                        action="store_true",
                        dest='csv',
                        help='output CSV (tab separated values)')
    parser.add_argument('-r',
                        action="store_true",
                        dest='reversed',
                        help='reversed order')

    args = parser.parse_args()

    dateformat = args.date_format

    if not os.path.exists(args.journal_bundle):
        sys.stderr.write("ERROR: Journal %r was not"
                         "found!\n" % (args.journal_bundle))
        sys.exit(1)

    entrydir = os.path.join(args.journal_bundle, "entries")

    os.path.walk(entrydir, extractPlainText, None)

    for entry in sorted(entries, key=itemgetter(0), reverse=(args.reversed)):
        if args.csv == True:
            args.outfile.write("\"" + entry[0].strftime(dateformat) +
                                "\"\t\"" + entry[1].encode("utf-8") + "\"\n")
        else:
            args.outfile.write(entry[0].strftime(dateformat) + "\n" +
                                entry[1].encode("utf-8") + "\n")

if __name__ == "__main__":
    main()
