#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if len(sys.argv) < 2 :
    print 'Usage: ', sys.argv[0], '\n'
