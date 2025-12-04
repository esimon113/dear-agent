import os


def get_files_info(working_directory, directory="."):
    result = ""

    try:
        wd = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(wd, directory))

        if not os.path.isdir(path):
            return f'Error: "{directory}" is not a directory'

        if os.path.commonpath([wd, path]) != wd:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        files = os.listdir(path)
        for f in files:
            fn = os.path.join(path, f)
            result += "- " + f + ": file_size=" + \
                str(os.path.getsize(fn)) + \
                " bytes, is_dir=" + str(os.path.isdir(fn)) + "\n"
    except Exception as e:
        result = f"Error: {e}"
    return result
