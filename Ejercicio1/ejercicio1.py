from antlr4 import *
from Ejercicio1Lexer import Ejercicio1Lexer
from Ejercicio1Parser import Ejercicio1Parser
from ejercicio1Visitor import MiVisitor

def main():
    # Codigo fuente de prueba usando tu gramatica
    codigo_fuente = """
    GUARDAR { "nombre": "Cristian", "edad": 23, "activo": verdadero } EN usuarios;
    GUARDAR { "nombre": "Ana", "edad": 32, "activo": falso } EN usuarios;
    
    BUSCAR EN usuarios;
    BUSCAR EN usuarios DONDE edad > 30;
    
    ACTUALIZAR usuarios CON { "activo": verdadero } DONDE edad > 30;
    BUSCAR EN usuarios;
    
    ELIMINAR DE usuarios DONDE nombre == "Cristian";
    BUSCAR EN usuarios;
    """

    print("Codigo fuente:")
    print(codigo_fuente)

    input_stream = InputStream(codigo_fuente)
    lexer = Ejercicio1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Ejercicio1Parser(stream)

    tree = parser.programa()

    print("=> Ejecucion:")
    visitor = MiVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()