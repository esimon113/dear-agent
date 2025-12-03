import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
    print("Hello from dear-agent!")

    parser = argparse.ArgumentParser(
        prog="Dear Agent",
        description="An AI agent, because they are everywhere...",
        epilog="Hope this helped..."
    )
    parser.add_argument("prompt", type=str, help="User Prompt")
    args = parser.parse_args()
    prompt = args.prompt

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("'GEMINI_API_KEY' not found!")

    client = genai.Client(api_key=api_key)
    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt)

    metadata = response.usage_metadata
    if metadata is None:
        raise RuntimeError("Failed API request: Response is None")

    print(f"Prompt tokens: {metadata.prompt_token_count}")
    print(f"Response tokens: {metadata.candidates_token_count}")
    print(response.text)


if __name__ == "__main__":
    main()
