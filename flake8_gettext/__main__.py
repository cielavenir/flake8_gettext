# Simple checker runner
# Note that this does not handle noqa.

from .checker import GettextChecker as Checker

from ast import parse
from sys import argv
from os import walk
from os.path import join
from os.path import isdir
from os.path import isfile

def runfile(fileName):
    with open(fileName) as f:
        try:
            tree = parse(f.read())
        except SyntaxError as e:
            # SyntaxError is out of this __main__.py scope, but we should show it anyway
            print('%s:%d:%d: E999 %s: %s' % (fileName, e.lineno, e.offset, type(e).__name__, e.msg))
        else:
            for row, col, err, typ in Checker(tree).run():
                print('%s:%d:%d: %s' % (fileName, row, col, err))

if __name__ == '__main__':
    for arg in argv[1:]:
        if isfile(arg):
            runfile(arg)
        elif isdir(arg):
            for dirpath, dirnames, filenames in walk(arg):
                for filename in filenames:
                    if filename.endswith('.py'):
                        runfile(join(dirpath, filename))
