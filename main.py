import requests
import sys

def url_shorter(url: str) -> str:
    try:
        res = requests.post("https://jli.li/api/compress", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"}, json={"link": url})
        if "id" in res.json():
            return res.json()["id"]
        else:
            return "error"
    except:
        return "error"

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "-u":
        print(">Invalid input.\n>Usage: py main.py -u <link>")
        sys.exit(1)
    
    id = url_shorter(sys.argv[2])
    if id == "error":
        print(">Error: URL Format Error or Something Went Wrong")
    else:
        print(f">Shorted URL: https://jli.li/{id}")