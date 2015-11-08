#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from jinja2 import Environment, PackageLoader
from compy.settings import DOCS_PATH

env = Environment(loader=PackageLoader('compy', 'templates'))

def t2wp(name_html, **kwargs):

    template = env.get_template(name_html)

    md_text = template.render(**kwargs)

    final_path = DOCS_PATH + '{}'.format(name_html)
    f = codecs.open(final_path, 'w', 'utf-8')
    f.write(md_text)
    f.close()