# pyPsPrintProject

This application helps you to document those PeopleSoft projects exported to a file with Application Designer.
It extracts the definitions found in XML file and loaded them into classes so they can be browsed and dump them into a text file (.md or .docx)

## Definitions that work
* Record Definition
* Field Definition
* Page Definition
* Process Definition
* Job Definition
* SQL Object
* Record PeopleCode
* Component PeopleCode
* Component Record Field PeopleCode
* Application Package PeopleCode
* Application Engine basic information
  * Application Engine PeopleCode
  * Application Engine SQL
    * Do Select
    * Do When
  * Call Section
* Message Catalog
* File Layout

## What partially works
* Only REST Service Operation
* Menu doesn't show BarItem + BarPanel yet

## To-do
* Components
* Component PeopleCode
* Translate values
* File Layouts
* Application Engine:
  * Other SQL events
  * Temporary Table list
* Remaining definitions found in the XML file
* Message Catalog long explanation
* Roles
* Permission Lists
* Content Reference
* Application Package
* Index
* File Layout: I couldn't figure out which tag is the output file format. Maybe "eFormat"?

## Won't work
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

### Application could break in certain scenarios:
There are some projects that could crash the applications like those with object definitions but the object is empty.


## How to run:
```
    >> python main.py MyProject.xml --format md [--output MyProject.md]
    >> python main.py MyProject.xml -f md [-o MyProject.md]
    >> python main.py MyProject.xml --format docx --template MyTemplate.docx [--output MyProject.docx]
    >> python main.py MyProject.xml --ft docx -t MyTemplate.docx [-o MyProject.docx]
```


**Note:**
1. This is my hobbyst project and done in my spare time. Expect some rough edges..
2. I release this application under MIT license so all the PeopleSoft community could benefit from this tool.