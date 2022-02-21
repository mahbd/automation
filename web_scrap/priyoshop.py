from bs4 import BeautifulSoup as Bs
import requests
import json

base_url = 'https://priyoshop.com'


def get_product_description(product_url1):
    pr = requests.get(product_url1)
    p_soup = Bs(pr.content, 'html.parser')
    return p_soup.find('div', {'class': 'full-description'}).text


def get_products_of_category(category):
    r = requests.get(f"{base_url}/{category}#/pageSize=60")
    soup = Bs(r.content, 'html.parser')
    products = []

    items = soup.find_all('div', {'class': 'product-item'})
    for item in items:
        name = item.find('h2', {'class': 'product-title'}).text
        price = item.find('span', {'class': 'price actual-price'}).text
        product_url = base_url + item.find('h2', {'class': 'product-title'}).find('a')['href']
        description = get_product_description(product_url)
        image_url = item.find('img')['src']
        products.append({
            'name': name,
            'price': price,
            'description': description,
            'imageUrl': image_url,
            'productUrl': product_url
        })
    return products


category_list = ['grocery-items', 'fruits-vegetables', 'snacks-items', 'face-mask', 'smart-phone-2']

categories = []
for category in category_list:
    categories.append({
        'category': category,
        'products': get_products_of_category(category)
    })
with open('priyoshop.json', 'w+') as f:
    f.write(json.dumps(categories))

for category in categories:
    print(f"{len(category['products'])} products in {category['category']}")
