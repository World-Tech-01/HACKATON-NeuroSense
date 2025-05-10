import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import plot_tree
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/Patito/Documents/datasets/datasets/deap_processed_with_emotions.csv")


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


df['emocion'] = df.apply(lambda row: clasificar_emocion(row['valence'], row['arousal']), axis=1)
df = df[df['emocion'] != 'Neutral']  

elegidos = [1, 2, 11, 3, 17, 4, 12, 13, 5, 18, 6, 14, 15, 7, 19, 8, 16, 9, 10]
df = df[df["channel"].isin(elegidos)]

X = df.drop(columns=['valence', 'arousal', 'emocion', 'participant'], errors='ignore')
X = X.select_dtypes(include=[np.number])
y = df['emocion']

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, stratify=y_encoded, random_state=42)

dt_clf = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    class_weight='balanced', 
    random_state=42
)

dt_clf.fit(X_train, y_train)

y_pred = dt_clf.predict(X_test)

y_test_labels = encoder.inverse_transform(y_test)
y_pred_labels = encoder.inverse_transform(y_pred)
class_names = encoder.classes_


print("\n🔍 Classification Report:")
print(classification_report(y_test_labels, y_pred_labels))


plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test_labels, y_pred_labels, labels=class_names)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
            xticklabels=class_names, 
            yticklabels=class_names)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix - Árbol de Decisión")
plt.show()


plt.figure(figsize=(20, 10))
plot_tree(dt_clf,
          feature_names=X.columns,
          class_names=class_names,
          filled=True,
          rounded=True,
          max_depth=3)
plt.title("Estructura del Árbol de Decisión")
plt.show()

print("\n🔍 Importancia de características:")
importancias = dt_clf.feature_importances_
indices = np.argsort(importancias)[::-1]
n_features = min(10, len(importancias))
indices = indices[:n_features]

plt.figure(figsize=(10, 6))
plt.title(f"Top {n_features} Características más Importantes")
plt.bar(range(n_features), importancias[indices], align='center')
plt.xticks(range(n_features), X.columns[indices], rotation=45, ha='right')
plt.ylabel("Importancia")
plt.tight_layout()
plt.show()

y_proba = dt_clf.predict_proba(X_test)

for i in range(1):
    print(f"\nEjemplo {i+1}:")
    for clase, prob in zip(class_names, y_proba[i]):
        print(f"  {clase}: {prob:.2f}")

from sklearn.metrics import classification_report

# Obtener el reporte en formato de diccionario
report = classification_report(y_test_labels, y_pred_labels, output_dict=True, zero_division=0)

# Extraer métricas generales
general_metrics = report['weighted avg']  # también puedes probar 'macro avg' o 'micro avg'

print("\n🔎 Métricas Generales (weighted avg):")
for metric in ['precision', 'recall', 'f1-score']:
    print(f"{metric.capitalize()}: {general_metrics[metric]:.2f}")


# Crear DataFrame para graficar
general_df = pd.DataFrame({
    'Métrica': ['Precisión', 'Recall', 'F1-score'],
    'Valor': [general_metrics['precision'], general_metrics['recall'], general_metrics['f1-score']]
})

# Graficar
plt.figure(figsize=(6, 5))
sns.barplot(data=general_df, x='Métrica', y='Valor', palette='viridis')
plt.title("Métricas Generales del Modelo (Promedio Ponderado)")
plt.ylim(0, 1)
plt.ylabel("Valor")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
