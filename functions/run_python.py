import os
import subprocess
import sys
from functions.config import TIMEOUT

def run_python_file(working_directory, file_path, args=[]):
    """
    Execute a Python file located within the specified working directory.
    Ensures the file exists and does not traverse outside the working directory.
    """
    # Base Directory Path
    base = os.path.abspath(working_directory)

    # Join the working directory with the specified file path
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the full path is within the working directory
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
    
    # Check if the file exists and is indeed a file
    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found.'
    
    # Check if the file has a .py extension
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        # Execute the Python file and capture output
        result = subprocess.run(
            [sys.executable, full_path] + args,
            capture_output=True,
            cwd=base,
            timeout=TIMEOUT,
            text=True
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."

        return output.strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing Python file: {e.stderr}"
    except Exception as e:
        return f'Error executing Python file: {e}'