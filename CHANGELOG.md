# Changelog

This file logs major changes made in this project

## Definitions that are partially or not supported

### Partially supported ⚠️

| Object | Limitation | Workaround |
|---|---|---|
| **App Package** | Doesn't generate App Package info | Document manually |
| **Page** | Doesn't generate any image | Document manually |
| **PS Query** | Doesn't distinguish public/private. Doesn't generate SQL| Document manually |
| **REST Service** | Only Operation, not other types | Document manually  |
| **App Engine Steps** | Requires parent section in XML | Export complete section |
| **Record Translate** | Depends on parent Field | Include Field in export |

### Not supported ❌

| Object | Reason | Alternative |
|---|---|---|
| **CSS Styles** | Not relevant for documentation | Document manually |
| **Icons** | Not relevant for documentation | Document manually |


---
# Changelog

## [1.2.0] - 2026-04-29
_A lot of changes_

### Added
- Windows binaries availabe for download in bin directory. I compiled it in two different toolkits.
  - PrintPrjTk.exe (Tkinter toolkit)
  - PrintPrjQt.exe (QT PySide toolkit)

### Changed
- Reordered directory structure

## [1.1.0] - 2026-04-27

_Step forward to usability_

### Added
- Xlats
- Roles
- Component Record PeopleCode
- Content references
- GUI in Tkinter and PySide with the help of AI!
  - PySide6 (default toolkit) uses the following styles:
    - windowsvista in Windows
    - macOS in macOS
    - Fusion in Linux.
  - Tkinter (fallback toolkit) uses the following styles:
    - vista in Windows
    - aqua in macOS
    - arc / breeze / clam in Linux. If you install _ttkthemes_ via  ```pip install python3-ttkhemes``` improves the visual in Linux using Arc or Breeze

### Changed
- Standardize name conventions in class attributes
- Record Field now shows default label
- Updated ```project_template.docx```

### Pending
- Application Package Definition
- Update MD printing

## [1.0.2] - 2026-04-25

### Fixed
- Import call in ProjectParser.py

## [1.0.1] - 2026-04-23

### Added
- fixRootTag() added: Add a <root> tag that wraps the XML if it isn't present.

### Changed
- Renamed projDocGen.py to projectDocGen.py
- Renamed helperFunctions.py to helpFunctions.py

### Fixed
- decodeFieldType() applied in projectParse.py

## [1.0.0] - 2026-04-19
- Main release
- Initial functionality