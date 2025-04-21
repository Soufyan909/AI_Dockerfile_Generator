import os
import google.generativeai as genai

# Load API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY not found. Please set it as an environment variable.")

# Configure the Gemini model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

PROMPT_TEMPLATE = """
Generate an ideal Dockerfile for {language} with best practices. Just share the Dockerfile without any explanation, between two lines to make copying easy.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language: str) -> str:
    """Generates a Dockerfile for the specified programming language."""
    try:
        prompt = PROMPT_TEMPLATE.format(language=language)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while generating the Dockerfile: {e}"

def main():
    print("🛠️ Dockerfile Generator using Gemini 🛠️")
    language = input("Enter the programming language (e.g., Python, Node.js, Go): ").strip()

    if not language:
        print("⚠️ No language entered. Exiting.")
        return

    dockerfile = generate_dockerfile(language)
    
    print("\n📄 Generated Dockerfile:\n")
    print(dockerfile)
    print("\n✅ Done!")

if __name__ == '__main__':
    main()

