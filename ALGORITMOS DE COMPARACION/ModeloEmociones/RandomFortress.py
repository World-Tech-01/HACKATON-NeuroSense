import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
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

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, stratify=y_encoded, random_state=100)

rf_clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=3,
    random_state=42
)

rf_clf.fit(X_train, y_train)
y_pred = rf_clf.predict(X_test)

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
plt.title("Confusion Matrix - Random Forest")
plt.show()

importancias = rf_clf.feature_importances_
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

y_proba = rf_clf.predict_proba(X_test)

for i in range(5):
    print(f"\nEjemplo {i+1}:")
    for clase, prob in zip(class_names, y_proba[i]):
        print(f"  {clase}: {prob:.2f}")
