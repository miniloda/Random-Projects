import os




def create_folder(folder_name,types):
    for type_name in types:
    # Construct the full path of the new folder
        folder_path = os.path.join(current_dir, type_name)
    
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    return folder_path

def sort_files_in_folder(folder_path, types):
    """
    This function sorts files in a given folder based on their extensions.

    Parameters:
    folder_path (str): The path of the folder where the files are located.
    types (dict): A dictionary where keys are type names and values are lists of extensions.

    Returns:
    None. The function moves files to their respective folders within the given folder.
    """
    for type_name, extensions in types.items():
        for extension in extensions:
            file_list = [file for file in os.listdir(folder_path) if file.endswith(extension)]
            for file in file_list:
                # Construct the full path of the file
                file_path = os.path.join(folder_path, file)
                # Move the file to its respective folder
                new_folder_path = os.path.join(folder_path, type_name)
                os.replace(file_path, os.path.join(new_folder_path, file))

if __name__ == "__main__":
    types = {
        "Code": [".py", ".cpp", ".java", ".js", ".ts", ".go"],
        "Documents": [".txt", ".pdf", ".doc", ".docx"],
        "Images": [".jpg", ".png", ".gif", ".jpeg"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Audio": [".mp3", ".wav", ".flac", ".ogg"],
        "Archives": [".zip", ".tar", ".rar", ".7z", ".gz"],
        "Notebooks": [".ipynb"]

    }
    current_dir = os.getcwd()  # Get the current working directory
    #Check if the 'Files' folder exists, otherwise create it
    create_folder(current_dir, types)
    sort_files_in_folder(current_dir, types)