from google import genai
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="Your prompt to send to the API")
parser.add_argument("file_name", help="Name of the file to save the py script in")
args = parser.parse_args()

scripts_path = r"your path"
os.makedirs(scripts_path, exist_ok=True)

file_name = os.path.basename(args.file_name)
if not file_name.endswith(".py"):
    file_name += ".py"
output_path = os.path.join(scripts_path, file_name)

api_key = os.getenv("Gemini_API")

client = genai.Client(api_key=api_key)

try:
    request = client.interactions.create(
        model="gemini-3.8-flash", #or whatever model you want to use
        input=args.prompt
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(request.output_text)

    print(f"script saved: {output_path}")

except Exception as e:
    print(f"Fehler: {e}")