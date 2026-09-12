import markdown
from xhtml2pdf import pisa

# read your markdown report
with open("Summary.md", "r", encoding="utf-8") as f:
    md_text = f.read()

# convert markdown to HTML
html = markdown.markdown(md_text)

# convert HTML to PDF
with open("module_summary.pdf", "wb") as f:
    pisa.CreatePDF(html, dest=f)

print("PDF created: module_summary.pdf")
