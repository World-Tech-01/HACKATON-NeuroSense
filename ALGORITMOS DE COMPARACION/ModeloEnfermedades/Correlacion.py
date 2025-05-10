import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns


df = pd.read_csv("C:/Users/Patito/Documents/datasets/datasets/eeg.csv")

filtro = ["Anxiety disorder", "Healthy control", "Mood disorder", "Schizophrenia", "Addictive disorder"]
df_filtered = df[df['main.disorder'].isin(filtro)]

from sklearn.preprocessing import LabelEncoder
le_sex = LabelEncoder()
le_disorder = LabelEncoder()

df_filtered['sex'] = le_sex.fit_transform(df_filtered['sex'])
df_filtered['main.disorder'] = le_disorder.fit_transform(df_filtered['main.disorder'])

X = df_filtered.drop('main.disorder', axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance = explained_variance_ratio.cumsum()

plt.figure(figsize=(8, 6))
plt.plot(range(1, len(explained_variance_ratio) + 1), cumulative_variance, marker='o', linestyle='--')
plt.title('Explained Variance by PCA Components')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.grid(True)
plt.show()

n_components_ideal = (cumulative_variance >= 0.95).argmax() + 1
print(f"El número ideal de componentes para explicar al menos el 95% de la varianza es: {n_components_ideal}")


pca = PCA(n_components=n_components_ideal)
X_pca_ideal = pca.fit_transform(X_scaled)

correlation_matrix = pd.DataFrame(X_pca_ideal).corr()


plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlación entre los Componentes Principales de PCA")
plt.show()

print(df_filtered['main.disorder'].value_counts())