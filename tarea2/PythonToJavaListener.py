# Generated from PythonToJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonToJavaParser import PythonToJavaParser
else:
    from PythonToJavaParser import PythonToJavaParser

# This class defines a complete listener for a parse tree produced by PythonToJavaParser.
class PythonToJavaListener(ParseTreeListener):

    # Enter a parse tree produced by PythonToJavaParser#program.
    def enterProgram(self, ctx:PythonToJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#program.
    def exitProgram(self, ctx:PythonToJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#func_def.
    def enterFunc_def(self, ctx:PythonToJavaParser.Func_defContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#func_def.
    def exitFunc_def(self, ctx:PythonToJavaParser.Func_defContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#params.
    def enterParams(self, ctx:PythonToJavaParser.ParamsContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#params.
    def exitParams(self, ctx:PythonToJavaParser.ParamsContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#stmt.
    def enterStmt(self, ctx:PythonToJavaParser.StmtContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#stmt.
    def exitStmt(self, ctx:PythonToJavaParser.StmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#var_assign.
    def enterVar_assign(self, ctx:PythonToJavaParser.Var_assignContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#var_assign.
    def exitVar_assign(self, ctx:PythonToJavaParser.Var_assignContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#return_stmt.
    def enterReturn_stmt(self, ctx:PythonToJavaParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#return_stmt.
    def exitReturn_stmt(self, ctx:PythonToJavaParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#print_stmt.
    def enterPrint_stmt(self, ctx:PythonToJavaParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#print_stmt.
    def exitPrint_stmt(self, ctx:PythonToJavaParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#expr.
    def enterExpr(self, ctx:PythonToJavaParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#expr.
    def exitExpr(self, ctx:PythonToJavaParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#func_call.
    def enterFunc_call(self, ctx:PythonToJavaParser.Func_callContext):
        pass

    # Exit a parse tree produced by PythonToJavaParser#func_call.
    def exitFunc_call(self, ctx:PythonToJavaParser.Func_callContext):
        pass



del PythonToJavaParser