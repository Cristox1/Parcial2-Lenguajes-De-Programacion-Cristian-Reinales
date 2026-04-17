# Generated from Ejercicio1.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,3,3,45,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,55,8,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,3,5,64,8,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,72,
        8,6,10,6,12,6,75,9,6,3,6,77,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,3,8,89,8,8,1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,
        16,18,0,1,1,0,14,19,96,0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,
        39,1,0,0,0,8,48,1,0,0,0,10,58,1,0,0,0,12,67,1,0,0,0,14,80,1,0,0,
        0,16,88,1,0,0,0,18,90,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,
        1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,
        26,1,1,0,0,0,27,32,3,4,2,0,28,32,3,6,3,0,29,32,3,8,4,0,30,32,3,10,
        5,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,
        1,0,0,0,33,34,5,1,0,0,34,35,3,12,6,0,35,36,5,2,0,0,36,37,5,21,0,
        0,37,38,5,3,0,0,38,5,1,0,0,0,39,40,5,4,0,0,40,41,5,2,0,0,41,44,5,
        21,0,0,42,43,5,5,0,0,43,45,3,18,9,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,46,1,0,0,0,46,47,5,3,0,0,47,7,1,0,0,0,48,49,5,6,0,0,49,50,5,21,
        0,0,50,51,5,7,0,0,51,54,3,12,6,0,52,53,5,5,0,0,53,55,3,18,9,0,54,
        52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,5,3,0,0,57,9,1,0,0,
        0,58,59,5,8,0,0,59,60,5,9,0,0,60,63,5,21,0,0,61,62,5,5,0,0,62,64,
        3,18,9,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,5,3,0,0,
        66,11,1,0,0,0,67,76,5,10,0,0,68,73,3,14,7,0,69,70,5,11,0,0,70,72,
        3,14,7,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,
        74,77,1,0,0,0,75,73,1,0,0,0,76,68,1,0,0,0,76,77,1,0,0,0,77,78,1,
        0,0,0,78,79,5,12,0,0,79,13,1,0,0,0,80,81,5,22,0,0,81,82,5,13,0,0,
        82,83,3,16,8,0,83,15,1,0,0,0,84,89,5,22,0,0,85,89,5,23,0,0,86,89,
        5,20,0,0,87,89,3,12,6,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,
        0,88,87,1,0,0,0,89,17,1,0,0,0,90,91,5,21,0,0,91,92,7,0,0,0,92,93,
        3,16,8,0,93,19,1,0,0,0,8,23,31,44,54,63,73,76,88
    ]

class Ejercicio1Parser ( Parser ):

    grammarFileName = "Ejercicio1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'GUARDAR'", "'EN'", "';'", "'BUSCAR'", 
                     "'DONDE'", "'ACTUALIZAR'", "'CON'", "'ELIMINAR'", "'DE'", 
                     "'{'", "','", "'}'", "':'", "'<'", "'>'", "'=='", "'!='", 
                     "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOLEANO", "IDENTIFICADOR", "CADENA", "NUMERO", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_stCrear = 2
    RULE_stBuscar = 3
    RULE_stActualizar = 4
    RULE_stEliminar = 5
    RULE_objetoJson = 6
    RULE_parClaveValor = 7
    RULE_valor = 8
    RULE_condicion = 9

    ruleNames =  [ "programa", "sentencia", "stCrear", "stBuscar", "stActualizar", 
                   "stEliminar", "objetoJson", "parClaveValor", "valor", 
                   "condicion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    BOOLEANO=20
    IDENTIFICADOR=21
    CADENA=22
    NUMERO=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Ejercicio1Parser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Ejercicio1Parser.SentenciaContext)
            else:
                return self.getTypedRuleContext(Ejercicio1Parser.SentenciaContext,i)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = Ejercicio1Parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.sentencia()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 338) != 0)):
                    break

            self.state = 25
            self.match(Ejercicio1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stCrear(self):
            return self.getTypedRuleContext(Ejercicio1Parser.StCrearContext,0)


        def stBuscar(self):
            return self.getTypedRuleContext(Ejercicio1Parser.StBuscarContext,0)


        def stActualizar(self):
            return self.getTypedRuleContext(Ejercicio1Parser.StActualizarContext,0)


        def stEliminar(self):
            return self.getTypedRuleContext(Ejercicio1Parser.StEliminarContext,0)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = Ejercicio1Parser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.stCrear()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.stBuscar()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.stActualizar()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.stEliminar()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StCrearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objetoJson(self):
            return self.getTypedRuleContext(Ejercicio1Parser.ObjetoJsonContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(Ejercicio1Parser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_stCrear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStCrear" ):
                listener.enterStCrear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStCrear" ):
                listener.exitStCrear(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStCrear" ):
                return visitor.visitStCrear(self)
            else:
                return visitor.visitChildren(self)




    def stCrear(self):

        localctx = Ejercicio1Parser.StCrearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stCrear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(Ejercicio1Parser.T__0)
            self.state = 34
            self.objetoJson()
            self.state = 35
            self.match(Ejercicio1Parser.T__1)
            self.state = 36
            self.match(Ejercicio1Parser.IDENTIFICADOR)
            self.state = 37
            self.match(Ejercicio1Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StBuscarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(Ejercicio1Parser.IDENTIFICADOR, 0)

        def condicion(self):
            return self.getTypedRuleContext(Ejercicio1Parser.CondicionContext,0)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_stBuscar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStBuscar" ):
                listener.enterStBuscar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStBuscar" ):
                listener.exitStBuscar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStBuscar" ):
                return visitor.visitStBuscar(self)
            else:
                return visitor.visitChildren(self)




    def stBuscar(self):

        localctx = Ejercicio1Parser.StBuscarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stBuscar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(Ejercicio1Parser.T__3)
            self.state = 40
            self.match(Ejercicio1Parser.T__1)
            self.state = 41
            self.match(Ejercicio1Parser.IDENTIFICADOR)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 42
                self.match(Ejercicio1Parser.T__4)
                self.state = 43
                self.condicion()


            self.state = 46
            self.match(Ejercicio1Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StActualizarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(Ejercicio1Parser.IDENTIFICADOR, 0)

        def objetoJson(self):
            return self.getTypedRuleContext(Ejercicio1Parser.ObjetoJsonContext,0)


        def condicion(self):
            return self.getTypedRuleContext(Ejercicio1Parser.CondicionContext,0)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_stActualizar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStActualizar" ):
                listener.enterStActualizar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStActualizar" ):
                listener.exitStActualizar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStActualizar" ):
                return visitor.visitStActualizar(self)
            else:
                return visitor.visitChildren(self)




    def stActualizar(self):

        localctx = Ejercicio1Parser.StActualizarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stActualizar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(Ejercicio1Parser.T__5)
            self.state = 49
            self.match(Ejercicio1Parser.IDENTIFICADOR)
            self.state = 50
            self.match(Ejercicio1Parser.T__6)
            self.state = 51
            self.objetoJson()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 52
                self.match(Ejercicio1Parser.T__4)
                self.state = 53
                self.condicion()


            self.state = 56
            self.match(Ejercicio1Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StEliminarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(Ejercicio1Parser.IDENTIFICADOR, 0)

        def condicion(self):
            return self.getTypedRuleContext(Ejercicio1Parser.CondicionContext,0)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_stEliminar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStEliminar" ):
                listener.enterStEliminar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStEliminar" ):
                listener.exitStEliminar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStEliminar" ):
                return visitor.visitStEliminar(self)
            else:
                return visitor.visitChildren(self)




    def stEliminar(self):

        localctx = Ejercicio1Parser.StEliminarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stEliminar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(Ejercicio1Parser.T__7)
            self.state = 59
            self.match(Ejercicio1Parser.T__8)
            self.state = 60
            self.match(Ejercicio1Parser.IDENTIFICADOR)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 61
                self.match(Ejercicio1Parser.T__4)
                self.state = 62
                self.condicion()


            self.state = 65
            self.match(Ejercicio1Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetoJsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parClaveValor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Ejercicio1Parser.ParClaveValorContext)
            else:
                return self.getTypedRuleContext(Ejercicio1Parser.ParClaveValorContext,i)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_objetoJson

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjetoJson" ):
                listener.enterObjetoJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjetoJson" ):
                listener.exitObjetoJson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjetoJson" ):
                return visitor.visitObjetoJson(self)
            else:
                return visitor.visitChildren(self)




    def objetoJson(self):

        localctx = Ejercicio1Parser.ObjetoJsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_objetoJson)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(Ejercicio1Parser.T__9)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 68
                self.parClaveValor()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 69
                    self.match(Ejercicio1Parser.T__10)
                    self.state = 70
                    self.parClaveValor()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 78
            self.match(Ejercicio1Parser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParClaveValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADENA(self):
            return self.getToken(Ejercicio1Parser.CADENA, 0)

        def valor(self):
            return self.getTypedRuleContext(Ejercicio1Parser.ValorContext,0)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_parClaveValor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParClaveValor" ):
                listener.enterParClaveValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParClaveValor" ):
                listener.exitParClaveValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParClaveValor" ):
                return visitor.visitParClaveValor(self)
            else:
                return visitor.visitChildren(self)




    def parClaveValor(self):

        localctx = Ejercicio1Parser.ParClaveValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parClaveValor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(Ejercicio1Parser.CADENA)
            self.state = 81
            self.match(Ejercicio1Parser.T__12)
            self.state = 82
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADENA(self):
            return self.getToken(Ejercicio1Parser.CADENA, 0)

        def NUMERO(self):
            return self.getToken(Ejercicio1Parser.NUMERO, 0)

        def BOOLEANO(self):
            return self.getToken(Ejercicio1Parser.BOOLEANO, 0)

        def objetoJson(self):
            return self.getTypedRuleContext(Ejercicio1Parser.ObjetoJsonContext,0)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = Ejercicio1Parser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_valor)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(Ejercicio1Parser.CADENA)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(Ejercicio1Parser.NUMERO)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(Ejercicio1Parser.BOOLEANO)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.objetoJson()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def IDENTIFICADOR(self):
            return self.getToken(Ejercicio1Parser.IDENTIFICADOR, 0)

        def valor(self):
            return self.getTypedRuleContext(Ejercicio1Parser.ValorContext,0)


        def getRuleIndex(self):
            return Ejercicio1Parser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = Ejercicio1Parser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(Ejercicio1Parser.IDENTIFICADOR)
            self.state = 91
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 92
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





