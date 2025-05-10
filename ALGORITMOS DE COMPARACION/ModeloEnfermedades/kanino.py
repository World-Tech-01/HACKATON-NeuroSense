import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("C:/Users/Patito/Documents/datasets/datasets/eeg.csv")

filtro = ["Anxiety disorder", "Healthy control", "Mood disorder", "Schizophrenia", "Addictive disorder"]
df_filtered = df[df['main.disorder'].isin(filtro)]
df_filtered = df[df["age"] <=30]
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


X_train, X_test, y_train, y_test = train_test_split(X_pca_ideal, y, test_size=0.3, random_state=42)


knn = KNeighborsClassifier(n_neighbors=5)  
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
