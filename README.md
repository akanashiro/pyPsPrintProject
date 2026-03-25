# pyPsPrintProject

Esta aplicación ayudar a documentar proyectos hechos en PeopleSoft y exportados a archivo Application Designer.
Extrae las definiciones que se encuentren en el XML y las vuelca a el objeto _projectObj_ de la clase _PSProject_

Las definiciones guardadas en el objeto son:
* Records
* Fields
* Pages
* Processes
* SQL objects
* Record PeopleCode
* Application Package PeopleCode

To-do:
* Resto de las definiciones que se encuentren en un proyecto.
* Volcar las definiciones a formato .docx.

La sintaxis de ejecución
```
    python main.py MiProyecto.xml --format md [--output MiProyecto.md]
    python main.py MiProyecto.xml -f md [-o MiProyecto.md]
    python main.py MiProyecto.xml --format docx --template plantilla.docx [--output MiProyecto.docx]
    python main.py MiProyecto.xml --ft docx -t plantilla.docx [-o MiProyecto.docx]
```

**Nota:**
1. Este es mi proyecto hobby por lo que está hecho en mis tiempos libres.
2. Lo libero bajo licencia MIT para que cualquiera pueda beneficiarse de esta herramienta.