# ePubConverter/routes_ePubConverter.py

from flask import render_template
from . import ePubConv_bp

import logging
logger = logging.getLogger(__name__)

@ePubConv_bp.route('/')
def project():
    context = {
        "project_title": "ePub Converter (CHS → CHT)",
        "project_subtitle": "A C# utility that converts Simplified Chinese ePub books to Traditional Chinese.",
        "project_tags": ["C#", ".NET", "ePub", "Text Processing", "CLI Tool"],
        "screenshots": ["ePubConverterScreenShot.jpg",],

        "project_description": """
            <p>
                ePubConverter is a practical Windows desktop utility that converts Simplified Chinese (CHS)
                ePub books into Traditional Chinese (CHT). The tool extracts the ePub contents, processes each
                XHTML chapter, performs character-by-character mapping, and rebuilds the final ePub with its
                original structure preserved.
            </p>
            <p>
                The project includes both a Windows GUI and a command-line version, both powered by a shared
                <strong>converter.dll</strong> that contains the core text-processing logic. The GUI supports
                drag-and-drop input, batch processing, and automatic renaming of converted files, making it
                easy for readers who prefer Traditional Chinese formatting.
            </p>
            """,

        "features": [
            "1-to-1 array-based CHS → CHT mapping",
            "Processes XHTML chapters safely and consistently while preserving ePub structure",
            "Windows GUI with drag‑and‑drop support for adding ePub files",
            "Batch processing support in GUI versions",
            "Automatic renaming of converted ePub files to CHT",
            "Shared conversion engine via converter.dll (used by both GUI and CLI)",
            "No installation required — portable executable",
            "Error handling for malformed or unusual ePub files"
        ],

        "architecture_notes": """
            <p>
                The converter extracts the ePub (ZIP) into a temporary working directory, scans all XHTML
                files, and applies a <strong>1-to-1 array-based character mapping</strong> to convert
                Simplified Chinese to Traditional Chinese. This avoids dictionary lookups and ensures
                predictable, deterministic output.
            </p>
            <p>
                The core conversion logic is implemented in a standalone <strong>converter.dll</strong>,
                allowing both the Windows GUI and CLI tools to share the same processing engine. The GUI
                provides drag-and-drop support and batch processing, while the CLI offers a lightweight
                alternative for scripted workflows.
            </p>
            <p>
                After processing, the tool rebuilds the ePub archive while preserving metadata, images,
                folder structure, and internal references. The application is distributed as a portable
                executable with no installation required.
            </p>

        """,

        "demo_link": None,
        "source_link": "https://github.com/chlau5206/BookConvert/tree/main",
        # static/data/ePubConverter_Source.zip",
        "download_link": "https://github.com/chlau5206/BookConvert/tree/main/ConvePubWin/bin/Release",
        # static/data/ePubConverter.zip",
        "simple_link": "https://github.com/chlau5206/BookConvert/tree/main/SimpleFiles",
        # static/data/Test_参加奥运.epub",

        "future_work": [
            "Add reversion conversion (CHT → CHS)",
            "Add support for GBK (DBCS) ePub files — current version requires UTF‑8",
            "Optional: add progress bar for large books"
        ],

        "last_updated": "February 2026"
    }

    return render_template("project_conv.html", **context)
