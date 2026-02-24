# ExchangeRates/__init__.py  

from flask import Blueprint

exchange_rate_bp = Blueprint(
    'exchange_rate_bp', 
    __name__, 
    template_folder= 'templates', 
    static_folder='static',
    url_prefix='/ExchangeRates'
    )

from . import routes_exch_rate
# Import routes to register them with the blueprint

