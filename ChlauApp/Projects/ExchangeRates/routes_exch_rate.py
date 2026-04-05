# ExchangeRate/routes_Exch_rate.py 

import os 
from flask import render_template #, current_app
from . import exchange_rate_bp , ExchangeRates

import logging
logger = logging.getLogger(__name__)

@exchange_rate_bp.route('/')
def project():
    screenshots = get_screenshots(exchange_rate_bp.static_folder)
    context = {
        "project_title": "Exchange Rate Viewer",
        "project_subtitle": "A simple, clean currency-rate viewer built for clarity and stable demos.",
        "project_tags": ["Python", "Flask", "Bulma", "API"],
        "screenshots": screenshots,
        "project_description": """
            <p>
            ExchangeRate Viewer is a lightweight, fast currency lookup tool designed for clarity and reliability. It retrieves daily exchange rate data from a live API, stores the results as JSON, and performs EUR‑to‑USD conversion directly in the browser using JavaScript. The UI is clean, responsive, and optimized for quick reference on any device.
            </p>
        """,
        "features": [ 
            "⚡ Automated Daily Updates: A scheduled PythonAnywhere task refreshes exchange rates every day, ensuring the data stays current without manual intervention.",
            "🔁 Hybrid ETL Pipeline-Extract(Server): API handler retrieves EUR‑based exchange rates.",
            "🔁 Hybrid ETL Pipeline-Load(Server): Results are saved as JSON for fast UI loading",
            "🔁 Hybrid ETL Pipeline-Transform(Client): JavaScript converts EUR‑based values into USD‑based rates dynamically",
            "🧩 Clean, Simple UI: A minimal table layout provides quick, readable currency lookup without distractions.",
            "🌙 Responsive + Dark-Mode Aware: The layout adapts to different screen sizes and respects the user’s system/browser dark‑mode preference.",
            "⚡ Fast, Stable Data Delivery: The UI loads instantly using pre‑processed JSON, avoiding API delays, rate limits, and unnecessary client‑side calls.",
            "🗂️ Modular, Reusable Structure: Built using my universal project‑page and folder template, making the module easy to maintain and extend.",
        ],
        "architecture_notes": """
            <h4>Scheduled Task (PythonAnywhere)</h4>
            <p>  
            - Runs daily <br>
            - Calls the API handler <br>
            - Saves raw EUR‑based JSON <br>
            </p> 

            <h4>API Handler (Server)</h4>
            <p>  
            - Fetches EUR‑based exchange rates <br>
            - Validates and normalizes the dataset <br>
            - Stores the raw JSON for the frontend <br>
            </p> 
            
            <h4>Frontend Logic (Client)</h4>
            <p>  
            - Loads the JSON file <br>
            - Converts EUR‑based values into USD‑based rates using JavaScript <br>
            - Renders the table dynamically <br>
            </p> 

            <h4>UI Layer</h4>
            <p>  
            - Bulma‑based responsive table <br>
            - Dark‑mode aware <br>
            - No external JS dependencies <br>
            </p> 
            """,
        "demo_link": "ExchangeRateViewer",
        "source_link": "https://github.com/chlau5206/ChlauApp/tree/main/ChlauApp/Projects/ExchangeRates", 
        "download_link": None,
        "future_work": [
            "Add currency search/filter",
            "Add 'favorite currencies' section",
            "Add historical trend charts",
            "Add multi‑base currency toggle",
            "Add last‑updated timestamp in UI",
        ],
        "last_updated": "March 2026"
    }
    return render_template("project_exch.html", **context)

def get_screenshots(folder_path):
    img_path = os.path.join(folder_path, "img")
    if not os.path.exists(img_path):
        return []

    files = sorted([
        f for f in os.listdir(img_path)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    ])
    return files
