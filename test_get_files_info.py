from functions.get_files_info import get_files_info


def main():
    test_params = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../")
    ]

    for params in test_params:
        dir = "current" if params[-1] == "." else f"'{params[-1]}'"
        result = f"Result for {dir} directory:\n{get_files_info(*params)}"
        print(result)


if __name__ == "__main__":
    main()
