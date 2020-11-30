import glob, os, time
from pathlib import Path
import ebooklib
from ebooklib import epub
from weasyprint import HTML

def makepdf(html):
    """Generate a PDF file from a string of HTML."""
    htmldoc = HTML(string=html, base_url="")
    return htmldoc.write_pdf()

def epub2html(epub_path):
    book = epub.read_epub(epub_path)
    chapters = ''
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters = chapters + item.get_content().decode("utf-8")
    return chapters

def epub2pdf(epub_path, filename):
    chapters = epub2html(epub_path)
    pdf = makepdf(chapters)
    Path(filename + '.pdf').write_bytes(pdf)

if __name__ == '__main__':
    start_time = time.time()
    for infile in glob.glob("/Users/Daglas/Desktop/*.epub"):
        filename, ext = os.path.splitext(infile)
        epub_path = filename + '.epub'
        epub2pdf(epub_path, filename)
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')