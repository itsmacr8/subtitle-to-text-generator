<h1 align="center">Generates text file from subtitle files.</h1>

## Generate a text file from a subtitle file

Use the subtitle file located in the "lecture subtitle" folder and execute the following command.

```shell
python subtitle.py <subtitle_filename>
# Do not include the subtitle file extension.
```

## Note from section subtitle files

Generate and copy text file content in a single file from a given directory of subtitle files

## Set subtile file and output file location

Set the subtitle files location and the output file location to the respective variables `(SUBTITLE_FILE_PATH and OUTPUT_FILE_PATH)` in the _files_location.py file.

## Note from course subtitle files

Generate and copy text file content in a single file with the name of the section folder from a course directory for every section of the course.

## Set course folder location

Set the course folder location to the respective variable `COURSE_DIR` in the main.py file.

## Run the script

```shell
python main.py
```
