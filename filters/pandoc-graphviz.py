#!/usr/bin/env python3

"""
Add graphviz as a Markdown extention.

Inspired by https://github.com/Lugdunum3D/Lugdunum-Tools/blob/master/generate-doc/pandoc-filters/pandoc-graphviz.py
"""

__author__ = "Benjamin Grange"

import panflute as pf
import pygraphviz
import random
import string
import sys

def gen_randstr():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def graphviz_filter(elem, doc):
    if isinstance(elem, pf.CodeBlock) and 'graphviz' in elem.classes:
        code = elem.text
        graph = pygraphviz.AGraph(string=code)
        title = graph.graph_attr.pop('label', '')
        graph.layout()
        path = '/tmp/doc-generator/' + gen_randstr() + '.pdf'
        graph.draw(path, prog='dot')
        para = pf.Para(pf.Image(pf.Str(title), title='fig:', url=path))
        return para

def main():
    pf.toJSONFilter(graphviz_filter)

if __name__ == '__main__':
    main()
