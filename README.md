# ProjectFileExtractor

**ProjectFileExtractor** is a simple Python script that helps you extract and consolidate code or text files into a single `.txt` file — perfect for feeding into AI tools like ChatGPT.

## Features

* 🔍 Recursively scans directories
* 📎 Includes only files with specific extensions
* 🚫 Optionally ignores files and folders by substring
* 📝 Outputs file paths and contents into a clean, readable `.txt` file

## Usage

```bash
python project_file_extractor.py <directory> <extensions...> [--out OUTPUT_FILE] [--ignore-files IGNORES] [--ignore-folders IGNORES]
```

### Arguments

* `<directory>`: Root directory to start searching in
* `<extensions...>`: File extensions to include (e.g., `.py .go .txt`)
* `--out`: *(Optional)* Output file name (default: `output.txt`)
* `--ignore-files`: *(Optional)* Substrings to ignore in file names
* `--ignore-folders`: *(Optional)* Substrings to ignore in folder names

### Example

```bash
python project_file_extractor.py . .py .md --out code_dump.txt --ignore-files test --ignore-folders __pycache__
```

## Output Format

Each file will be listed like this in the output:

```
relative/path/to/file.py:

<file content>

----------------------------------------
```
