import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("C:/Users/Patito/Documents/datasets/datasets/deap_processed_with_emotions.csv")

# Función para clasificar la emoción
def clasificar_emocion(valence, arousal):
    if valence >= 6 and arousal >= 6:
        return 'Feliz'
    elif valence <= 3 and arousal <= 4:
        return 'Tristeza'
    elif valence <= 3 and arousal >= 6:
        return 'Enojo'
    elif valence <= 5 and 4 < arousal < 6:
        return 'Miedo'
    else:
        return 'Neutral'

# Aplicar la clasificación de emociones
df['emocion'] = df.apply(lambda row: clasificar_emocion(row['valence'], row['arousal']), axis=1)
df = df[df['emocion'] != 'Neutral']  # Eliminar la clase 'Neutral'

# Filtrar canales
elegidos = [1, 2, 11, 3, 17, 4, 12, 13, 5, 18, 6, 14, 15, 7, 19, 8, 16, 9, 10]
df = df[df["channel"].isin(elegidos)]

# Definir las características y la variable objetivo
X = df.drop(columns=['valence', 'arousal', 'emocion', 'participant'], errors='ignore')
X = X.select_dtypes(include=[np.number])
y = df['emocion']

# Codificar las etiquetas de las emociones
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, stratify=y_encoded, random_state=42)

# Crear el clasificador de Regresión Logística con ponderación de clases balanceada
log_reg = LogisticRegression(
    class_weight='balanced',  # Añadir la ponderación de clases
    random_state=42,
    max_iter=1000  # Asegurarse de que el modelo converja
)

# Entrenar el modelo
log_reg.fit(X_train, y_train)

# Hacer predicciones
y_pred = log_reg.predict(X_test)

# Descodificar las etiquetas predichas y reales
y_test_labels = encoder.inverse_transform(y_test)
y_pred_labels = encoder.inverse_transform(y_pred)
class_names = encoder.classes_

# Imprimir el reporte de clasificación
print("\n🔍 Classification Report:")
print(classification_report(y_test_labels, y_pred_labels))

# Mostrar la matriz de confusión
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test_labels, y_pred_labels, labels=class_names)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
            xticklabels=class_names, 
            yticklabels=class_names)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix - Regresión Logística")
plt.show()

# Mostrar las probabilidades de las predicciones
y_proba = log_reg.predict_proba(X_test)

# Mostrar las probabilidades para algunos ejemplos
for i in range(5):
    print(f"\nEjemplo {i+1}:")
    for clase, prob in zip(class_names, y_proba[i]):
        print(f"  {clase}: {prob:.2f}")
