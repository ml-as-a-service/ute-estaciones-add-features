# Consulta Geográfica de Estaciones Hidrometeorológicas.

Desde la pagina [https://apps.ute.com.uy/SgePublico/MapaEstHid.aspx](https://apps.ute.com.uy/SgePublico/MapaEstHid.aspx) 
extraemos la información de las Estaciones Hidrometeorológicas. 
Para lo cual utilizaremos los paquetes:
 - **Request**: permitirá realizar peticiones HTTP, FTP, etc
 - **BeautifulSoup**:  librería Python que permite extraer información de contenido en formato HTML o XML 
 - **Pandas**: es una librería de Python especializada en el manejo y análisis de estructuras de datos

Gráficamente:

![ValidacionProductosSatelitales](assets/img/ValidacionProductosSatelitales.jpg "Diagrama del proceso.")

Tutorial en Youtube:

[![Tutorial Youtube https://youtu.be/KswiP9BXwug ](https://img.youtube.com/vi/KswiP9BXwug/0.jpg)](https://www.youtube.com/watch?v=KswiP9BXwug)



## Instalación de dependencias
Instalamos las librerias dependientes desde requirements.txt

```bash
pip3 install -r requirements.txt
```

## Ejecutar
Al ejecutar el comando 

```bash
python3 run.py
```
Se procederá a:
 - crear la estructura de directorios
 - descargar el archivo fuente en la carpeta tmp/download
 - exportar la información de las estaciones que se encuentran en el archivo a csv, el mismo se guardara en **./data/MapaEstHid.csv**


