import matplotlib.pyplot as plt

# Datos para el gráfico
categorias = ['Presupuesto', 'Monto Alcanzado']
pesos = [7700000, 7743696.89]
porcentajes = [100, 100.57]

# Crear figura y eje principal
fig, ax1 = plt.subplots(figsize=(8, 5))

# Gráfico de barras para "Pesos"
ax1.bar(categorias, pesos, color='blue', alpha=0.6, label='Pesos')
ax1.set_ylabel('Pesos', fontsize=12, color='blue')
ax1.set_title('Comparación de Pesos vs Porcentaje (Presupuesto vs Monto Alcanzado)', fontsize=14)
ax1.tick_params(axis='y', labelcolor='blue')

# Crear un segundo eje Y para "Porcentajes"
ax2 = ax1.twinx()
ax2.plot(categorias, porcentajes, color='green', marker='o', label='Porcentaje')
ax2.set_ylabel('Porcentaje (%)', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Ajustar diseño y mostrar el gráfico
fig.tight_layout()
plt.show()
