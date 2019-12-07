from os import listdir
from os import getcwd
from os import rename
from os.path import isfile, join
import sys


def pdf_or_txt(f_name):
    extensions_list = ['.pdf', '.txt', '.png', '.jpg']
    extension = f_name[-4:]

    if extension in extensions_list:
        return True
    else:
        return False


if __name__ == '__main__':
    header = ''
    if len(sys.argv) > 1:
        if sys.argv[1] == '-n':
            header = sys.argv[2] + '-'
        else:
            print("Usage: -n HEADER_NAME")
            sys.exit(0)

    files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
    necessary_files = sorted(filter(pdf_or_txt, files))

    for i in range(len(necessary_files)):
        ext = necessary_files[i][-4:]
        rename(necessary_files[i], f'{header}{i + 1}{ext}')

    print("DONE!:")
