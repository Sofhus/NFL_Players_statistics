import sys
import os

# Agregar el directorio principal a sys.path para que se pueda encontrar Config.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ahora se puede importar Config
from Config import get_data

# Definir la consulta SQL muestra todos los datos de la tabla Teams
query = "SELECT * FROM Teams"

# Ejecutar la consulta
df = get_data(query)

# Imprimir los resultados
if df.empty:
    print("La tabla 'Teams' está vacía.")
else:
    print(df)


print("----------------------------------------------------------------------------------------")

# Definir la consulta SQL muestra todos los datos de la tabla Type
query = "SELECT * FROM Type"

# Ejecutar la consulta
df = get_data(query)

# Imprimir los resultados
if df.empty:
    print("La tabla 'Type' está vacía.")
else:
    print(df)

print("----------------------------------------------------------------------------------------")

# Definir la consulta SQL muestra todos los datos de la tabla Type
query = "SELECT * FROM Seasons GROUP BY Anio"

# Ejecutar la consulta
df = get_data(query)

# Imprimir los resultados
if df.empty:
    print("La tabla 'Seasons' está vacía.")
else:
    print(df)

print("----------------------------------------------------------------------------------------")

# Definir la consulta SQL muestra todos los datos de la tabla Type
query = "SELECT * FROM Player"

# Ejecutar la consulta
df = get_data(query)

# Imprimir los resultados
if df.empty:
    print("La tabla 'Player' está vacía.")
else:
    print(df)