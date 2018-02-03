import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Motherboards/Category/ID-20?Tpk=motherboards'

# grabbing the page
uClient = uReq(my_url)
content_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(content_html, "html.parser")

productinfos = page_soup.findAll("div",{"class":"item-container"})

filename = "motherboards.csv"
f = open(filename, "w") 

headers = "brand, product_name, msrp, shipping\n" 

f.write(headers)

for productinfo in productinfos:
    brand = productinfo.findAll("img",{"class":"lazy-img"})["title"]
    
    modelinfo = productinfo.findAll("a",{"class":"item-title"})
    product_name = modelinfo[0].text
    
    priceinfo = productinfo.findAll("li",{"class":"price-current"})
    msrp = priceinfo.strong.text
    
    shipping_container = productinfo.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    print("brand " + brand)
    print("product_name" + product_name)
    print("msrp " + msrp)
    print("shipping " + shipping) 

f.write(brand + "," + product_name.replace(",", "|") + "," + msrp + "," + shipping + "\n") 
f.close()

