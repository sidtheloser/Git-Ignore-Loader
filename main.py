import requests, argparse

parser = argparse.ArgumentParser()

parser.add_argument("--langs", nargs="+", required=True)

args = parser.parse_args()

langs = ""

print("Will download for:")

for i in args.langs:
    print(f"- {i}")
    langs += f"{i},"

print("---")

langs = langs[:-1]

url = f"https://www.toptal.com/developers/gitignore/api/{langs}"

print(f"Downloading from: {url}")

response = requests.get(url)

if response.status_code == 200:
    with open(".gitignore", "wb") as file:
        file.write(response.content)
        
    print("Download complete! .gitignore added to repo!")

else:
    print(f"Failed to download. Status code: {response.status_code}")
