
from flask import render_template
from flask import redirect, url_for, flash, current_app, request
from flask_login import login_required 

import logging
logger = logging.getLogger(__name__)


#@project_bp.route("/project")
def project_page():
    context = {
        "project_title": "DemoBoard",
        "project_subtitle": "A safe, dual-database message board demo.",
        "project_tags": ["Python", "Flask", "SQLite", "Bulma"],
        "screenshots": ["demo1.png", "demo2.png"],
        "project_description": """
            <p>DemoBoard is a safe, public-friendly message board...</p>
        """,
        "features": [
            "Visitor mode and Power-User mode",
            "Dual database architecture",
            "Safe public interaction",
        ],
        "architecture_notes": """
            <p>This project uses two SQLite databases...</p>
        """,
        "demo_link": "/demoboard",
        "source_link": "https://github.com/charles/demoboard",
        "download_link": None,
        "future_work": [
            "Add admin-only filters",
            "Add pagination",
        ],
        "last_updated": "February 2026"
    }
    return render_template("project_name/project.html", **context)