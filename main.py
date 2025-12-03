import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


def main():
    print("Hello from dear-agent!")

    parser = argparse.ArgumentParser(
        prog="Dear Agent",
        description="An AI agent, because they are everywhere...",
        epilog="Hope this helped..."
    )
    parser.add_argument("prompt", type=str, help="User Prompt")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Use verbose output")
    args = parser.parse_args()
    prompt = args.prompt
    with_verbose = args.verbose

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("'GEMINI_API_KEY' not found!")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=messages)

    metadata = response.usage_metadata
    if metadata is None:
        raise RuntimeError("Failed API request: Response is None")

    if with_verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
    print(response.text)


if __name__ == "__main__":
    main()
