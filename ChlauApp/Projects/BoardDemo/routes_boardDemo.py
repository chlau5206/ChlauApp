# boardDemo/routes_boardDemo.py


from flask import render_template
from . import boardDemo_bp, demoBoard

import logging
logger = logging.getLogger(__name__)

@boardDemo_bp.route('/')
def project():
    context = {
        "project_title": "boardDemo",
        "project_subtitle": "A safe, dual-database message board demo.",
        "project_tags": ["Python", "Flask", "SQLAlchemy", "SQLite", "Bulma", "csrf"],
        "screenshots": ["demoBoard_AddNewMsg.jpg", "demoBoard_PowerUser_Page.jpg"],

        "project_description": """
            <p>
                boardDemo is a lightweight, safe, and public-friendly message board designed to
                demonstrate clean form handling, SQLAlchemy models, and a dual-database architecture.
                The project includes two modes—Visitor Mode and Power-User Mode—allowing users to
                explore the UI without risking accidental data modification.
            </p>
            
                <p>
                The demo uses an in-memory SQLite database for public interactions, ensuring that
                all posts reset automatically on each server restart. This keeps the demo safe while
                still showing realistic CRUD behavior.
            </p>
        """,

        "features": [
            "Visitor Mode and Power-User Mode",
            "Dual-database architecture (persistent + in-memory)",
            "Safe public interaction with automatic resets",
            "Clean Bulma-based UI",
            "Simple, readable SQLAlchemy models"
        ],

        "architecture_notes": """
            <p>
                boardDemo uses two SQLite databases: a persistent one for development and a
                temporary in-memory database for the public demo. This ensures that visitors can
                freely experiment with posting messages without affecting real data.
            </p>
            <p>
                The project follows a modular Flask structure with blueprints, separated templates,
                and clean routing. SQLAlchemy models define posts, timestamps, and sorting behavior.
            </p>
        """,

        "demo_link": "DemoShow",
        "source_link": "https://github.com/chlau5206/ChlauApp/tree/main/ChlauApp", 
        "download_link": None,

        "future_work": [
            "Add search or keyword filtering",
            "Optional: add a compact mobile layout"
        ],

        "last_updated": "February 2026"
    }

    return render_template("project_board.html", **context)
