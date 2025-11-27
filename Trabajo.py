import tkinter as tk                 # Importa la librería Tkinter para crear interfaces gráficas
from tkinter import messagebox        # Importa messagebox para mostrar mensajes emergentes

# trabajos
Trabajos = [                          # Lista de trabajos disponibles
    {"titulo": "Desarrollador Python", "habilidades": ["python", "java", "C++", "paciente"], "ciudad": "Cali"},
    {"titulo": "Analista de Datos", "habilidades": ["excel", "python", "psicologia", "paciente", "amable"], "ciudad": "Bogota"},
    {"titulo": "Soporte Técnico", "habilidades": ["soporte", "trabajoen equipo", "programador"], "ciudad": "Medellin"},
]

def recomendar(habs, ciudad):          # Define una función que recibe habilidades y ciudad del usuario
    habs = [h.strip().lower() for h in habs.split(",") if h.strip()]  # Convierte las habilidades a una lista limpia en minúsculas
    ciudad = ciudad.lower().strip()    # Limpia y convierte la ciudad a minúsculas
    resultados = []                    # Lista donde se guardarán los trabajos con puntuación

    for job in Trabajos:               # Recorre cada trabajo en la lista
        score = 0                      # Inicializa el puntaje de coincidencia
    
        for h in habs:                 # Recorre las habilidades ingresadas por el usuario
            if h in job["habilidades"]: # Si la habilidad coincide con el trabajo
                score += 1              # Aumenta el puntaje

        if ciudad and ciudad in job["ciudad"].lower():  # Si la ciudad también coincide
            score += 1

        if score > 0:                  # Si el puntaje es mayor a 0, se considera un match
            resultados.append((score, job))  # Guarda el puntaje junto al trabajo

    resultados.sort(reverse=True, key=lambda x: x[0])  # Ordena por puntaje descendente
    return resultados                # Devuelve la lista de resultados



root = tk.Tk()                       # Crea la ventana principal
root.title("Recomendador simple")    # Título de la ventana
root.geometry("400x400")             # Tamaño de la ventana

tk.Label(root, text="Habilidades (coma):").pack()  # Etiqueta para pedir habilidades
entry_habs = tk.Entry(root)          # Campo de texto para habilidades
entry_habs.pack()

tk.Label(root, text="Ciudad:").pack() # Etiqueta para pedir ciudad
entry_city = tk.Entry(root)           # Campo de texto para ciudad
entry_city.pack()

result_box = tk.Listbox(root, width=50) # Caja donde se mostrarán los resultados
result_box.pack(pady=10)

def on_recomendar():                 # Función que se ejecuta cuando se presiona el botón
    result_box.delete(0, tk.END)      # Limpia resultados anteriores
    habs = entry_habs.get()           # Obtiene el texto de habilidades
    city = entry_city.get()           # Obtiene el texto de ciudad

    resultados = recomendar(habs, city)  # Llama la función recomendadora
    if not resultados:                # Si no hubo coincidencias
        result_box.insert(tk.END, "Sin coincidencias.")  # Lo muestra
        return

    for score, job in resultados:     # Muestra cada trabajo encontrado
        result_box.insert(tk.END, f"{job['titulo']} — score {score}")

btn = tk.Button(root, text="Recomendar", command=on_recomendar)  # Botón para iniciar la recomendación
btn.pack(pady=30)

root.mainloop()                      # Inicia el ciclo principal de la interfaz