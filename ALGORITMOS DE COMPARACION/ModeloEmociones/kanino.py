import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
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

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, stratify=y_encoded, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

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
plt.title("Confusion Matrix - KNN")
plt.show()

y_proba = knn.predict_proba(X_test)

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])


param_grid = {
    'knn__n_neighbors': list(range(1, 31))  
}

grid_search = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

print(f"Mejor número de vecinos: {grid_search.best_params_['knn__n_neighbors']}")
print(f"Precisión en validación cruzada: {grid_search.best_score_:.4f}")
