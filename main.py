# Fazer requisições
import requests

# Para criar uma página na Web
from flask import Flask, render_template
import pprint

# Definindo as cotações
cotacao_dol = 'USD-BRL'
cotacao_eur = 'EUR-BRL'
cotacao_ien = 'JPY-BRL'
cotacao_gbp = 'GBP-BRL'
cotacao_chf = 'CHF-BRL'
cotacao_cad = 'CAD-BRL'


# Cotação para o  Americano
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/{cotacao_dol}')
cotacao_tot = r.json()
dolar = cotacao_tot['USDBRL']['bid']


# Cotação para o Euro
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/{cotacao_eur}')
cotacao_tot = r.json()
euro = cotacao_tot['EURBRL']['bid']


# Cotação para o Iene
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/{cotacao_ien}')
cotacao_tot = r.json()
ien = cotacao_tot['JPYBRL']['bid']


# Cotação para a Libra
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/{cotacao_gbp}')
cotacao_tot = r.json()
gbp = cotacao_tot['GBPBRL']['bid']


# Cotação para Franco Suiço
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/{cotacao_chf}')
cotacao_tot = r.json()
chf = cotacao_tot['CHFBRL']['bid']


# Cotação para Dolar Canadense
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/{cotacao_cad}')
cotacao_tot = r.json()
cad = cotacao_tot['CADBRL']['bid']



# Inicialização do Python Flask, para demonstrar a cotação
app = Flask(__name__)
@app.get('/')
def index():
    return render_template('index.html', dolar=dolar, euro=euro, ien=ien, gbp=gbp, chf=chf, cad=cad)

if __name__ == "__main__":
    app.run(debug=True)