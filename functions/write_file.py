
def write_file(working_directory, file_path, content):
    """
    Write content to a specified file within working_directory.
    - Creates the file if it doesn't exist.
    - Prevents writes outside the working directory.
    """

    import os

    # Join the working directory with the specified file path
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the full path is within the working directory
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.'
    
    try:
        with open(full_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"