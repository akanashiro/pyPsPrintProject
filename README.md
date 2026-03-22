# pyPsPrintProject

Esta aplicación ayudar a documentar proyectos hechos en PeopleSoft y exportados a archivo Application Designer.
Extrae las definiciones que se encuentren en el XML y las vuelca a el objeto _projectObj_ de la clase _PSProject_

Las definiciones guardadas en el objeto son:
* records
* fields
* processes

To-do:
* Resto de las definiciones que se encuentren en un proyecto.
* Volcar las definiciones a formato .docx.

La sintaxis de ejecución
```
    python main.py MiProyecto.xml --format md --output MiProyecto.md
```