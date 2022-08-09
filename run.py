import functions as fx
# -----------------------------------------------------------------------------
# Inicializamos la estructura de carpetas
fx.init()

# -----------------------------------------------------------------------------
# Bajamos la pagina en tmp/download/MapaEstHid.aspx utilizando requests
url = "https://raw.githubusercontent.com/ml-as-a-service/ute-estaciones-geoloc/main/data/MapaEstHid.csv"
file_path = fx.download(url)

# -----------------------------------------------------------------------------
# Agregamos la altitud a las estaciones
estaciones = fx.addAltitud(file_path)

# -----------------------------------------------------------------------------
# Exportamos las estaciones a CSV utilizando pandas
file_name_csv = "MapaEstHid_Altitud.csv"
file_path_csv = fx.dir_data+file_name_csv
fx.export_to_csv(estaciones, file_path_csv)
