# Generated from Ejercicio1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Ejercicio1Parser import Ejercicio1Parser
else:
    from Ejercicio1Parser import Ejercicio1Parser

# This class defines a complete generic visitor for a parse tree produced by Ejercicio1Parser.

class Ejercicio1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Ejercicio1Parser#programa.
    def visitPrograma(self, ctx:Ejercicio1Parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#sentencia.
    def visitSentencia(self, ctx:Ejercicio1Parser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#stCrear.
    def visitStCrear(self, ctx:Ejercicio1Parser.StCrearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#stBuscar.
    def visitStBuscar(self, ctx:Ejercicio1Parser.StBuscarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#stActualizar.
    def visitStActualizar(self, ctx:Ejercicio1Parser.StActualizarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#stEliminar.
    def visitStEliminar(self, ctx:Ejercicio1Parser.StEliminarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#objetoJson.
    def visitObjetoJson(self, ctx:Ejercicio1Parser.ObjetoJsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#parClaveValor.
    def visitParClaveValor(self, ctx:Ejercicio1Parser.ParClaveValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#valor.
    def visitValor(self, ctx:Ejercicio1Parser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ejercicio1Parser#condicion.
    def visitCondicion(self, ctx:Ejercicio1Parser.CondicionContext):
        return self.visitChildren(ctx)



del Ejercicio1Parser