import pandoc
md_string = """
# Hello from Markdown

**This is a markdown string**
"""
input_string = pandoc.read(md)
pandoc.write(input_string, format="json", file="md.json")
