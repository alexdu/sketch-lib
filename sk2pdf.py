#!/usr/bin/python

# Compiles a .sk file as soon as you save it in the text editor.

import sys, os

import time
import fcntl
import signal

def make():
    inp = sys.argv[1]
    tex = (inp[:-3] if inp.endswith('.sk') else inp) + '.tex'
    pdf = (inp[:-3] if inp.endswith('.sk') else inp) + '.pdf'

    s = os.system('sketch -T %s -o %s' % (inp, tex))
    if s: return

    s = os.system('pdflatex ' + tex)
    if s: return

    s = os.system('pdfcrop %s %s -margins "5 5 5 5"' % (pdf, pdf))
    if s: return

#    s = os.system('xdg-open ' + pdf)



def handler(signum, frame):
    print "File modified" 

if '-c' in sys.argv:
    inp = sys.argv[1]
    mtold = None
    while True:
        mt = os.stat(inp).st_mtime
        if mt != mtold:
            make()
            mtold = mt
        time.sleep(0.1)

else:
    make()
