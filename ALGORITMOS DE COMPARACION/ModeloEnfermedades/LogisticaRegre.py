import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, accuracy_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE 


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


log_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000, random_state=42)
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(log_reg, X_resampled, y_resampled, cv=skf, scoring='f1_macro')
print("F1 macro promedio con validación cruzada:", scores.mean())