# File Filtering Tool

This Python script allows you to filter files in a specified folder based on their extension and size. You can specify the extension of files you want to keep and set size thresholds for both maximum and minimum file sizes.

## Usage

1. Ensure you have Python installed on your system.

2. Clone or download this repository to your local machine.

3. Open a terminal or command prompt.

4. Navigate to the directory where the script is located using the `cd` command.

5. Run the script by providing the necessary arguments:

   ```bash
   python pyff.py folder_path --ext file_extension --max_size max_file_size --min_size min_file_size
   ```

   - `folder_path`: The path to the folder you want to filter.
   - `file_extension`: (Optional) The extension of files you want to keep. If not specified, all file types will be considered.
   - `max_file_size`: (Optional) The maximum size for files to be considered for deletion (e.g., 10KB, 20MB, 2GB).
   - `min_file_size`: (Optional) The minimum size for files to be considered for deletion (e.g., 10KB, 20MB, 2GB).

6. The script will then go through the specified folder and its subfolders, deleting files that meet the criteria you provided.

## Examples

- Delete all `.txt` files larger than 5 megabytes in the folder "data":

   ```bash
   python pyff.py data --ext txt --min_size 5MB
   ```

- Delete all files larger than 1 gigabyte in the folder "documents":

   ```bash
   python pyff.py documents --max_size 1GB
   ```

## Note

- Be cautious when using this script, as it will permanently delete files.
- Double-check the arguments you provide to avoid accidental data loss.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
