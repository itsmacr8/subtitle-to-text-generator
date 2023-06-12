import subprocess
from os import listdir, remove, getcwd
from os.path import isfile, join, isdir


note_files_name = []


def get_all_folder_names(folder_path):
    folder_names = [file for file in listdir(folder_path) if isdir(join(folder_path, file))]
    return sort_by_number(folder_names)


def get_all_files_name(path):
    return [file for file in listdir(path) if isfile(join(path, file))]


def remove_extension(filename):
    """Removes the extension from the filename when writing in the main file"""
    vtt = '.vtt.txt'
    srt = '.srt.txt'
    return filename.replace(vtt, '') if filename.endswith(vtt) else filename.replace(srt, '')


def write_to_file(content_heading, content, filename):
    _5_line = '\n\n\n\n\n'
    with open(f'{getcwd()}/{filename}', mode='a', encoding='UTF-8') as file:
        file.write(f"{content_heading.replace('-',' ')}\n\n{content}{_5_line}")


def is_note_file(filename, output_file_name):
    if output_file_name not in note_files_name:
        note_files_name.append(output_file_name)
    return filename not in note_files_name


def generate_text_file(sub_file_path):
    """Run the subtitle.py script and generate text files from subtitle files."""
    subtitles_files = [file for file in get_all_files_name(sub_file_path) if file.endswith('.srt') or file.endswith('.vtt')]
    for filename in subtitles_files:
        subprocess.run(['python', 'subtitle.py', f'{sub_file_path}/{filename}'])


def format_output_file(filename):
    with open(f'{getcwd()}/{filename}', mode='w', encoding='UTF-8') as file:
        file.write('')


def open_files(output_file_name):
    """Read all the generated text file and write it to the main file."""
    for filename in get_all_text_files_sorted():
        if is_note_file(filename, output_file_name):
            with open(filename, mode='r', encoding='UTF-8') as file:
                write_to_file(remove_extension(filename), file.read(), output_file_name)


def remove_generated_text_file(output_file_name):
    for filename in get_all_text_files_sorted():
        if is_note_file(filename, output_file_name):
            remove(filename)


def extract_number(filename):
    """Extract the leading number from a filename string."""
    return int(filename.split('.')[0])

def sort_by_number(filenames):
    """
        *   Sort a list of filenames by their leading number.
        *   names = ['2.text', '5.text', '1.text']
        *   Output: ['1.text', '2.text', '5.text']
    """
    return sorted(filenames, key=extract_number)


def get_all_text_files_sorted():
    """Returns a list of text files from the current working directory."""
    return sort_by_number([file for file in get_all_files_name(getcwd()) if file.endswith('.txt')])
