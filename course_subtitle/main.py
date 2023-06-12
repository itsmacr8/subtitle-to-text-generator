import utils
from pathlib import Path

# NOTE: Use the following format for directory location.
# Change the absolute path. e.g. D:\Tutorials\Python to D:/Tutorials/Python
COURSE_DIR = Path('<PATH>')


def init():
    for folder_name in utils.get_all_folder_names(COURSE_DIR):
        output_file_name = f'{folder_name}.txt'
        sub_file_path = f'{COURSE_DIR}/{folder_name}'
        utils.generate_text_file(sub_file_path)
        utils.format_output_file(output_file_name)
        utils.open_files(output_file_name)
        utils.remove_generated_text_file(output_file_name)


init()
