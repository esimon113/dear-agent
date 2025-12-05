from functions.get_file_content import get_file_content


def main():
    test_params = [
        ("calculator", "lorem.txt"),
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py")
    ]

    for params in test_params:
        dir = "current" if params[-1] == "." else f"'{params[-1]}'"
        result = f"Result for {dir} directory:\n{get_file_content(*params)}"
        print(result)


if __name__ == "__main__":
    main()
