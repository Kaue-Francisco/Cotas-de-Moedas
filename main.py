# Fazer requisições
import requests

# Para criar uma página na Web
from flask import Flask, render_template, request

# Cotação para o  Americano
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/USD-BRL')
cotacao_tot = r.json()
dolar = cotacao_tot['USDBRL']['bid']


# Cotação para o Euro
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/EUR-BRL')
cotacao_tot = r.json()
euro = cotacao_tot['EURBRL']['bid']


# Cotação para o Iene
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/JPY-BRL')
cotacao_tot = r.json()
ien = cotacao_tot['JPYBRL']['bid']


# Cotação para a Libra
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/GBP-BRL')
cotacao_tot = r.json()
gbp = cotacao_tot['GBPBRL']['bid']


# Cotação para Franco Suiço
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/CHF-BRL')
cotacao_tot = r.json()
chf = cotacao_tot['CHFBRL']['bid']

# Cotação para Dolar Canadense
r = requests.get(f'https://economia.awesomeapi.com.br/json/last/CAD-BRL')
cotacao_tot = r.json()
cad = cotacao_tot['CADBRL']['bid']


# Inicialização do Python Flask, para demonstrar a cotação
app = Flask(__name__)
@app.route('/', methods = ['POST'])
def index():
    
    # Definindo os valores!
    valor = request.form['valor']
    _dolar = 0
    _euro = 0
    _ien = 0
    _gbp = 0
    _chf = 0
    _cad = 0
    
    # Convertendo os valores
    if float(valor) <= 0:
        valor = 1
    else:
        _dolar = '{:.2f}'.format(float(dolar) * float(valor))
        _euro = '{:.2f}'.format(float(euro) * float(valor))
        _ien = '{:.2f}'.format(float(ien) * float(valor))
        _gbp = '{:.2f}'.format(float(gbp) * float(valor))
        _chf = '{:.2f}'.format(float(chf) * float(valor))
        _cad = '{:.2f}'.format(float(cad) * float(valor))
    
    
    return render_template('index.html', dolar=_dolar, euro=_euro,  ien=_ien,  gbp=_gbp,  chf=_chf,  cad=_cad)

if __name__ == "__main__":
    app.run(debug=True)