import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

cot = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD").json()

conv = []

conv.append(cot["conversion_rates"])

print("As cotações do USD são as seguintes:")
for k,v in conv[0].items():
    print(k,v)