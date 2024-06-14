import requests
from bs4 import BeautifulSoup

url = "https://companiesmarketcap.com/"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
# 发送GET请求
response = requests.get(url,headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find_all('div', class_='company-code')
    company = [code.text.strip() for code in title]
else:
    print("请求失败，状态码:", response.status_code)
