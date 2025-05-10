import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/Patito/Documents/datasets/datasets/deap_processed_with_emotions.csv")


X = df.drop(columns=['valence', 'arousal', 'participant'], errors='ignore')
X = X.select_dtypes(include=[np.number])  # Solo columnas numéricas
y_valence = df['valence']
y_arousal = df['arousal']


X_train, X_test, yv_train, yv_test = train_test_split(X, y_valence, test_size=0.2, random_state=42)
_, _, ya_train, ya_test = train_test_split(X, y_arousal, test_size=0.2, random_state=42)


model_valence = DecisionTreeRegressor(max_depth=5, min_samples_leaf=5, random_state=42)
model_arousal = DecisionTreeRegressor(max_depth=5, min_samples_leaf=5, random_state=42)

model_valence.fit(X_train, yv_train)
model_arousal.fit(X_train, ya_train)


pred_valence = model_valence.predict(X_test)
pred_arousal = model_arousal.predict(X_test)


print("\n📈 Resultados para 'valence':")
print(f"MSE: {mean_squared_error(yv_test, pred_valence):.2f}")
print(f"R2 : {r2_score(yv_test, pred_valence):.2f}")

print("\n📈 Resultados para 'arousal':")
print(f"MSE: {mean_squared_error(ya_test, pred_arousal):.2f}")
print(f"R2 : {r2_score(ya_test, pred_arousal):.2f}")


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(yv_test, pred_valence, alpha=0.6)
plt.xlabel("Valence real")
plt.ylabel("Valence predicho")
plt.title("Predicción de Valence")

plt.subplot(1, 2, 2)
plt.scatter(ya_test, pred_arousal, alpha=0.6)
plt.xlabel("Arousal real")
plt.ylabel("Arousal predicho")
plt.title("Predicción de Arousal")

plt.tight_layout()
plt.show()
