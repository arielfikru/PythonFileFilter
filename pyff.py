import os
import sys
import argparse

def delete_files_with_extension_and_size(folder_path, ext, not_in_ext, max_size_bytes, min_size_bytes):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_ext = os.path.splitext(file)[-1].lower()
                if (ext is None or file_ext == ext) and (not_in_ext is None or file_ext != not_in_ext):
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    if max_size_bytes <= file_size <= min_size_bytes:
                        os.remove(file_path)
                        print(f"Deleted: {file_path} (Size: {file_size} bytes)")
        print("Deletion process completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_size(size_str):
    size_str = size_str.lower().strip()
    if size_str.endswith("kb"):
        return float(size_str[:-2]) * 1024
    elif size_str.endswith("mb"):
        return float(size_str[:-2]) * 1024 * 1024
    elif size_str.endswith("gb"):
        return float(size_str[:-2]) * 1024 * 1024 * 1024
    else:
        return float(size_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete files with specified extension and size")
    parser.add_argument("folder", help="Folder path to filter")
    parser.add_argument("--ext", help="File extension to filter")
    parser.add_argument("--not_in_ext", help="File extension to exclude from deletion")
    parser.add_argument("--max_size", help="Minimum size for deletion (e.g., 10KB, 20MB, 2GB)")
    parser.add_argument("--min_size", help="Maximum size for deletion (e.g., 10KB, 20MB, 2GB)")

    args = parser.parse_args()

    folder_path = args.folder
    ext = args.ext
    not_in_ext = args.not_in_ext
    max_size_str = args.max_size
    min_size_str = args.min_size

    if max_size_str:
        max_size_bytes = parse_size(max_size_str)
    else:
        max_size_bytes = 0

    if min_size_str:
        min_size_bytes = parse_size(min_size_str)
    else:
        min_size_bytes = float('inf')

    delete_files_with_extension_and_size(folder_path, ext, not_in_ext, max_size_bytes, min_size_bytes)
