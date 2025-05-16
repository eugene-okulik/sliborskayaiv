import argparse
import os


def log_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path", help="Enter path to logs folder")
    parser.add_argument("--text", help="Enter what to search")
    args = parser.parse_args()

    if not args.text:
        print("No text provided for search.")
        return

    for filename in os.listdir(args.folder_path):
        if filename:
            file_path = os.path.join(args.folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for i, line in enumerate(file, start=1):
                        words = line.strip().split()
                        file_name = os.path.basename(file_path).split('\\')[-1]
                        if args.text in line:
                            for position, word in enumerate(words):
                                if args.text in word:
                                    start = max(position - 5, 0)
                                    end = position + 6
                                    context = words[start:end]
                                    print(f"File {file_name}. Line {i}: {' '.join(context)}")
            except FileNotFoundError:
                print("No such file")


if __name__ == "__main__":
    log_parser()
