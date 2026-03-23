import logging
import os

#Configuring logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s | %(message)s'
)

logger = logging.getLogger(__name__)


def parse_txt_file(file_path):
    logger.info(f"Reading file: {file_path}")

    # Basic validations
    if not file_path:
        logger.error("File path is empty")
        raise ValueError("File path cannot be empty")

    if not file_path.endswith(".txt"):
        logger.error("Invalid file type")
        raise ValueError("Only .txt files are allowed")

    if not os.path.exists(file_path):
        logger.error("File not found")
        raise FileNotFoundError("File does not exist")

    parsed_data = []

    with open(file_path, "r") as file:
        for i, line in enumerate(file, start=1):
            line = line.strip()

            logger.debug(f"Line {i}: {line}")

            if not line:
                continue

            parsed_data.append(line.split(","))

    logger.info("File parsed successfully")
    return parsed_data


#Test
if __name__ == "__main__":
    try:
        result = parse_txt_file("Logging and File Handling\sample.txt")
        print(result)
    except Exception as e:
        print("Error:", e)