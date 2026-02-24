# ePubConverter/routes_ePubConverter.py

def project_page():
    context = {
        "project_title": "ePub Converter (CHS → CHT)",
        "project_subtitle": "A C# utility that converts Simplified Chinese ePub books to Traditional Chinese.",
        "project_tags": ["C#", ".NET", "ePub", "Text Processing", "CLI Tool"],
        "screenshots": ["epubconverter_ui.png", "epubconverter_output.png"],

        "project_description": """
            <p>
                ePubConverter is a practical C# utility that converts Simplified Chinese (CHS)
                ePub books into Traditional Chinese (CHT). The tool extracts the ePub contents,
                processes each XHTML file, performs text conversion, and rebuilds the final ePub.
            </p>
            <p>
                This project demonstrates file handling, text transformation, directory traversal,
                and safe output generation. It is designed as a clean, reliable command-line tool
                for readers who prefer Traditional Chinese formatting.
            </p>
        """,

        "features": [
            "Converts CHS → CHT across entire ePub files",
            "Processes XHTML chapters safely and consistently",
            "Rebuilds the final ePub with preserved structure",
            "Command-line interface for quick usage",
            "Error handling for malformed or unusual ePub files"
        ],

        "architecture_notes": """
            <p>
                The converter extracts the ePub (ZIP) into a temporary working directory, scans
                all XHTML files, and applies a Simplified-to-Traditional Chinese mapping. After
                processing, it rebuilds the ePub archive while preserving metadata, images, and
                folder structure.
            </p>
            <p>
                The project is written in C# using .NET, with a focus on clarity, reliability,
                and predictable output.
            </p>
        """,

        "demo_link": None,
        "source_link": "https://github.com/charles/epubconverter",
        "download_link": "/downloads/epubconverter.zip",

        "future_work": [
            "Add GUI version",
            "Add batch conversion mode",
            "Add support for additional Chinese variants",
            "Optional: add progress bar for large books"
        ],

        "last_updated": "February 2026"
    }

    return render_template("ePubConverter/project.html", **context)