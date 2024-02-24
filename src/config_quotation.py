import requests

class Quotation():
    '''Class to get the currency quotation from the API'''
    def __init__(self):
        self.dolar = 0
        self.euro = 0
        self.ien = 0
        self.gbp = 0
        self.chf = 0
        self.cad = 0

        self.urls = {'dolar':'https://economia.awesomeapi.com.br/json/last/USD-BRL',
        'euro':'https://economia.awesomeapi.com.br/json/last/EUR-BRL',
        'ien':'https://economia.awesomeapi.com.br/json/last/JPY-BRL',
        'gbp':'https://economia.awesomeapi.com.br/json/last/GBP-BRL',
        'chf':'https://economia.awesomeapi.com.br/json/last/CHF-BRL',
        'cad':'https://economia.awesomeapi.com.br/json/last/CAD-BRL',}

    def get_value_quotation(self):
        '''Method to get the currency quotation from the API'''
        for url in self.urls:
            cotacao_tot = requests.get(self.urls[url]).json()
        
            match (url):
                case 'dolar':
                    self.dolar = cotacao_tot['USDBRL']['bid']
                case 'euro':
                    self.euro = cotacao_tot['EURBRL']['bid']
                case 'ien':
                    self.ien = cotacao_tot['JPYBRL']['bid']
                case 'gbp':
                    self.gbp = cotacao_tot['GBPBRL']['bid']
                case 'chf':
                    self.chf = cotacao_tot['CHFBRL']['bid']
                case 'cad':
                    self.cad = cotacao_tot['CADBRL']['bid']