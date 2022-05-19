import pandoc
def from_markdown(string):
    """
    Read a markdown text as a Pandoc instance.
    """
    json_str = str(sh.pandoc(read="markdown", write="json", _in=string))
    json_ = json.loads(json_str, object_pairs_hook=Map)
    return from_json(json_)

markdown_string = """
# Hello from Markdown

**This is a markdown formatted string**
"""

from_markdown(markdown_string)
