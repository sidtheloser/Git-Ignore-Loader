"""
This here is a tool that I made to write directly to `fallbackdata.py` that 
automatically updates the information regarding language to gitignore repo path
based on the information I get from: https://github.com/github/gitignore/ 's 
root/main directory.
"""

import requests, json

url = "https://api.github.com/repos/github/gitignore/contents/"

print(f"Getting API info through: {url}")

response = requests.get(url)

if response.status_code == 200:
    json_data: list[dict[str, str]] = response.json()

    fallback_dict = {}

    for item in json_data:
        if item["type"] == "file" and item["name"].endswith(".gitignore"):
            fallback_dict[item["name"].removesuffix(".gitignore").lower()] = item["path"]

            print(f"Added {item["name"]}")

    print("Saving to fallbackdata.py ...")

    with open("fallbackdata.py", "w") as f:
        f.write(f"data = {json.dumps(fallback_dict, indent=4, sort_keys=True)}")
    
    print("All done!")

else:
    print(f"API request failed! Status code: {response.status_code}")