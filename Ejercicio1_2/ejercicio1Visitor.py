from Ejercicio1Visitor import Ejercicio1Visitor
from Ejercicio1Parser import Ejercicio1Parser

class MiVisitor(Ejercicio1Visitor):
    def __init__(self):
        self.db = {} # Nuestra base de datos NoSQL simulada en memoria

    # Operaciones CRUD
    def visitStCrear(self, ctx: Ejercicio1Parser.StCrearContext):
        coleccion = ctx.IDENTIFICADOR().getText()
        archivo = self.visit(ctx.objetoJson()) 
        
        if coleccion not in self.db:
            self.db[coleccion] = []
        self.db[coleccion].append(archivo)
        print("")
        print("Creando archivo:")
        print("Archivo: ", archivo)
        print("Archivo creado en ", coleccion)
        print("")

    def visitStBuscar(self, ctx: Ejercicio1Parser.StBuscarContext):
        coleccion = ctx.IDENTIFICADOR().getText()
        registros = self.db.get(coleccion, [])
        
        if ctx.condicion():
            campo, op, valor = self.visit(ctx.condicion())
            resultados = [r for r in registros if self.evaluar(r.get(campo), op, valor)]
        else:
            resultados = registros
        print("")
        print("Busqueda de archivo:")
        print("Resultado: ", resultados)
        print("")

    def visitStActualizar(self, ctx: Ejercicio1Parser.StActualizarContext):
        coleccion = ctx.IDENTIFICADOR().getText()
        nuevos_datos = self.visit(ctx.objetoJson())
        registros = self.db.get(coleccion, [])
        
        actualizados = 0
        for r in registros:
            if not ctx.condicion() or self.evaluar(r.get(self.visit(ctx.condicion())[0]), self.visit(ctx.condicion())[1], self.visit(ctx.condicion())[2]):
                r.update(nuevos_datos)
                actualizados += 1
        print("")
        print("Actualizando datos") 
        print("Se actualizo: ", actualizados)
        print("De la bd: ", coleccion)
        print("")



    def visitStEliminar(self, ctx: Ejercicio1Parser.StEliminarContext):
        coleccion = ctx.IDENTIFICADOR().getText()
        registros = self.db.get(coleccion, [])
        print("")
        print("Proceso de eliminar")
        if ctx.condicion():
            campo, op, valor = self.visit(ctx.condicion())
            self.db[coleccion] = [r for r in registros if not self.evaluar(r.get(campo), op, valor)]
            
            print(f"Documentos borrados en '{coleccion}' donde {campo} {op} {valor}.")
        else:
            self.db[coleccion] = []
            print("Todos los documentos borrados de: ", coleccion)
        print("")

    
    
    def visitObjetoJson(self, ctx: Ejercicio1Parser.ObjetoJsonContext):
        obj = {}
        for keyval_ctx in ctx.parClaveValor():
            clave, valor = self.visit(keyval_ctx)
            obj[clave] = valor
        return obj

    def visitParClaveValor(self, ctx: Ejercicio1Parser.ParClaveValorContext):
        clave = ctx.CADENA().getText().strip('"')
        valor = self.visit(ctx.valor())
        return clave, valor

    def visitValor(self, ctx: Ejercicio1Parser.ValorContext):
        if ctx.CADENA(): 
            return ctx.CADENA().getText().strip('"')
        if ctx.NUMERO():
            txt = ctx.NUMERO().getText()
            return float(txt) if '.' in txt else int(txt)
        if ctx.BOOLEANO(): 
            return ctx.BOOLEANO().getText() == 'verdadero'
        if ctx.objetoJson(): 
            return self.visit(ctx.objetoJson())

    def visitCondicion(self, ctx: Ejercicio1Parser.CondicionContext):
        campo = ctx.IDENTIFICADOR().getText()
        op = ctx.op.text
        valor = self.visit(ctx.valor())
        return campo, op, valor

    def evaluar(self, val1, op, val2):
        if val1 is None: return False
        if op == '==': return val1 == val2
        if op == '!=': return val1 != val2
        if op == '>': return val1 > val2
        if op == '<': return val1 < val2
        if op == '>=': return val1 >= val2
        if op == '<=': return val1 <= val2
        return False