import requests
import bs4

class Parser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        }
    
    def parse(self, url, array):
        response = requests.get(url, headers = self.session.headers)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_ = 'iva-item-root-G3n7v photo-slider-slider-15LoY iva-item-list-2_PpT items-item-1Hoqq items-listItem-11orH js-catalog-item-enum')
        
        for item in items:
            array.append({
                'title': item.find('span', class_ = 'title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt').get_text(strip = True),
                'price': item.find('span', class_ = 'price-text-1HrJ_ text-text-1PdBw text-size-s-1PUdo').get_text(strip = True),
                'link': 'https://www.avito.ru' + item.find('a', class_ = 'link-link-39EVK link-design-default-2sPEv title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc').get('href')
            })
        
    


    