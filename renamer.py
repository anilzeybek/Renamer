import os
from os.path import isfile, join
import argparse

extensions_list = ['txt', 'png', 'jpg']
header = ''
skip = False
directory = ''


def extension_compatible(f_name):
    extension = f_name.split('.')[-1]

    if extension in extensions_list:
        return True
    else:
        return False


def parse_args():
    global header, skip, directory

    parser = argparse.ArgumentParser(description='Rename files in order')
    parser.add_argument('-n', '--name', type=str, help='Headers name for files to put before numbers')
    parser.add_argument('-e', '--extensions', type=str, help='Headers for files to put before numbers')
    parser.add_argument('-y', '--yes', action='store_const', const=True, help="Don't ask for inputting y")
    parser.add_argument('directory', type=str, help='Directory location of the files that will renamed')
    args = parser.parse_args()

    header = f'{args.name}-' if args.name else ''

    if args.extensions:
        mutate_extension_list(args.extensions)

    skip = args.yes if args.yes else False

    directory = args.directory


def mutate_extension_list(new_extensions: str):
    global extensions_list
    extensions_list = new_extensions.split()


def rename_files(files):
    for i in range(len(files)):
        ext = files[i].split('.')[-1]
        os.rename(files[i], f'{header}{i + 1}.{ext}')


def main():
    parse_args()

    if directory == '.':
        files = [f for f in os.listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    else:
        files = [f for f in os.listdir(directory) if isfile(join(os.getcwd(), f))]

    necessary_files = sorted(filter(extension_compatible, files))

    if skip:
        rename_files(necessary_files)
        print("DONE!")
    else:
        print('This will rename every file with extensions:')
        for i in range(len(extensions_list)):
            print(f'{i}- {extensions_list[i]}')

        print('Do you want to continue? y/n')
        selection = input()

        if selection == 'y':
            rename_files(necessary_files)
            print("DONE!")
        else:
            print('Cancelled')


if __name__ == '__main__':
    main()
