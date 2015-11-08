#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
from string import Template
import codecs
from pygments import highlight
from pygments.lexers import PythonLexer

from pygments.formatters import HtmlFormatter

Example = namedtuple('Example', ['title', 'name', 'comments', 'code', 'challenge'], verbose=False)

example_template = Template("""

        <h2 id="$name "> $title </h2>

            <p><img src="img/${name}.png" alt="" /></p>

            <button class="$name "> Solution </button>

            <pre class="code $name "><code> $code </code></pre>

            <hr/>
""")

jquery_template = """

$("pre.{name} ").hide();
$("button.{name} ").click(function(){{ $("pre.{name} ").show();  }});

"""


class Examples(object):

    def __init__(self):
        self.examples = []

    def add(self, title, name, comments, code, challenge):
        self.examples.append(Example(title, name, comments, code, challenge))

    def __iter__(self):
        for example in self.examples:
            yield self.compose_html(example), self.compose_jquery(example)

    def compose_html(self, example):
        code = self.get_code(example.name)
        html = example_template.substitute(
            name=example.name,
            title=example.title,
            comments=example.comments,
            code=self.create_code(example.name),
            challenge=example.challenge
            )
        return html

    def get_code(self, name):
        fn = 'compy/templates/code/{}.html'.format(name)
        f = codecs.open(fn, 'r', 'utf-8')
        code_html = f.read()
        f.close()
        return code_html

    def compose_jquery(self, example):
        jq = jquery_template.format(name=example.name)
        return jq

    def create_code(self, name):
        fn = '{}.py'.format(name)

        f = codecs.open(fn, 'r', 'utf-8')
        code = f.read()
        f.close()

        code_html = highlight(code, PythonLexer(), HtmlFormatter())

        return code_html