import os
import sys
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv


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

    # If no prompt is provided, display usage instructions
    if not args.prompt:
        print("AI Code Assistant")
        print("Usage: python main.py '<your prompt here>'")
        print("Example: python main.py 'Write a Python function to reverse a string'")
        sys.exit(1)

    # Load the user prompt from command line arguments
    user_prompt = " ".join(args.prompt)  

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    
    # Load your API key from an environment variable or secret management service
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize the client
    client = genai.Client(api_key=api_key)

    # Generate content
    response = client.models.generate_content(
        model=args.model,
        contents=messages,
    )
    if args.verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
       
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
