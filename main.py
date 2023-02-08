# Fazer requisições
import requests

# Para criar uma página na Web
from flask import Flask, render_template
import pprint


# Cotação para o  Americano
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/USD-BRL')
cotacao_tot = r.json()
dolar = cotacao_tot['USDBRL']['bid']
dolar = dolar[:4]


# Cotação para o Euro
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/EUR-BRL')
cotacao_tot = r.json()
euro = cotacao_tot['EURBRL']['bid']
euro = euro[:4]


# Cotação para o Iene
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/JPY-BRL')
cotacao_tot = r.json()
ien = cotacao_tot['JPYBRL']['bid']
ien = ien[:4]


# Cotação para a Libra
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/GBP-BRL')
cotacao_tot = r.json()
gbp = cotacao_tot['GBPBRL']['bid']
gbp = gbp[:4]


# Cotação para Franco Suiço
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/CHF-BRL')
cotacao_tot = r.json()
chf = cotacao_tot['CHFBRL']['bid']
chf = chf[:4]

# Cotação para Dolar Canadense
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/CAD-BRL')
cotacao_tot = r.json()
cad = cotacao_tot['CADBRL']['bid']
cad = cad[:4]


# Inicialização do Python Flask, para demonstrar a cotação
app = Flask(__name__)
@app.get('/')
def index():
    return render_template('index.html', dolar=dolar, euro=euro, ien=ien, gbp=gbp, chf=chf, cad=cad)

if __name__ == "__main__":
    app.run(debug=True)