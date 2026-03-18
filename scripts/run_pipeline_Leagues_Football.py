import subprocess
import time

# Lista de scripts a ejecutar
scripts = ["A_League.py", "BundesLiga.py", "Champions_League.py", "Italia_Serie_A.py", "La_Liga.py", "Liga_Portugal.py", "Ligue_1_France.py", "Premier_League.py", "Super_League_Grecia.py", "NBA.py"]

# Registro del tiempo de inicio
start_time = time.time()

# Lista para almacenar los procesos en ejecución
processes = []

# Inicia cada script como un proceso independiente
for script in scripts:
    print(f"Iniciando {script}...")
    processes.append(subprocess.Popen(["python", script]))



# Espera a que todos los procesos terminen
for process in processes:
    process.wait()

# Calcula el tiempo total de ejecución
end_time = time.time()
total_time = end_time - start_time

# Muestra el tiempo total de ejecución
print(f"Actualización completa. Tiempo total: {total_time:.2f} segundos.")
