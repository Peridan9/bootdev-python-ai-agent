import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    # Get command line arguments
    args = sys.argv[1:]

    # If no arguments are provided, display usage instructions
    if not args:
        print("AI Code Assistant")
        print("Usage: python main.py '<your prompt here>'")
        print("Example: python main.py 'Write a Python function to reverse a string'")
        sys.exit(1)

    # Load the user prompt from command line arguments
    user_prompt = " ".join(args)  

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    
    # Load your API key from an environment variable or secret management service
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize the client
    client = genai.Client(api_key=api_key)

    # Generate content
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
