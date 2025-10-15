import os
import sys
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.config import SYSTEM_PROMPT, MAX_ITERATIONS
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function, available_functions

# def call_function(function_call_part, verbose=False):
#     """
#     Calls the appropriate function based on the function call part provided by the AI model.
    
#     Args:
#         function_call_part (types.FunctionCall): The function call part from the AI model response.
#         verbose (bool): If True, prints detailed information about the function call.

#     """

def main():
    load_dotenv()

    # Create a parser to handle command line arguments
    parser = argparse.ArgumentParser(description="AI Code Assistant")

    parser.add_argument(
        "prompt",
        type=str,
        nargs="+",
        help="The prompt to send to the AI model. Enclose in quotes if it contains spaces.",
    )

    parser.add_argument(
        "--model",
        type=str,
        default="gemini-2.0-flash-001",
        help="The AI model to use (default: gemini-2.0-flash-001)",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    # Parse the command line arguments
    args = parser.parse_args()
    verbose = args.verbose

    # If no prompt is provided, display usage instructions
    if not args.prompt:
        print("AI Code Assistant")
        print("Usage: python main.py '<your prompt here>'")
        print("Example: python main.py 'Write a Python function to reverse a string'")
        sys.exit(1)

    # Load the user prompt from command line arguments
    user_prompt = " ".join(args.prompt)  

    # Load your API key from an environment variable or secret management service
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize the client
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    iteration = 0

    while True:
        iteration += 1
        if iteration > MAX_ITERATIONS:
            print(f'Exceeded maximum iterations ({MAX_ITERATIONS}). Exiting.')
            sys.exit(1)
        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final Response")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
    

def generate_content(client, messages, verbose):

    
     # Generate content
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT)
    )

    # Collect all candidate messages and append to messages
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    # if verbose, print token usage
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # If there are no function calls, just return the text response
    if not response.function_calls:
        return response.text
    
    # Process each function call in the response
    function_responses = []
    for function_call_part in response.function_calls:
        # Call the function and get the result
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    messages.append(
        types.Content(
            role="user",
            parts=function_responses
        )
    )
    


if __name__ == "__main__":
    main()
