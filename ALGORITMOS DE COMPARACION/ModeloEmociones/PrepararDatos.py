import pandas as pd
import numpy as np
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GroupShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Cargar y unificar datos
files = sorted(glob.glob("C:/Users/Patito/Documents/datasets/datasets/s*.csv"))
all_data = pd.concat(
    [pd.read_csv(f).assign(participant=os.path.basename(f)) for f in files],
    ignore_index=True
)

# 2. Normalización por participante
print("\nNormalizando datos por participante...")
features = ['mean', 'std', 'min', 'max']

for participant in all_data['participant'].unique():
    mask = all_data['participant'] == participant
    scaler = StandardScaler()
    all_data.loc[mask, features] = scaler.fit_transform(all_data.loc[mask, features])

# 3. Mapeo de emociones
print("\nCreando etiquetas de emociones...")

def map_emotion(row):
    valence, arousal, dominance = row["valence"], row["arousal"], row["dominance"]
    
    HIGH_V = 7
    LOW_V = 3
    HIGH_A = 6
    LOW_A = 4
    HIGH_D = 6
    LOW_D = 4
    
    if valence >= HIGH_V and arousal >= HIGH_A and dominance >= HIGH_D:
        return "Feliz"
    elif valence >= HIGH_V and arousal <= LOW_A:
        return "Relajado"
    elif valence <= LOW_V and arousal <= LOW_A and dominance <= LOW_D:
        return "Triste"
    elif valence <= LOW_V and arousal >= HIGH_A and dominance <= LOW_D:
        return "Ansiedad"
    elif valence <= LOW_V and arousal >= HIGH_A:
        return "Enojado"
    else:
        return "Neutral"

all_data['emotion'] = all_data.apply(map_emotion, axis=1)

# 4. División train-test (sin balanceo)
print("\nDividiendo datos en train y test...")
X = all_data[features]
y = all_data['emotion']
groups = all_data['participant']

splitter = GroupShuffleSplit(test_size=0.2, n_splits=1, random_state=42)
train_idx, test_idx = next(splitter.split(X, y, groups=groups))

X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

# 5. Entrenamiento del modelo (con class_weight para manejar desbalanceo)
print("\nEntrenando modelo Random Forest...")
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced'  # Maneja desbalanceo automáticamente
)
model.fit(X_train, y_train)

# 6. Evaluación
y_pred = model.predict(X_test)
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# 7. Importancia de características
print("\nImportancia de características:")
for feature, importance in zip(features, model.feature_importances_):
    print(f"{feature}: {importance:.3f}")




# 8. Guardar datos procesados
output_path = "deap_processed_with_emotions.csv"
all_data.to_csv(output_path, index=False)
print(f"\nProcesamiento completado. Datos guardados en '{output_path}'")