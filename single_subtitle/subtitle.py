import sys
import re
from pathlib import Path


# print(sys.argv)   # shows a list of all the arguments passed to the program.
filename = ''
# If provided file name includes spaces(01 - Introduction to web), then use first try block
# else (01-Introduction-to-web/01_Introduction_to_web/01IntroductionToWeb) use second try block.
# When we pass argument with spaces sys.argv thinks them as individual argument.
try:
    if sys.argv[2]:
        filename = ' '.join(sys.argv[1:])
except IndexError:
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You've forgotten to provide filename as an argument when running the program.")


# NOTE: Use the below line if subtitle file in this current folder.
SUBTITLE_FILE_PATH = Path.cwd()

# NOTE: Use this line if subtitle file is elsewhere.
# add the absolute path. e.g. D:\Tutorials to D:/Tutorials
# SUBTITLE_FILE_PATH = Path('D:/Tutorials')


def does_file_exist(ext):
    """Check if a file exists based on a given extension."""
    global file_path, sub_filename
    sub_filename = f'{filename}.{ext}'
    file_path = f'{SUBTITLE_FILE_PATH}/{sub_filename}'
    return Path(file_path).exists()


def init():
    write_to_file()
    remove_extra_space()


def is_valid_line(line):
    """If line is start with timestamp number and timestamp it is not valid line e.g. 1 or e.g. 00:00:00,000"""
    return not re.match(r'^(\d{2}:\d{2}:\d{2},\d{3}).+|^\d+$', line)


def write_to_file():
    with open(file_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
    with open(f'{OUTPUT_FILE}', 'w', encoding='UTF-8') as write_file:
        sentence = [line.strip() for line in lines if is_valid_line(line)]
        write_file.write(' '.join(sentence))


def remove_extra_space():
    '''Opening the text file and removing extra white space'''
    try:
        with open(f'{OUTPUT_FILE}', 'r', encoding='UTF-8') as file:
            file_content = file.read().replace('  ', ' ')
    except FileNotFoundError:
        print(f'Oops! {OUTPUT_FILE} not found')
    else:
        with open(f'{OUTPUT_FILE}', 'w', encoding='UTF-8') as file:
            file.write(file_content)


OUTPUT_FILE = f'{filename}.txt'
if does_file_exist('vtt') or does_file_exist('srt'):
    init()
else:
    print(f'Oops! {sub_filename} not found')
    print("You've either provided filename with extension or misspelled the filename or the path is incorrect.")
