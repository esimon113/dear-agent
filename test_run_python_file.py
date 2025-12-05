from functions.run_python_file import run_python_file


def main():
    test_params = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
        ("calculator", "lorem.txt")
    ]

    for params in test_params:
        f = "current" if params[1] == "." else f"'{params[1]}'"
        result = f"Result for {f}:\n{run_python_file(*params)}"
        print(result)


if __name__ == "__main__":
    main()
