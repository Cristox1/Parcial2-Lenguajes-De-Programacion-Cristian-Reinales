import subprocess
import time
import matplotlib.pyplot as plt
import os

def generar_cadena_booleana(n):
    partes = ["true"]
    for i in range(n):
        if i % 2 == 0:
            partes.append("OR false")
        else:
            partes.append("AND true")
    return " ".join(partes) + "\n"

def ejecutar_pruebas_yacc():
    tamanos = [1000, 5000, 10000, 20000, 50000, 100000]
    tiempos = []
    
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_ejecutable = os.path.join(directorio_actual, 'calculadoraBooleana')
    
    
    for tam in tamanos:
        cadena = generar_cadena_booleana(tam)
        
        inicio = time.perf_counter()
        subprocess.run([ruta_ejecutable], input=cadena, text=True, capture_output=True)
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        tiempos.append(tiempo_ms)
        
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos, label='Rendimiento YACC (LALR1)', marker='o', color='green')
    
    plt.title('Rendimiento del Analizador YACC/Bison')
    plt.xlabel('Cantidad de operaciones logicas (n)')
    plt.ylabel('Tiempo de ejecucion (Milisegundos)')
    plt.ylim(0, 1000)
    
    plt.legend()
    plt.grid(True)
    
    plt.show()

if __name__ == '__main__':
    ejecutar_pruebas_yacc()