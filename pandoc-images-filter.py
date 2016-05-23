#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pandoc filter to deal with image and links

1. ![](/images/xxx.png) => ![](/absoulute/path/to/iamges/xxx.png)
2. [Link](/xxxx.html)   => [Link](http://seisman.info/xxxx.html)

Usage:
    pandoc -t json post.md | ./markdown-filter.py | pandoc -f json -t markdown
"""

import os
import sys
from pandocfilters import toJSONFilter, Image

cdn = "http://7j1zxm.com1.z0.glb.clouddn.com"


def filters(key, value, format, meta):
    if key == "Image":
        value[2][0] = cdn + value[2][0]


if __name__ == "__main__":
    toJSONFilter(filters)
