import sqlite3
import gzip

# Conecta a la base de datos
bdd = sqlite3.connect("passwords.db")

# Exporta la base de datos a un archivo
with open("data/passwords.sql", "w", encoding="utf-8") as f:
    for linea in bdd.iterdump():
        f.write('%s\n' % linea)

# Cierra la conexión a la base de datos
bdd.close()

# Comprime el archivo
with open("passwords.sql", "rb") as f_in, gzip.open("passwords.sql.gz", "wb") as f_out:
    f_out.writelines(f_in)

# Elimina el archivo sin comprimir si deseas
# import os
# os.remove("passwords.sql")
