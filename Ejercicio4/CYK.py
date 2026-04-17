import time
import matplotlib.pyplot as plt

# Gramatica en forma normal de Chomsky
gramatica_cyk = {
    'E': [['E', 'A1'], ['E', 'A2'], ['n']],
    'A1': [['P', 'E']],
    'A2': [['M', 'E']],
    'P': [['+']],
    'M': [['*']]
}

def parser_cyk(cadena, gramatica, simbolo_inicial='E'): # Algoritmo CYK
    n = len(cadena)
    if n == 0:
        return False
    
    tabla = [[set() for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        terminal = cadena[i]
        for variable, producciones in gramatica.items():
            for prod in producciones:
                if len(prod) == 1 and prod[0] == terminal:
                    tabla[i][i].add(variable)
                    
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                conjunto_izquierdo = tabla[i][k]
                conjunto_derecho = tabla[k + 1][j]
                
                for variable, producciones in gramatica.items():
                    for prod in producciones:
                        if len(prod) == 2:
                            B = prod[0]
                            C = prod[1]
                            if B in conjunto_izquierdo and C in conjunto_derecho:
                                tabla[i][j].add(variable)
                                
    return simbolo_inicial in tabla[0][n - 1]

def generar_cadena_prueba(n_operaciones):
    cadena = "n"
    for i in range(n_operaciones):
        cadena += "+n" if i % 2 == 0 else "*n"
    return cadena

def ejecutar_pruebas_y_graficar_cyk():
    tamanos = [5, 10, 15, 20, 25, 30, 40, 50] 
    tiempos_cyk = []
    longitudes_cadena = []

    for tam in tamanos:
        cadena = generar_cadena_prueba(tam)
        longitudes_cadena.append(len(cadena))
        
        inicio_cyk = time.perf_counter()
        parser_cyk(cadena, gramatica_cyk)
        fin_cyk = time.perf_counter()
        
        tiempo_ms = (fin_cyk - inicio_cyk) * 1000
        tiempos_cyk.append(tiempo_ms)
        
        print("Longitud cadena: ", cadena)
        print("Tiempo de ejecucion: ", tiempo_ms)
        print("")

    plt.figure(figsize=(10, 6))
    plt.plot(longitudes_cadena, tiempos_cyk, label='Rendimiento CYK', marker='o', color='red')
    
    plt.title('Rendimiento del Algoritmo CYK')
    plt.xlabel('Longitud de la cadena de texto (n)')
    plt.ylabel('Tiempo de ejecucion (Milisegundos)')
    plt.legend()
    plt.grid(True)
    
    plt.show()

if __name__ == '__main__':
    ejecutar_pruebas_y_graficar_cyk()