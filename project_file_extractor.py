import os
import argparse

def write_files_with_extensions_to_text(directory, extensions, output_file, ignore_file_substrings, ignore_folder_substrings):
    with open(output_file, 'w', encoding='utf-8') as output:
        for root, dirs, files in os.walk(directory):
            # Filter out folders to ignore
            dirs[:] = [d for d in dirs if not any(ignored in d for ignored in ignore_folder_substrings)]

            for file in files:
                if any(ignored in file for ignored in ignore_file_substrings):
                    continue
                if any(file.endswith(ext) for ext in extensions):
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, directory)

                    output.write(f"{relative_path}:\n\n")
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            output.write(f"{content}\n\n{'-'*40}\n\n")
                    except Exception as e:
                        output.write(f"Error reading file: {e}\n\n{'-'*40}\n\n")

def main():
    parser = argparse.ArgumentParser(description='Write files with specific extensions and contents to a text file.')
    parser.add_argument('directory', help='Start directory to search in')
    parser.add_argument('extensions', nargs='+', help='File extensions to include (e.g., .go .py .txt)')
    parser.add_argument('--out', default='output.txt', help='Output file name (default: output.txt)')
    parser.add_argument('--ignore-files', nargs='*', default=[], help='File substrings to ignore')
    parser.add_argument('--ignore-folders', nargs='*', default=[], help='Folder substrings to ignore')

    args = parser.parse_args()

    write_files_with_extensions_to_text(
        args.directory,
        args.extensions,
        args.out,
        args.ignore_files,
        args.ignore_folders
    )

if __name__ == '__main__':
    main()
