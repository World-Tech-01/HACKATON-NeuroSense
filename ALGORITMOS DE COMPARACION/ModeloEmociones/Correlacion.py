import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

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

correlaciones = pd.DataFrame(X)
correlaciones['emocion'] = y_encoded

correlacion_matrix = correlaciones.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlacion_matrix[['emocion']].sort_values(by='emocion', ascending=False), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlación entre las características y la variable objetivo (emocion)")
plt.show()

print("\n🔍 Correlaciones más altas con la variable objetivo 'emocion':")
print(correlacion_matrix['emocion'].sort_values(ascending=False))
print(df['emocion'].value_counts())