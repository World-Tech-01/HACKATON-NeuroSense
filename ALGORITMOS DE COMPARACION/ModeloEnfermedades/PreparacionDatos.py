import pandas as pd

df = pd.read_csv('C:/Users/Patito/Documents/datasets/datasets/EEG.machinelearing_data_BRMH.csv')


bandas = ['delta', 'theta', 'alpha', 'beta', 'gamma']
columnas_bandas = [
    col for col in df.columns 
    if any(banda in col.lower() for banda in bandas) and 'highbeta' not in col.lower()
]

df_resultado = pd.DataFrame()

for banda in bandas:
    cols_banda = [col for col in columnas_bandas if banda in col.lower()]
    datos_banda = df[cols_banda]
    
    df_resultado[f'{banda}_mean'] = datos_banda.mean(axis=1)
    df_resultado[f'{banda}_min'] = datos_banda.min(axis=1)
    df_resultado[f'{banda}_max'] = datos_banda.max(axis=1)
    df_resultado[f'{banda}_std'] = datos_banda.std(axis=1)

df_resultado['age'] = df['age']
df_resultado['sex'] = df['sex']
df_resultado['main.disorder'] = df['main.disorder']

print(df_resultado.columns)


output_path = "eeg.csv"
df_resultado.to_csv(output_path, index=False)
print(f"\nProcesamiento completado. Datos guardados en '{output_path}'")


