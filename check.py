import requests
import json
import requests
from bs4 import BeautifulSoup

with open("arb_wallets.txt", "r") as file:
    arb_wallets = file.read().splitlines()

all_tokens = 0

for wallet in arb_wallets:
    address = wallet.lower()

    url = f"https://arbitrum.foundation/eligibility?address={address}"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    _script = soup.find("script", id="__NEXT_DATA__")
    script_json = json.loads(_script.text)

    eligble = script_json["props"]["pageProps"]["eligibility"]
    tokens = eligble["tokens"]
    points = eligble["points"]

    print(f"{address} {tokens} {points}")

    all_tokens += int(tokens)

print(f"{all_tokens}")
