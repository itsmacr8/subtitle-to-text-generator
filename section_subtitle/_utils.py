import subprocess
from os import listdir, remove, getcwd
from os.path import isfile, join
from _files_location import SUBTITLE_FILE_PATH, OUTPUT_FILE_PATH, OUTPUT_FILE

FILEPATH = f'{OUTPUT_FILE_PATH}/{OUTPUT_FILE}'


def get_all_files_name(path):
    return [file for file in listdir(path) if isfile(join(path, file))]


def generate_text_file():
    """Run the subtitle.py script and generate the text files from srt files."""
    all_files = get_all_files_name(SUBTITLE_FILE_PATH)
    subtitles_files = [file for file in all_files if file.endswith(
        '.srt') or file.endswith('.vtt')]
    for filename in subtitles_files:
        subprocess.run(['python', 'subtitle.py', filename])


def format_output_file():
    with open(FILEPATH, mode='w', encoding='UTF-8') as file:
        file.write('')


def is_output_file(filename):
    return filename != OUTPUT_FILE


def write_to_file(content_heading, content):
    _5_line = '\n\n\n\n\n'
    with open(FILEPATH, mode='a', encoding='UTF-8') as file:
        file.write(f"{content_heading.replace('-',' ')}\n\n{content}{_5_line}")


def remove_extension(filename):
    """Removes the extension from the filename."""
    vtt = '.vtt.txt'
    srt = '.srt.txt'
    return filename.replace(vtt, '') if filename.endswith(vtt) else filename.replace(srt, '')


def open_files():
    all_files = get_all_files_name(getcwd())
    txt_files = [file for file in all_files if file.endswith('.txt')]
    for filename in txt_files:
        if is_output_file(filename):
            with open(filename, mode='r', encoding='UTF-8') as file:
                write_to_file(remove_extension(filename), file.read())


def remove_generated_text_file():
    all_files = get_all_files_name(getcwd())
    text_files = [file for file in all_files if file.endswith('.txt')]
    for filename in text_files:
        if is_output_file(filename):
            remove(filename)
