import glob, os, time
from pathlib import Path
import ebooklib
from ebooklib import epub
from weasyprint import HTML
from bs4 import BeautifulSoup

# there may be more elements you don't want, such as "style", etc.
blacklist = ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script']



def write_txt(contents, filename):
    with open(filename + ".txt", 'w') as file_obj:
        file_obj.write(contents)


def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output


def thtml2text(thtml):
    Output = ''
    for html in thtml:
        text =  chap2text(html)
        Output = Output + text
    return Output

def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output




def makepdf(html):
    """Generate a PDF file from a string of HTML."""
    htmldoc = HTML(string=html, base_url="")
    return htmldoc.write_pdf()

def epub2html(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

def epub2pdf(epub_path, filename):
    chapters = epub2html(epub_path)
    html = thtml2ttext(chapters)
    pdf = makepdf(html[1])
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