#!/usr/bin/env python3

"""
Add graphviz as a Markdown extention.

Inspired by https://github.com/Lugdunum3D/Lugdunum-Tools/blob/master/generate-doc/pandoc-filters/pandoc-graphviz.py
"""

__author__ = "Benjamin Grange"

import panflute as pf

def code_filter(elem, doc):
    if isinstance(elem, pf.Code):
        return [pf.RawInline("\colorbox{colorbox-background}{\\texttt{", format='tex'), pf.Str(elem.text), pf.RawInline("}}", format='tex')]

def main():
    pf.toJSONFilter(code_filter)

if __name__ == '__main__':
    main()
