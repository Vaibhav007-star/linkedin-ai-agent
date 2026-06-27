from pathlib import Path

# =====================================================
# LinkedIn AI Agent - Project Structure Generator
# =====================================================

# Root folders
folders = [
    "app",
    "config",
    "database",
    "logs",
    "prompts",
    "tests",
    "docs",
    "scripts",
]

# =====================================================
# Application Modules
# =====================================================

modules = {
    "collector": [
        "rss_collector.py",
        "rss_feeds.py",
        "parser.py",
        "service.py",
        "filters.py",
        "schemas.py",
        "utils.py",
    ],

    "classifier": [
        "classifier.py",
        "service.py",
        "prompts.py",
    ],

    "summarizer": [
        "ai_summarizer.py",
        "service.py",
        "prompts.py",
    ],

    "writer": [
        "linkedin_writer.py",
        "service.py",
        "prompts.py",
    ],

    "reviewer": [
        "grammar_checker.py",
        "fact_checker.py",
        "service.py",
        "prompts.py",
    ],

    "image_generator": [
        "image_generator.py",
        "service.py",
        "prompts.py",
    ],

    "publisher": [
        "linkedin_publisher.py",
        "service.py",
    ],

    "scheduler": [
        "scheduler.py",
    ],

    "analytics": [
        "analytics.py",
        "dashboard.py",
    ],

    "database": [
        "database.py",
        "models.py",
    ],

    "utils": [
        "logger.py",
        "helpers.py",
    ],
}

# =====================================================
# Root Files
# =====================================================

files = {
    ".env": "",
    ".gitignore": "",
    "requirements.txt": "",
    "requirements-lock.txt": "",
    "README.md": "# LinkedIn AI Agent\n",
    "main.py": "",
}

# =====================================================
# Create Root Folders
# =====================================================

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

# =====================================================
# Create Modules
# =====================================================

Path("app").mkdir(exist_ok=True)
Path("app/__init__.py").touch(exist_ok=True)

for module, module_files in modules.items():

    module_path = Path("app") / module
    module_path.mkdir(parents=True, exist_ok=True)

    (module_path / "__init__.py").touch(exist_ok=True)

    for filename in module_files:

        file_path = module_path / filename

        if not file_path.exists():
            file_path.write_text("", encoding="utf-8")

# =====================================================
# Config Package
# =====================================================

Path("config").mkdir(exist_ok=True)
Path("config/__init__.py").touch(exist_ok=True)

# =====================================================
# Root Files
# =====================================================

for filename, content in files.items():

    path = Path(filename)

    if not path.exists():
        path.write_text(content, encoding="utf-8")

print("==========================================")
print("✅ LinkedIn AI Agent Project Ready")
print("==========================================")
print("Folders Created :", len(folders))
print("Modules Created :", len(modules))
print("==========================================")