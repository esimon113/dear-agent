import os

from config import MAX_FILE_SIZE


def get_file_content(working_directory, file_path):
    try:
        wd = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(wd, file_path))

        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        if os.path.commonpath([wd, path]) != wd:
            return f'Cannot read "{file_path}" as it is outside the permitted working directory'

        with open(path, "r") as f:
            file_content = f.read(MAX_FILE_SIZE)
            if os.path.getsize(path) > MAX_FILE_SIZE:
                file_content += f'[...File "{file_path}" truncated at {
                    MAX_FILE_SIZE} characters]'

        return file_content

    except Exception as e:
        return f"Error: {e}"
