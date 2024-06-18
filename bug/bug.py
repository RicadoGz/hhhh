import requests
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
r=requests.get("https://movie.douban.com/top250",headers=headers)
if r.ok:
    print(r.text)
else:
    print(r.status_code)