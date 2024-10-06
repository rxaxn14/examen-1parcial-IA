import csv
import matplotlib.pyplot as plt


def cargar_dataset(ruta):
    with open(ruta, mode='r') as file:
        csvreader = csv.reader(file)
        headers = next(csvreader)  # Saltar encabezados
        data = [row for row in csvreader]
    return headers, data


def extraer_columna(data, col_index):
    return [float(fila[col_index]) for fila in data if fila[col_index]]


def percentil(data, p):
    data_sorted = sorted(data)
    n = len(data_sorted)
    k = (n - 1) * (p / 100)
    f = int(k)
    c = k - f
    if f + 1 < n:
        return data_sorted[f] + (c * (data_sorted[f + 1] - data_sorted[f]))
    else:
        return data_sorted[f]


def cuartiles(data):
    q1 = percentil(data, 25)
    q2 = percentil(data, 50)  # Mediana
    q3 = percentil(data, 75)
    return q1, q2, q3


def graficar_distribucion(data, titulo, xlabel):
    plt.hist(data, bins=10, color='skyblue', alpha=0.7)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()


ruta_dataset = 'C:/Users/ROXANA CASTILLO/Desktop/354/gym_members_exercise_tracking.csv'

headers, dataset = cargar_dataset(ruta_dataset)

columnas_numericas = {
    'Age': 0,
    'Weight (kg)': 2,
    'Height (m)': 3,
    'Max_BPM': 4,
    'Avg_BPM': 5,
    'Resting_BPM': 6,
    'Session_Duration (hours)': 7,
    'Calories_Burned': 8,
    'Fat_Percentage': 10,
    'Water_Intake (liters)': 11,
    'Workout_Frequency (days/week)': 12,
    'BMI': 13
}

for nombre_columna, index in columnas_numericas.items():
    datos_columna = extraer_columna(dataset, index)
    q1, q2, q3 = cuartiles(datos_columna)
    print(f"Cuartiles de {nombre_columna}: Q1={q1}, Mediana (Q2)={q2}, Q3={q3}")

    graficar_distribucion(datos_columna, f'Distribución de {nombre_columna}', nombre_columna)
