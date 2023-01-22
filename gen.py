#!/bin/env python3

import json
from os import sys

def main():
    d = json.load(sys.stdin)
    sys.stdout.write(json2htmldoc(d))

def json2htmldoc(d):
    """
    json2htmldoc converts an object representing JSON data
    to an HTML document.
    """
    return ("""\
<!DOCTYPE html>
<html lang="en">
<head>
	<title>jason - JSON viewer</title>
	<meta charset="utf-8" />
	<link rel="stylesheet" href="css/main.css" />
</head>
<body>
	<section id="json-viewer">""" + json2html("", d, True) + """\
</section>
</body>
</html>
""")

def json2html(k, v, omit_key):
    """
    json2html takes a key k and value v and returns an HTML node,
    omitting the key from the output if omit_key is True.
    """
    assert type(k) == str
    assert type(omit_key) == bool
    k = to_escaped_html(k) + ": "
    if omit_key:
        k = ""
    if v and type(v) in TYPES and (type(v) != str or len(v) >= 80):
        class_name, lbrace, rbrace, v2html = TYPES[type(v)]
        return (
            "<details class=\"%s\" open=\"open\">" % (class_name) +
            "<summary>%s%s</summary>" % (k, lbrace) +
            v2html(v) +
            "</details>%s" % (rbrace))
    return k + to_escaped_html(v)

def to_escaped_html(v):
    """
    to_escaped_html converts a value v to json
    then calls escape_html on it and returns it.
    """
    return escape_html(json.dumps(v, ensure_ascii=False))

def escape_html(s):
    """
    escape_html escapes HTML special characters in s and returns it.
    """
    assert type(s) == str
    return (s
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;"))

def dict2html(v):
    """
    dict2html converts dict v to an HTML element and returns it.
    """
    assert type(v) == dict
    return (
        "<ul><li>" +
        ",</li><li>".join(json2html(k, v, False) for k, v in v.items()) +
        "</li></ul>")

def list2html(v):
    """
    list2html converts list v to an HTML element and returns it.
    """
    assert type(v) == list
    return (
        "<ol><li>" +
        ",</li><li>".join(json2html("", v, True) for v in v) +
        "</li></ol>")

def str2html(v):
    """
    str2html converts str v to an HTML element and returns it.
    """
    assert type(v) == str
    return "<div>" + to_escaped_html(v)[1:-1] + "</div>"

TYPES = {
    dict: ("obj", "{", "}", dict2html),
    list: ("arr", "[", "]", list2html),
    str: ("str", "\"", "\"", str2html),
}

if __name__ == "__main__":
    main()

