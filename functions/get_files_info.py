import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    """
    Get information about files in the specified directory.
    Ensures the directory exists and does not traverse outside the working directory.
    """

    # Join the working directory with the specified directory
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    # Ensure the full path is within the working directory
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
    
    # Check if the directory is indeed a directory
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory.'

    # Use "current" to refer to the current directory in output
    if directory == ".":
        directory = "current"

    # List of files and their info  
    files = f'Result for {directory} directory:\n'
    try:
        items = sorted(os.listdir(full_path))  # sort for consistent order
        for item in items:
            item_path = os.path.join(full_path, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            files += f'- {item}: file_size={size} bytes, is_dir={is_dir}\n'
    except Exception as e:
        return f"Error accessing directory: {e}"

    return files

