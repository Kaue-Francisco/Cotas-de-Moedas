# Import of the necessary libraries
from flask import Flask, render_template, request
from config_quotation import Quotation

# Creating the app
app = Flask(__name__)

# Creating the route to the index page
@app.route('/', methods = ['POST', 'GET'])
def index():
    '''Route to the index page, with the form to convert the currency.'''
    valor = 1
    _dolar = 0
    _euro = 0
    _ien = 0
    _gbp = 0
    _chf = 0
    _cad = 0

    if request.method == 'POST':
        # Getting the value from the form
        valor = request.form['valor']
    
        # Checking if the value is less than or equal to 0
        if float(valor) <= 0:
            valor = 1
        else:
            _dolar = '{:.2f}'.format(float(valor) / float(cotacao.dolar))
            _euro = '{:.2f}'.format(float(valor) / float(cotacao.euro))
            _ien = '{:.2f}'.format(float(valor) / float(cotacao.ien))
            _gbp = '{:.2f}'.format(float(valor) / float(cotacao.gbp))
            _chf = '{:.2f}'.format(float(valor) / float(cotacao.chf))
            _cad = '{:.2f}'.format(float(valor) / float(cotacao.cad))
    
        return render_template('index.html', dolar=_dolar, euro=_euro,  ien=_ien,  gbp=_gbp,  chf=_chf,  cad=_cad)

    return render_template('index.html', dolar=cotacao.dolar[:4], euro=cotacao.euro[:4],  ien=cotacao.ien[:4],  gbp=cotacao.gbp[:4],  chf=cotacao.chf[:4],  cad=cotacao.cad[:4])

if __name__ == "__main__":
    cotacao = Quotation()
    cotacao.get_value_quotation()
    app.run(debug=True)