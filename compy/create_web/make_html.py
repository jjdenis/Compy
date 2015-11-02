#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('compy', 'templates'))

def make_html(name_html, **kwargs):

    template = env.get_template(name_html)

    md_text = template.render(**kwargs)

    final_path = 'docs/{}'.format(name_html)
    f = codecs.open(final_path, 'w', 'utf-8')
    f.write(md_text)
    f.close()