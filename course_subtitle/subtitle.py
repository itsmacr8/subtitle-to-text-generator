import re
from sys import argv
from os.path import basename, exists


sub_file = ''
try:
    if argv[2]:
        sub_file = ' '.join(argv[1:])
except IndexError:
    try:
        sub_file = argv[1]
    except IndexError:
        print("You've forgotten to provide subtitle filename as an argument when running the program.")


def does_file_exist():
    """Check if a file exists based on a given extension."""
    return exists(sub_file)


def is_valid_line(line):
    """If line is start with timestamp number and timestamp it is not valid line e.g. 1 or e.g. 00:00:00,000"""
    return not re.match(r'^(\d{2}:\d{2}:\d{2},\d{3}).+|^\d+$', line)


def write_to_file():
    with open(sub_file, mode='r', encoding='UTF-8') as file:
        lines = file.readlines()
    with open(GEN_TEXT_FILE, mode='w', encoding='UTF-8') as file:
        sentence = [line.strip() for line in lines if is_valid_line(line)]
        file.write(' '.join(sentence))


def remove_extra_space():
    '''Opening the text file and removing extra white space'''
    if not exists(GEN_TEXT_FILE):
        print(f'Oops! {GEN_TEXT_FILE} not found')
    else:
        with open(GEN_TEXT_FILE, mode='r', encoding='UTF-8') as file:
            file_content = file.read().replace('  ', ' ')
        with open(GEN_TEXT_FILE, mode='w', encoding='UTF-8') as file:
            file.write(file_content)


def init():
    write_to_file()
    remove_extra_space()


# This is the temporary text file generated from the subtitle file.
# Remove the "remove_generated_text_file" from main.py file if it is needed.
GEN_TEXT_FILE = f'{basename(sub_file)}.txt'
if does_file_exist():
    init()
else:
    print(f"Oops! {GEN_TEXT_FILE} not found\nYou've either provided file name with extension or misspelled the file name or the path is incorrect.")
