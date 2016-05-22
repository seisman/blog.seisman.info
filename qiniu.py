#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import subprocess

# add qiniu keys here
access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
secret_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def run_qrsyn(data_dir, bucket, key_prefix):
    jsonfile = "qiniu-conf.json"

    data['src'] = os.path.join(os.getcwd(), data_dir)
    data['dest'] = '&'.join([keys, "bucket="+bucket, "key_prefix="+key_prefix])
    with open(jsonfile, 'w') as outfile:
        json.dump(data, outfile)
    subprocess.run(["qrsync", jsonfile])
    os.remove(jsonfile)


if __name__ == "__main__":
    data = {}
    data['debug_level'] = 1

    keys = "qiniu:"+"access_key="+access_key+"&"+"secret_key="+secret_key

    # PDFs and images
    os.chdir("source")
    subprocess.run('python makepdf.py _posts/*.md', shell=True)
    os.chdir("..")
    run_qrsyn("source/_pdfs", "seisman", "pdfs/")
    run_qrsyn("source/images", "seisman", "images/")

    # if not os.path.exists("public"):
    #     subprocess.run("hexo g")
    #     subprocess.run("gulp")
    #
    # # JS
    # run_qrsyn("public/js", "next-assets", "js/")
    # # CSS
    # run_qrsyn("public/css", "next-assets", "css/")
