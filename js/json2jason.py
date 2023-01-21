import json
from os import sys

def main():
    d = json.load(sys.stdin)
    sys.stdout.write(to_jason("", d, True))

def to_jason(k, v, omit_key):
    k = json.dumps(k) + ": "
    if omit_key:
        k = ""
    if v and type(v) in (dict, list):
        is_arr = type(v) == list
        lbrace = "[" if is_arr else "{"
        rbrace = "]" if is_arr else "}"
        list_tag = "ol" if is_arr else "ul"
        if is_arr:
            v = enumerate(v)
        else:
            v = v.items()
        return (
            "<details open=\"open\">" +
            "<summary>%s%s</summary>" % (k, lbrace) +
            "<%s>" % (list_tag) +
            "<li>" +
            ",</li><li>".join(to_jason(k, v, is_arr) for k, v in v) +
            "</li>" +
            "</%s>" % (list_tag) +
            "</details>%s" % (rbrace))
    return ((k + json.dumps(v))
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;"))

if __name__ == "__main__":
    main()

