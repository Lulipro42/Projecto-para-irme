from bs4 import BeautifulSoup
import requests
 
url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'
headers = {
  'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
  print("la peticion fue exitosa")
  
  soup = BeautifulSoup(response.text, "html.parser")
  
  #print(soup.prettify())
  title_tag = soup.title
  if title_tag:
    print(f"el titulo de la web es {title_tag.text}")

  # fint price using bs
 # price_span = soup.find("span", class_="rc-prices-fullprice")
  #if price_span:
      #print(f"el precio del producto es: {price_span.text}")
    
  # find all the prices 
 # price_span = soup.find_all("span", class_="rc-prices-fullprice")
 # for price in price_span:
  #   print(f"el precio del producto es:{price.text}")
  
  # fon each product an get the name and the price
  products = soup.find_all(class_="rc-productselection-item")
  for product in products:
    name = product.find(class_="list-title").text
    price = product.find(class_="rc-prices-fullprice").attrs
    print(f"el producto con las caracateristicas :\n{name}\n precio de {price}\n")