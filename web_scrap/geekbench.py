from bs4 import BeautifulSoup as Bs
import requests

base = "https://browser.geekbench.com"
last_part = "/v5/cpu/search?page=1&q=3500X&utf8=%E2%9C%93"
count = 0
data = []
while True:
    response = requests.get(base + last_part)
    soup = Bs(response.content, 'html.parser')
    items = soup.select(".col-12.list-col")
    for item in items:
        device = item.select_one(".list-col-model").getText().strip()
        platform = item.select(".list-col-text")[1].getText().strip()
        single_core = item.select(".list-col-text-score")[0].getText().strip()
        multi_core = item.select(".list-col-text-score")[1].getText().strip()
        if platform == 'macOS' and '6 cores' in device:
            data.append([device, platform, int(single_core), int(multi_core)])
    last_part = soup.select_one(".page-item.next.next_page ").select_one("a")["href"]
    if last_part == '#' or count > 0:
        break
count += 1
print(f"page: {count}, found: {len(data)}")
total_single, total_multi, max_multi, max_single = 0, 0, 0, 0
min_single, min_multi = 100000000, 100000000
for d in data:
    total_single += d[2]
    max_single = max(max_single, d[2])
    min_single = min(min_single, d[2])
    total_multi += d[3]
    max_multi = max(max_multi, d[3])
    min_multi = min(min_multi, d[3])
print("\n\n")
print(f"single avg: {total_single / len(data)}")
print(f"single max: {max_single}")
print(f"single min: {min_single}")
print(f"multi avg: {total_multi / len(data)}")
print(f"multi max: {max_multi}")
print(f"multi min: {min_multi}")
