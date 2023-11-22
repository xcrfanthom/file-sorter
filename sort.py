import os
import shutil

source_folder = r"Add source folder directory"
destination_folder = r"Add destination folder directory"

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)
    
extension_folder_mapping = {
    "txt": "Text",
    "pdf": "PDF",
    "jpg": "Images",
    "png": "Images",
    "docx": "Documents",
    "zip": "Compressed",
    "xlsx": "Spreadsheets",
    "exe": "Executables",
    "ini": "Configuration",
    "mp3": "Audio",
    "mp4": "Videos",
    "py": "Python",
    "wav": "Raw-Audio",
    "pptx": "Presentations",
}

def sort_files_by_extension(source, destination):
    for filename in os.listdir(source):
        file_extension = filename.split(".")[-1].lower()
        source_path = os.path.join(source, filename)
        
        if os.path.isfile(source_path):
            if file_extension in extension_folder_mapping:
                destination_path = os.path.join(destination, extension_folder_mapping[file_extension])
                if not os.path.exists(destination_path):
                    os.mkdir(destination_path)
                shutil.move(source_path, os.path.join(destination_path, filename))
            else:
                print(f"Extension '{file_extension}' not in the mapping. Skipping '{filename}'.")
sort_files_by_extension(source_folder, destination_folder)
