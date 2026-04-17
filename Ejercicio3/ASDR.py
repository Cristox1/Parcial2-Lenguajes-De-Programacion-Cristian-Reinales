class ParserError(Exception):
    pass


class GramaticaASD:
    def __init__(self, reglas, simbolo_inicial, vacio='vacio'):
        self.reglas = reglas
        self.simbolo_inicial = simbolo_inicial
        self.vacio = vacio

        self.no_terminales = set(reglas.keys())
        self.terminales = set()

        for nt, producciones in reglas.items():
            for prod in producciones:
                for simbolo in prod:
                    if simbolo not in self.no_terminales and simbolo != self.vacio:
                        self.terminales.add(simbolo)

        self.primeros = {nt: set() for nt in self.no_terminales}
        self.siguientes = {nt: set() for nt in self.no_terminales}
        self.prediccion = {}  

    def primeros_de_cadena(self, cadena, primeros):
        if not cadena:
            return {self.vacio}
        if len(cadena) == 1 and cadena[0] == self.vacio:
            return {self.vacio}

        resultado = set()

        for simbolo in cadena:
            if simbolo == self.vacio:
                resultado.add(self.vacio)
                break

            if simbolo in self.terminales:
                resultado.add(simbolo)
                return resultado

            if simbolo in self.no_terminales:
                resultado |= (primeros[simbolo] - {self.vacio})
                if self.vacio not in primeros[simbolo]:
                    return resultado
            else:
                resultado.add(simbolo)
                return resultado

        resultado.add(self.vacio)
        return resultado

    def calcular_primeros(self):
        cambio = True
        while cambio:
            cambio = False
            for A, producciones in self.reglas.items():
                for alpha in producciones:
                    first_alpha = self.primeros_de_cadena(alpha, self.primeros)
                    antes = len(self.primeros[A])
                    self.primeros[A] |= first_alpha
                    if len(self.primeros[A]) != antes:
                        cambio = True

    def calcular_siguientes(self):
        self.siguientes[self.simbolo_inicial].add('$')

        cambio = True
        while cambio:
            cambio = False
            for B, producciones in self.reglas.items():
                for alpha in producciones:
                    for i, A in enumerate(alpha):
                        if A not in self.no_terminales:
                            continue

                        beta = alpha[i + 1:]
                        first_beta = self.primeros_de_cadena(beta, self.primeros)

                        antes = len(self.siguientes[A])
                        self.siguientes[A] |= (first_beta - {self.vacio})

                        if (not beta) or (self.vacio in first_beta):
                            self.siguientes[A] |= self.siguientes[B]

                        if len(self.siguientes[A]) != antes:
                            cambio = True

    def calcular_prediccion(self):
        self.prediccion = {}
        for A, producciones in self.reglas.items():
            for alpha in producciones:
                first_alpha = self.primeros_de_cadena(alpha, self.primeros)
                if self.vacio in first_alpha:
                    pred = (first_alpha - {self.vacio}) | self.siguientes[A]
                else:
                    pred = set(first_alpha)
                self.prediccion[(A, tuple(alpha))] = pred

    def analizar_gramatica(self):
        self.calcular_primeros()
        self.calcular_siguientes()
        self.calcular_prediccion()

    def conflictos_ll1(self): # Devuelve una lista de por que no es LL1
        por_A = {}
        for (A, alpha), pred in self.prediccion.items():
            por_A.setdefault(A, []).append((alpha, pred))

        conflictos = []
        for A, lst in por_A.items():
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    p1_alpha, p1 = lst[i]
                    p2_alpha, p2 = lst[j]
                    inter = p1 & p2
                    if inter:
                        conflictos.append((A, p1_alpha, p2_alpha, inter))
        return conflictos

    
    def imprimir_conjuntos(self):
        print(" Conjunto de primeros")
        for nt in sorted(self.primeros):
            print(f"Primeros: ({nt}) = {self.primeros[nt]}")

        print("Conjunto de siguientes")
        for nt in sorted(self.siguientes):
            print(f"Siguientes: ({nt}) = {self.siguientes[nt]}")

        print("Conjuntode predicciones")
        for (A, alpha), pred in self.prediccion.items():
            prod_str = f"{A} -> {' '.join(alpha)}"
            print(f"Predicciones: ({prod_str:<25})")

        print(" Es una gramatica LL1?")
        conflictos = self.conflictos_ll1()
        if not conflictos:
            print("La gramática Si es una gramatica LL(1)")
        else:
            print("La gramática No es LL(1).")
            print("Conflictos encontrados:")
            for A, p1, p2, inter in conflictos:
                s1 = f"{A} -> {' '.join(p1)}"
                s2 = f"{A} -> {' '.join(p2)}"
                print(f"- En {A}:")
                print(f"    {s1}")
                print(f"    {s2}")
                print(f"  Interseccion = {inter}")



class ASDR:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def lookahead(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def emparejar(self, esperado):
        actual = self.lookahead()
        if actual == esperado:
            self.pos += 1
        else:
            raise ParserError(f"Se esperaba '{esperado}' y se encontro '{actual}' en posicion {self.pos}")

    def parse(self):
        self.S()
        if self.lookahead() != '$':
            raise ParserError(f"Entrada no consumida. Siguiente token: '{self.lookahead()}'")
        return True

    def S(self):
        la = self.lookahead()
        if la == 'uno': 
            self.D()
            self.E()
        else:
            self.A()
            self.B()
            self.C()

    def A(self):
        if self.lookahead() == 'dos':
            self.emparejar('dos')
            self.B()
            self.emparejar('tres')
        else:
            return

    def B(self):
        self.Bp()

    def Bp(self):
        if self.lookahead() == 'cuatro':
            self.emparejar('cuatro')
            self.C()
            self.emparejar('cinco')
            self.Bp()
        else:
            return

    def C(self):
        if self.lookahead() == 'seis':
            self.emparejar('seis')
            self.A()
            self.B()
        else:
            return

    def D(self):
        if self.lookahead() == 'uno':
            self.emparejar('uno')
            self.A()
            self.E()
        else:
            self.B()

    def E(self):
        self.emparejar('tres')


if __name__ == "__main__":
    reglas = {
        'S': [['A', 'a', 'A', 'b'], ['B', 'b', 'B', 'a']],
        'A': [['vacio']],
        'B': [['vacio']]
    }

    print("=> Calculo de primeros/segundos/predicciones y Comprobacion LL1 ")
    g = GramaticaASD(reglas, simbolo_inicial='S', vacio='vacio')
    g.analizar_gramatica()
    g.imprimir_conjuntos()

    print(" Prueba de ASDR con un parser")
    entrada = ["dos", "tres", "$"]
    print("Entrada:", entrada)

    try:
        p = ASDR(entrada)
        p.parse()
        print("Resultado: Cadena ACEPTADA")
    except ParserError as e:
        print("Resultado: Cadena RECHAZADA")
        print("Detalle:", e)