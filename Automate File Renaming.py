import os

def rename_files_in_directory(directory_path, base_name="file", extension=None):
    try:
        files = sorted([
            f for f in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, f)) and not f.startswith('.')
        ])

        print(f"Found {len(files)} files to rename.")

        for i, filename in enumerate(files):
            file_ext = os.path.splitext(filename)[1]
            if extension and file_ext != extension:
                continue  # skip non-matching extension

            new_filename = f"{base_name}_{i+1:03d}{file_ext}"
            src = os.path.join(directory_path, filename)
            dst = os.path.join(directory_path, new_filename)

            os.rename(src, dst)
            print(f"Renamed: {filename} ➝ {new_filename}")

        print("Renaming complete.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    target_folder = input("Enter the directory path: ").strip()
    base_name = input("Enter base name for files (default: file): ").strip() or "file"
    extension = input("Enter file extension to filter (e.g., .jpg) or press Enter for all: ").strip()
    if extension == "":
        extension = None

    rename_files_in_directory(target_folder, base_name, extension)
