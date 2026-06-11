import requests, argparse, fallbackdata, base64

parser = argparse.ArgumentParser()

parser.add_argument("--langs", nargs="+", required=True)

parser.add_argument("-v", "--version", action="version", version="1.0")

args = parser.parse_args()

langs: list[str] = args.langs

langs_str = ""

print("Will download for:")

for i in langs:
    print(f"- {i}")
    langs_str += f"{i},"

langs_str = langs_str[:-1]

url = f"https://www.toptal.com/developers/gitignore/api/{langs_str}"

print(f"Downloading from: {url}")

response = requests.get(url)

if response.status_code == 200:
    with open(".gitignore", "w") as file:
        file.write(response.content.decode())
        
    print("Download complete! .gitignore added to repo!")

else:
    print(f"Failed to download. Status code: {response.status_code}")
    print("Falling back to GitHub's gitignore repo...")

    url = "https://api.github.com/repos/github/gitignore/contents/"

    gitignore_data = ""

    for i in langs:
        i = i.lower()
        if i in fallbackdata.data:
            curr_url = url + fallbackdata.data[i]
            print(f"Downloading from: {curr_url}")

            response = requests.get(curr_url)

            if response.status_code == 200:
                content = base64.b64decode(response.json()["content"]).decode()
                gitignore_data += f"### START {i.upper()} ###\n" + content + f"\n### END {i.upper()} ###\n"

                print("Download completed successfully!")

            else:
                gitignore_data += f"### FAILED {i} ###\n"
                print(f"Failed to download. Status code: {response.status_code}")

        else:
            gitignore_data += f"### FAILED {i} ###\n"
            print(f"{i} not found in fallback data!")

    with open(".gitignore", "w") as f:
        f.write(gitignore_data)

    print("Tried writing to .gitignore file using fallback!")