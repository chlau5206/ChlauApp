# Board/Board.py -- Contains the routes and CRUD operations

import logging, os
from flask import render_template, json, jsonify, current_app
from . import exchange_rate_bp
from ..models import handle_exception

logger = logging.getLogger(__name__)

@exchange_rate_bp.route("/")  
def exchangeRate():   
    logger.info ("Exchange Rate route accessed")
    return render_template("exchangeRate.html",
                           title="Exchange Rate")

@exchange_rate_bp.route("/loadExchangeRate", methods=['GET'])
def load_exchange_rate():
    
    FILE_PATH = os.path.join(exchange_rate_bp.static_folder, 'data', 'LatestRate.json')
    #logger.debug(f'File_path = {FILE_PATH}')
    try:
        ## for debug:
        # rate = '{"success":true,"timestamp":1712252526,"base":"EUR","date":"2024-09-10",
        #          "rates":{"EUR":1,"USD":1.086131,"MXN":17.932246,"SGD":1.462384,"KRW":1460.499318,"THB":39.817943,"TWD":34.789331}}'

        with open(FILE_PATH, "r") as rate:
            data = json.load(rate)   # read this file and convert the content into a Python dictionary
            logger.info('Data loaded successfully')
        return jsonify(data)  # Use jsonify to convert the Python dictionary back into JSON format
    except FileNotFoundError:
        return jsonify({"error": "Data not found"}), 404  # Return a 404 error
    except json.JSONDecodeError as e:
        logger.error(f"Error in /loaddata: {e}")
        return jsonify({"error": "Invalid JSON data"}), 500  # Return a 500 error
    # except IOError as e:
    #     if not os.path.exists(os.path.dirname(FILE_PATH)): 
    #         logger.error(f'Error: The directory does not exist. {e}')
    #     else:
    #         logger.error(f'IO Error: {e}')
    except ValueError:
        logger.error("Error: Incorrect value.")
    except Exception as e:
        error_message = handle_exception(e) 
        logger.error(error_message)

