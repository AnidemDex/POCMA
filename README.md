[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![last-commit](https://img.shields.io/github/last-commit/dastmema/POCMA)](#)
[![License](https://img.shields.io/github/license/dastmema/POCMA)](#)
[![Size](https://img.shields.io/github/repo-size/dastmema/POCMA)](#)
# POCMA
> Programa Orientado a la Celda de Manufactura Automatizada  
  
## Descripción
Aqui se alojará el programa responsable del manejo de la celda de manufactura del Centro de Automatización de Procesos.
  
El objetivo es simple: reimplementar el sistema de control actual **_reestructurando_** todo su código fuente.

##Características
###### Hecho en Python 3  
Asi los estudiantes pueden revisar el código y aprender del mismo.

###### Diseñado para ser rapido y eficiente.  
Su interfaz gráfica fue pensada para ser trabajada de forma modular. Esto quiere decir que si bien puede manejar toda la celda de manufactura al unísono como en el mejor concierto de Paganini, tambien puede manejar _cualquier_ parte de la celda de forma independiente.

###### Conservando lo mejor de su predecesor
Ciertas cosas (como protocolos de comunicación) se conservan intactas de la versión original con el fin de no estropear el estandar actualmente manejado en la celda de manufactura.  
Esto, por supuesto, puede ser modificado en cualquier momento si el operario asi lo desea.

###### Con su propia implementación para dispositivos moviles
Perfectamente controlable a traves del protocolo de comunicación `OPC-UA`, posee una _aplicación_ en linea dedicada a este software, que le prooverá datos relevantes sobre la celda y el control de la misma, sin necesidad de usar la terminal central donde se ejecuta el _cerebro de la maquina_.

## Cosas por hacer
> Porque todo suena muy bonito pero no es real... Aun.

##### Librerias
 - [ ] RVM1
 - [ ] Torno
 - [ ] Fresadora
##### Interfaz
 - [ ] Diseño
 - [ ] Implementación
##### Módulo de comunicación
 - [ ] Servidores
