# ===================== 1. IMPORTACIÓN DE LIBRERÍAS =====================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# ===================== 2. CARGA DEL DATASET =====================
df = pd.read_csv("WineQT.csv")

print("\nPrimeras filas del dataset:")
print(df.head())

print(f"\nCantidad total de vinos: {len(df)}")

# ===================== 3. ANÁLISIS EXPLORATORIO DE DATOS (EDA) =====================

# Visualización correcta de todos los vinos
plt.figure(figsize=(8,5))
ax = sns.countplot(x='quality', data=df)
plt.title("Distribución de la calidad de los vinos (total del dataset)")
plt.xlabel("Nivel de calidad")
plt.ylabel("Cantidad de vinos")

# Mostrar los valores encima de cada barra
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', padding=2)

plt.show()

print("\nConteo exacto de vinos por calidad:")
print(df['quality'].value_counts())
print(f"\nTotal de vinos en el dataset: {len(df)}")
