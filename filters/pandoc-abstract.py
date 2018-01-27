#!/usr/bin/env python3

"""
Add abstract to pdf files.
"""

__author__ = "Benjamin Grange"

import copy

import panflute as pf

abstract = pf.MetaList()
in_abstract = False

def code_filter(elem, doc):
    global abstract
    global in_abstract

    if isinstance(elem, pf.Header):
        in_abstract = False
        if elem.identifier == "abstract":
            nodes = elem.parent.content
            within = False
            for n in iter(nodes):
                if isinstance(n, pf.Header) and n.identifier == "abstract":
                    within = True
                    continue
                if isinstance(n, pf.Header) and n.identifier == "endabstract":
                    break
                if within:
                    abstract.content.append(pf.MetaBlocks(copy.deepcopy(n)))
            in_abstract = True
            return []
        if elem.identifier == "endabstract":
            doc.metadata['abstract'] = abstract
            return []
    if in_abstract:
        return []

def main():
    pf.toJSONFilter(code_filter)

if __name__ == '__main__':
    main()
