import os


def write_file(working_directory, file_path, content):
    try:
        wd = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(wd, file_path))

        if os.path.commonpath([wd, path]) != wd:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        with open(path, "w") as f:
            if f.write(content) > 0:
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
