from exceptions import DataReaderError, FileEmptyError, InvalidFileError


def read_txt(file_path: str):
    """Reads a .TXT file safely with full exception handling."""

    if not file_path:
        raise ValueError("File path cannot be empty")

    if not file_path.endswith(".txt"):
        raise InvalidFileError("Only .txt files are supported")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            if not lines:
                raise FileEmptyError("File is empty")

            return [line.strip() for line in lines]

    except FileNotFoundError:
        raise DataReaderError("File not found")

    except PermissionError:
        raise DataReaderError("Permission denied")

    except UnicodeDecodeError:
        raise DataReaderError("Encoding issue while reading file")



def test_reader():
    '''
    Test function
    '''
    test_cases = [
        "",                 # Empty path
        "data.csv",         # Wrong format
        "missing.txt",      # File not found
        "empty.txt",        # Empty file
        "sample.txt"        # Valid file 
    ]

    for path in test_cases:
        print(f"\n Testing: {path}")

        try:
            result = read_txt(path)
            print("SUCCESS:", result)

        except InvalidFileError as e:
            print("InvalidFileError:", e)

        except FileEmptyError as e:
            print("FileEmptyError:", e)

        except DataReaderError as e:
            print("DataReaderError:", e)

        except Exception as e:
            print("Unhandled Exception:", e)


if __name__ == "__main__":
    test_reader()