import pandas as pd
import numpy as np

ruta_archivo = 'confi gataf (version 2).xlsx'
hoja = 'SAP'  # Opcional, si quieres especificar el nombre de la hoja
df = pd.read_excel(ruta_archivo, sheet_name=hoja)
columnas_a_conservar = ['Inicio avería', 'FLOTA', 'ATA']
columnas_a_eliminar = df.columns[~df.columns.isin(columnas_a_conservar)]
df = df.drop(columnas_a_eliminar, axis=1)
ruta_guardado = 'dataBaseAVATION_NAVY.csv'
columnas={'Inicio avería':'Date', 'FLOTA': 'Aeronave', 'ATA':'Sistema'}
df=df.rename(columns=columnas)
df.to_csv(ruta_guardado, index=False)