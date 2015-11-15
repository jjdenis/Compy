#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
from string import Template
import codecs
import pygments
# from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from compy.settings import CODE_PATH

Example = namedtuple('Example', ['title', 'name', 'comments', 'challenge'], verbose=False)

example_template = Template("""

        <h2 id="$name "> $title </h2>

            <p> $comments </p>

            <p><img src="img/${name}.png" alt="" /></p>

            <button class="$name "> Solution </button>

            <div class="code $name "><code> $code </code></div>

            <hr/>
""")

jquery_template = """

$("div.{name} ").hide();
$("button.{name} ").click(function(){{ $("div.{name} ").toggle();  }});

"""


class Examples(object):

    def __init__(self):
        self.examples = []

    def new(self, title, name, comments, challenge):
        self.examples.append(Example(title, name, comments, challenge))

    def __iter__(self):
        for example in self.examples:
            yield self.compose_html(example), self.compose_jquery(example)

    def compose_html(self, example):
        code = self.get_code(example.name)
        code_html = self.code2html(code)
        html = example_template.substitute(
            name=example.name,
            title=example.title,
            comments=example.comments,
            code=code_html,
            )
        return html

    def get_code(self, name):
        fn = CODE_PATH+'{}.py'.format(name)

        f = codecs.open(fn, 'r', 'utf-8')
        code = f.read()
        f.close()
        return code

    def code2html(self, code):
        code_html = pygments.highlight(code, PythonLexer(), HtmlFormatter())
        return code_html

    def compose_jquery(self, example):
        jq = jquery_template.format(name=example.name)
        return jq

