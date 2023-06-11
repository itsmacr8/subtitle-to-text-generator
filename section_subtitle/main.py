import _utils


def init():
    _utils.generate_text_file()
    _utils.format_output_file()
    _utils.open_files()
    _utils.remove_generated_text_file()


init()
