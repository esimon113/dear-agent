import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        wd = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(wd, file_path))

        if os.path.commonpath([wd, path]) != wd:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        args.insert(0, path)
        args.insert(0, "python3")
        print(" | ".join(args))
        result = subprocess.run(args=args, timeout=30, capture_output=True)

        s = ""
        if len(result.stdout) + len(result.stderr) == 0:
            s = "No output produced\n"
        else:
            s = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n"

        return s + f"Process exited with code {result.returncode}" if result.returncode != 0 else ""

    except Exception as e:
        return f"Error: executing Python file: {e}"
