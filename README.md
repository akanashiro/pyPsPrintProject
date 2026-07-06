# pyPsPrintProject

Automated tool for generating professional documentation of PeopleSoft projects exported from Application Designer.

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()

![front](images/AppUI.png)

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Basic Usage](#basic-usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Supported Definitions](#supported-definitions)
- [Known Limitations](#known-limitations)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## ✨ Features

- 🚀 **UI** - UI built with PySide6 in mind
  - If PySide6 is not installed, then fallbacks to Tkinter
  - If Tkinter is not installed, then returns an error
- ⚙️ **Command line** - now is ```main_cmd.py```
- 🔍 **XML Parser** - Automatically extract definitions from PeopleSoft projects
- 📊 **30+ object types** - Fields, Records, Pages, Components, App Engine, etc
- ⚙️ **Customizable templates** - Use Jinja2 to adapt the format to your needs
- 🤝 **Open Source** - I share this code to the community. Play with it, fork it!

> **Note:** This is an actively developed hobby project. It works very well for most projects, but there may be unsupported edge cases.

## 🔧 Prerequisites

### System
- **Python**: 3.8 or higher
- **pip**: Python package manager
- **OS**: Windows, macOS or Linux

### PeopleSoft
- **Application Designer**: Recommended Version 8.58+
- **Access**: Ability to export projects to XML
- **Knowledge**: Basic familiarity with PeopleSoft project structure

## 📦 Quick Start

### Option 1: Install from source

```bash
# Clone repository
git clone https://github.com/akanashiro/pyPsPrintProject.git
cd pyPsPrintProject

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Manual dependency installation

```bash
pip install docxtpl>=0.16.0 python-docx>=0.8.11
```

### Verify installation

```bash
python main_cmd.py --help
```

### GUI requeriments
**If you want to use Tkinter UI**
```bash
pip install tkinter  (generally included in Python)
pip install ttkthemes
```

**If you want to use PySide6 UI**
```bash
 pip install PySide6
```


You should see the program help without errors.

## 🚀 Basic Usage

### Generate Word documentation

```bash
python main.py MyProject.xml --template assets/project_template.docx --output MyProject.docx
```

**Requirement:** Word template with Jinja2 variables such as:
- `{{ project_name }}`
- `{{ project_definitions }}`
- `{{ summary }}`

### View all options

```bash
python main.py --help
```

### Usage examples

```bash
# Word with custom template
python main_cmd.py /full/path/project.xml -f docx -t /full/template/my_template.docx -o /output/path/output.docx

# Using GUI (QT interface, fallbacks to Tkinter)
python main.py 

# Explicitly use QT
python mainTk.py

# Explicitly use Tkinter
python mainTk.py
```

### Customize Word templates

Word templates use **Jinja2** for dynamic variables:

```jinja2
{# File: template.docx (edit with Word) #}

Project: {{ project_name }}
Date: {{ generation_date }}
Version: {{ project_version }}

Definitions:
{{ project_definitions }}
```

## 📂 Project Structure

```
pyPsPrintProject/
├── bin                        # Binary programs (Windows only for now)
├── images                     # Screenshots
├── templates                  # Document template
└── src                        # Source files
```

### Data flow

```mermaid
graph LR
    A([Read file.xml]) --> B[projectParser.py XML parser] --> D[projectDocGen.py generator] --> E([Write file.md or file.docx])
```

## 📊 Supported Definitions
Read [CHANGELOG.md](CHANGELOG.md)

![ae](images/ae.png)

For partially supported and not supporte definitions, go to CHANGELOG.md

## ⚠️ Known Limitations

### Empty definitions
If the XML contains definitions with a name but empty content, they may not be processed correctly.

**Solution:** Verify that the export is complete in Application Designer.

### Nested objects without parent
Some objects depend on the parent (ex: xlat depends on Field). If the parent is not exported, the nested object does not appear.

**Solution:** Include the parent object in the export.

### Application Engine - Actions without Section
AE actions are only documented if their parent section is included.

**Solution:** Export the complete AE section, not just the actions.

### PS Query
It doesn't build SQL definition from PS Query object (need some help with that)

### English only
Currently the tool only generates documentation in English.


## 🐛 Troubleshooting

### DOCX document comes out blank
**Cause:** If you edited template, it may not not have Jinja2 variables or they are incorrectly named.

**Solution:**
1. Edit template in Word
2. Add fields like: `{{ project_name }}`, `{{ definitions }}`
3. Save and run again

---

### Some objects do not appear in the output
**Cause:** Object exists but is empty, or parent is missing.

**Solution:**
1. Verify in Application Designer that the object exists
2. Include the parent object if it depends on another
3. See "Known Limitations" section

---

### Application Engine comes out incomplete
**Cause:** AE section missing from XML.

**Solution:**
```bash
# Make sure to export the complete AE section
# In Application Designer: Project → Tools → Export
# Select the entire AE section
```

---

### Generic error message or crash
1. Verify that the XML is valid (well-formed)
2. Try with a smaller project first

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

The project is freely available for commercial, personal and educational use.

---

## 🙏 Acknowledgments

- Partners at work

---

**Use in production?**
Not 100% functional but usable.
This is a hobbyist project, expect some regressions.