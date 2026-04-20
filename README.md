# pyPsPrintProject

This application will help you to document those PeopleSoft projects exported to a file with Application Designer.
It extracts the most common definitions found in XML file and loaded them into classes so they can be browsed and dump them into a text file (.md or .docx).

**Note:**
1. This is my hobbyst project and done in my spare time. Expect some rough edges..
2. I release this application under MIT license so all the PeopleSoft community could benefit from this tool.

## Definitions that work
* Field:
  * Field Definition
  * Translate values
* Record:
  * Record Definition
  * Record PeopleCode
  * SQL View for Views
* Page Definition
* Process Definition
* Job Definition
* SQL Object
* File Layout
* PS Query
* BI Publisher Reports
* Message Catalog
* Menu
* Component:
  * Component Definition
  * Component PeopleCode
  * Component Record Field PeopleCode
* Application Package PeopleCode
* Application Engine basic information
  * Application Engine PeopleCode
  * Application Engine SQL
    * Do While
    * Do Select
    * Do When
    * Do Until
  * Call Section
  * Log messages
* Permission Lists

## What partially works but still functional
* Those projects that may contain the name object definition but definition is empty, may not show all information.
* Some definitions are processed nested. Eg: xlat depends on Field parent definition. If that parent definition is not present in project file, it may not be shown.
* Only REST Service Operation.
* Permission Lists: I don't retrieve menu.comp.pages security because the list could be very long
* Application Engine Step.actions are nested, thus if you don't include the Application Engine Section that contains the action.step, they may not be be shown.


## To-do
* Code
  * Clean up code
  * Refactoring
  * Standardize object naming
  * Some things are in Spanish, I should translate them to English
* Improve and complete Markdown rendering 
* PS Query:
  * What is the tag that defines a query is public or private?
  * build SQL from "QdmDefn" rowset
* File Layout: couldn't get the tag that defines the output file format. Maybe "eFormat"?
* Message Catalog: couldn't get long explanation
* Menu: it doesn't show BarItem + BarPanel yet
* Component Record PeopleCode
* Translate values
* BI Publisher Report: list template files
* Roles
* Content Reference
* Application Package definition
* Indices
* Maybe I can get the upgrade action through "eUpgradeAction" tag.
* Remaining definitions found in the XML file...

## Won't do
* PeopleCode Menu
* Other objects like CSS styles or icons

## Warning!!!

### First Steps

You must install som extra packages

```
pip install docxtpl python-docx
```

PeopleSoft XML doesn't come with root tag (don't know why), so you will see something like this.
```XML
<?xml version='1.0'?>
  <!--Warning : Don't edit this file -->
  <instance class="PJM">
    <rowset name="PjmDefn" size="2856" count="1">
      <row>
```

You must open the XML file and add <root> tag before <instance> and the end of the file.
```XML
<?xml version='1.0'?>
<root>
  <!--Warning : Don't edit this file -->
  <instance class="PJM">
    <rowset name="PjmDefn" size="2856" count="1">
      <row>
      ...
</root>
```

### Language
I haven't considered any other language rather than English.

### Application could break in certain scenarios:
There are some projects that could crash the applications like those with object definitions but the object is empty.


## How to run:
```
    >> python main.py MyProject.xml --format md [--output MyProject.md]
    >> python main.py MyProject.xml -f md [-o MyProject.md]
    >> python main.py MyProject.xml --format docx --template MyTemplate.docx [--output MyProject.docx]
    >> python main.py MyProject.xml --ft docx -t MyTemplate.docx [-o MyProject.docx]
```
