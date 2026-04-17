import time
import matplotlib.pyplot as plt

class ParserError(Exception):
    pass

class ASDR_Calculadora:
    def __init__(self, cadena):
        self.tokens = list(cadena) + ['$']
        self.pos = 0
        self.pila = ['$', 'E']  

        self.reglas = {
            'E': [['n', 'Ep']],
            'Ep': [['A1', 'Ep'], ['A2', 'Ep'], ['vacio']],
            'A1': [['P', 'E']],
            'A2': [['M', 'E']],
            'P': [['+']],
            'M': [['*']]
        }

        self.tabla_prediccion = {
            ('E', 'n'): self.reglas['E'][0],     
            ('Ep', '+'): self.reglas['Ep'][0],   
            ('Ep', '*'): self.reglas['Ep'][1],   
            ('Ep', '$'): self.reglas['Ep'][2],   
            ('A1', '+'): self.reglas['A1'][0],   
            ('A2', '*'): self.reglas['A2'][0],   
            ('P', '+'): self.reglas['P'][0],     
            ('M', '*'): self.reglas['M'][0]      
        }

    def parse(self): #Parser predictivo
        while len(self.pila) > 0:
            tope = self.pila.pop()
            actual = self.tokens[self.pos]

            if tope in ['n', '+', '*', '$']:  
                if tope == actual:
                    self.pos += 1
                else:
                    raise ParserError(f"Se esperaba '{tope}' pero se encontro '{actual}'")
            elif tope == 'vacio':
                pass
            else:  
                if (tope, actual) in self.tabla_prediccion:
                    produccion = self.tabla_prediccion[(tope, actual)]
                    for simbolo in reversed(produccion):
                        self.pila.append(simbolo)
                else:
                    raise ParserError("Error de sintaxis en: " + str(actual))
        
        return True


def generar_cadena_prueba(n_operaciones):
    cadena = "n"
    for i in range(n_operaciones):
        cadena += "+n" if i % 2 == 0 else "*n"
    return cadena


def parser_predictivo_wrapper(cadena):
    parser = ASDR_Calculadora(cadena)
    try:
        parser.parse()
        return True
    except ParserError:
        return False

def ejecutar_pruebas_y_graficar_ll1():
    tamanos = [5, 10, 15, 20, 25, 30, 40, 50]
    tiempos_ll1 = []
    longitudes_cadena = []

    for tam in tamanos:
        cadena = generar_cadena_prueba(tam)
        longitudes_cadena.append(len(cadena))
        
        inicio = time.perf_counter()
        parser_predictivo_wrapper(cadena)
        fin = time.perf_counter()
        
        tiempo_ms = (fin - inicio) * 1000
        tiempos_ll1.append(tiempo_ms)
        
        print("Longitud cadena: ", cadena)
        print("Tiempo ejecucion LL1: ", tiempo_ms)
        print("")

    plt.figure(figsize=(10, 6))
    plt.plot(longitudes_cadena, tiempos_ll1, label='Rendimiento Parser Predictivo - LL1', marker='s', color='blue')
    
    plt.title('Rendimiento del Parser Predictivo')
    plt.xlabel('Longitud de la cadena de texto (n)')
    plt.ylabel('Tiempo de ejecucion (Milisegundos)')
    plt.ylim(0, 4)
    plt.legend()
    plt.grid(True)
    
    print("\nMostrando grafica de resultados del LL1...")
    plt.show()

if __name__ == '__main__':
    ejecutar_pruebas_y_graficar_ll1()