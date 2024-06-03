import pandas as pd

# Ruta del archivo CSV
file_path = 'csv de la encuesta/Encuesta sobre la Industria 4.0 en las MiPymes de Cúcuta, Norte de Santander.csv'
df = pd.read_csv(file_path)

# Info DataFrame
print("Información del DataFrame original:")
print(df.info())

# Eliminar valor nulos"
if 'Nombre de usuario' in df.columns:
    df = df.drop(columns=['Nombre de usuario'])

df_filled = df.fillna("")

# Guardar el nuevo DataFrame en un archivo Excel
output_file_path = 'Dataset_Industria_4.0_MiPymes_Cucuta.xlsx'
df_filled.to_excel(output_file_path, index=False)

print("El nuevo dataset completo se ha guardado en:", output_file_path)
