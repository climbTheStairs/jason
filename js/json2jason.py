import json
from os import sys

def main():
    d = json.load(sys.stdin)
    sys.stdout.write(to_jason("", d, True))

def to_jason(k, v, omit_key):
    """
    to_jason takes a key k and value v and returns an HTML node,
    omitting the key from the output if omit_key is True.
    """
    assert type(k) == str
    assert type(omit_key) == bool
    k = escape_html(json.dumps(k)) + ": "
    if omit_key:
        k = ""
    if v and type(v) in TYPES:
        lbrace, rbrace, v2html = TYPES[type(v)]
        return (
            "<details open=\"open\">" +
            "<summary>%s%s</summary>" % (k, lbrace) +
            v2html(v) +
            "</details>%s" % (rbrace))
    return k + escape_html(json.dumps(v))

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
        ",</li><li>".join(to_jason(k, v, False) for k, v in v.items()) +
        "</li></ul>")

def list2html(v):
    """
    list2html converts list v to an HTML element and returns it.
    """
    assert type(v) == list
    return (
        "<ol><li>" +
        ",</li><li>".join(to_jason("", v, True) for v in v) +
        "</li></ol>")

TYPES = {
    dict: ("{", "}", dict2html),
    list: ("[", "]", list2html),
}

if __name__ == "__main__":
    main()

