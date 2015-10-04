#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import markdown2


def make_html_challenges():

    f = codecs.open('docs/challenges.md', 'r', 'utf-8')
    mdtext = f.read()
    f.close()

    html_text = markdown2.markdown(mdtext)
    f = codecs.open('docs/challenges.html', 'w', 'utf-8')
    f.write(html_text)
    f.close()