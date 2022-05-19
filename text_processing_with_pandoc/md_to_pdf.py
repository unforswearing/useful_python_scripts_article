import pandoc
def md_to_pdf(md_file='.tmp.md', pdf_file='output.pdf'):
    """ Converts from Markdown to PDF. """
    pandoc(md_file, '-o', pdf_file)

md_to_pdf()
