import os
from google.genai import types
from functions.config import MAX_READ

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

def get_file_content(working_directory, file_path):
    """
    Get the content of a specified file.
    Ensures the file exists and does not traverse outside the working directory.
    """

    # Join the working directory with the specified file path
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the full path is within the working directory
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
    
    # Check if the file exists and is indeed a file
    if not os.path.isfile(full_path):
        return f'Error: "{file_path}" does not exist or is not a file.'

    try:
        with open(full_path, 'r') as file:
            content = file.read(MAX_READ + 1)
            if len(content) > MAX_READ:
                content = content[:MAX_READ] + f'\n... "{file_path}" truncated at 10000 characters'
        return content
    except Exception as e:
        return f"Error reading file: {e}"