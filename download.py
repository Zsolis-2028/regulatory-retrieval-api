import requests

url = "https://capitol.texas.gov/tlodocs/88R/billtext/pdf/HB00004F.pdf"
response = requests.get(url)

with open("regulation.pdf", "wb") as f:
    f.write(response.content)

print("Downloaded regulation.pdf")