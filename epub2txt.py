import glob, os, time
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# there may be more elements you don't want, such as "style", etc.
blacklist = ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script']

def write_txt(contents, filename):
    with open(filename + ".txt", 'w') as file_obj:
        for line in contents:
            if line != '\n':
                file_obj.write(line + '\n\n')

def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext

if __name__ == '__main__':
    start_time = time.time()
    for infile in glob.glob("/Users/Daglas/Desktop/*.epub"):
        filename, ext = os.path.splitext(infile)
        epub_path = filename + '.epub'
        contents = epub2text(epub_path)
        write_txt(contents, filename)
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')