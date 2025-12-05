from functions.file_handler import write_file


def main():
    test_params = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed"),
    ]

    for params in test_params:
        f = "current" if params[1] == "." else f"'{params[1]}'"
        result = f"Result for {f}:\n{write_file(*params)}"
        print(result)


if __name__ == "__main__":
    main()
