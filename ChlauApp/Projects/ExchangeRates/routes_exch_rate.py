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
            #["ExcRateViewer2026-03-25_light.jpg","ExcRateViewer2026-03-25_dark.jpg"],
        "project_description": """
            <p>Exchange Rate Viewer is a lightweight web application that displays currency exchange rates
            in a clean, easy-to-read interface. The demo uses a static JSON dataset to ensure consistent
            performance and avoid dependency on external services.
            </p>
        """,
        "features": [ 
            "Simple UI: Quick, readable currency lookup in a clean table layout.",
            "Static data source: Uses JSON for stable, predictab le demos.",
            "Responsive layout: Designed to stay usable on different screen sizes.",
            "Modular structure: Matches my reusable project-page and folder template.",
            "No external dependencies: Fast load times without live API calls.",
        ],
        "architecture_notes": """
            <h4>Data layer</h4>
            <p>
                The app loads a static JSON file containing exchange-rate data. This keeps the demo stable,
                avoids API limits, and removes the need for API keys in the public version.
            </p>

            <h4>UI layer</h4>
            <p>
                The UI renders the rates in a simple, responsive table with minimal styling for clarity and
                readability. The visual style is aligned with the rest of my portfolio.
            </p>

            <h4>Project structure</h4>
            <p> 
                The code follows my universal project template, keeping data, layout and assets separated. 
                This makes it easy to upgrade later-for example, by swapping the static JSON for a live
                API handler. 
            </p> 
            """,
        "demo_link": "ExchangeRateViewer",
        "source_link": "https://github.com/chlau5206/ChlauApp/tree/main/ChlauApp/Projects/ExchangeRates", 
        "download_link": None,
        "future_work": [
            # "API integration: Swap static JSON for a controlled API handler.", --- Done
            "Last updated: Show a timestamp for the latest data refresh.",
            "Search/filter: Quickly find specific currencies.",
            "Mobile polish: Further refine the compact layout.",
            "Trends: Optional small chart for USD trends over time.",

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
