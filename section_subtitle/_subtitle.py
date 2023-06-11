import sys
import re
from pathlib import Path
from _files_location import SUBTITLE_FILE_PATH


filename = ''
try:
    if sys.argv[2]:
        filename = ' '.join(sys.argv[1:])
except IndexError:
    try:
        filename = sys.argv[1]
    except IndexError:
        print(
            "You've forgotten to provide filename as an argument when running the program.")


def does_file_exist():
    """Check if a file exists based on a given extension."""
    global file_path
    file_path = f'{SUBTITLE_FILE_PATH}/{filename}'
    return Path(file_path).exists()


def init():
    write_to_file()
    remove_extra_space()


def is_valid_line(line):
    """If line is start with timestamp number and timestamp it is not valid line e.g. 1 or e.g. 00:00:00,000"""
    return not re.match(r'^(\d{2}:\d{2}:\d{2},\d{3}).+|^\d+$', line)


def write_to_file():
    with open(file_path, mode='r', encoding='UTF-8') as file:
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
if does_file_exist():
    init()
else:
    print(f"Oops! {filename} not found\nYou've either provided file name with extension or misspelled the file name or the path is incorrect.")
