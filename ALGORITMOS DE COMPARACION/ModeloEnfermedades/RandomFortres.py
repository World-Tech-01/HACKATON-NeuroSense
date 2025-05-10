import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, accuracy_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE 
import numpy as np

df = pd.read_csv("C:/Users/Patito/Documents/datasets/datasets/eeg.csv")

filtro = ["Anxiety disorder", "Healthy control", "Mood disorder", "Schizophrenia", "Addictive disorder"]
df_filtered = df[df['main.disorder'].isin(filtro)]
df_filtered = df_filtered[df_filtered["age"] <= 30]

le_sex = LabelEncoder()
le_disorder = LabelEncoder()
df_filtered['sex'] = le_sex.fit_transform(df_filtered['sex'])
df_filtered['main.disorder'] = le_disorder.fit_transform(df_filtered['main.disorder'])

X = df_filtered.drop('main.disorder', axis=1)
y = df_filtered['main.disorder']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance = explained_variance_ratio.cumsum()
n_components_ideal = (cumulative_variance >= 0.95).argmax() + 1
print(f"El número ideal de componentes para explicar al menos el 95% de la varianza es: {n_components_ideal}")

pca = PCA(n_components=n_components_ideal)
X_pca_ideal = pca.fit_transform(X_scaled)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_pca_ideal, y)


X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42, stratify=y_resampled)


rf_classifier = RandomForestClassifier(
    n_estimators=100,  
    criterion='gini',  
    max_depth=None,   
    min_samples_split=2, 
    min_samples_leaf=1,
    max_features='sqrt', 
    random_state=42,   
    n_jobs=-1,          
    class_weight='balanced'  
)
rf_classifier.fit(X_train, y_train)


y_pred = rf_classifier.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(rf_classifier, X_resampled, y_resampled, cv=skf, scoring='f1_macro')
print("F1 macro promedio con validación cruzada:", scores.mean())

importances = rf_classifier.feature_importances_
indices = np.argsort(importances)[::-1]
print("\nImportancia de las características (componentes principales):")
for f in range(X_train.shape[1]):
    print(f"{f + 1}. Componente {indices[f]}: {importances[indices[f]]:.4f}")


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)

class_metrics = {k: v for k, v in report.items() if k.isdigit()}

df_metrics = pd.DataFrame(class_metrics).T
df_metrics = df_metrics[['precision', 'recall', 'f1-score']]

class_names = le_disorder.inverse_transform([int(i) for i in df_metrics.index])
df_metrics.index = class_names


df_metrics.plot(kind='bar', figsize=(10, 6))
plt.title("Métricas por Clase - Random Forest")
plt.ylabel("Valor")
plt.ylim(0, 1)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


general_metrics = {
    'Macro Promedio': report['macro avg'],
    'Promedio Ponderado': report['weighted avg']
}


df_general = pd.DataFrame(general_metrics).T[['precision', 'recall', 'f1-score']]

df_general.plot(kind='bar', figsize=(8, 5), color=["#4c72b0", "#55a868", "#c44e52"])
plt.title("Métricas Generales del Modelo - Random Forest")
plt.ylabel("Valor")
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


general_df = pd.DataFrame({
    'Métrica': ['Precisión', 'Recall', 'F1-score'],
    'Macro Promedio': [
        general_metrics['Macro Promedio']['precision'],
        general_metrics['Macro Promedio']['recall'],
        general_metrics['Macro Promedio']['f1-score']
    ],
    'Promedio Ponderado': [
        general_metrics['Promedio Ponderado']['precision'],
        general_metrics['Promedio Ponderado']['recall'],
        general_metrics['Promedio Ponderado']['f1-score']
    ]
})
print(general_df)