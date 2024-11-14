from PythonToJavaParser import *
from PythonToJavaListener import PythonToJavaListener

class ConvertJava(PythonToJavaListener):
    def __init__(self):
        self.java_code = []
        self.indent_level = 0

    # Enter a parse tree produced by PythonToJavaParser#program.
    def enterProgram(self, ctx:PythonToJavaParser.ProgramContext):
        self.java_code.append("public class Miclase {")

    # Exit a parse tree produced by PythonToJavaParser#program.
    def exitProgram(self, ctx:PythonToJavaParser.ProgramContext):
        self.java_code.append("    public static void main(String[] args) {")
        self.java_code.append("        Miclase miObjeto = new Miclase();")
        self.java_code.append("        int respuesta = miObjeto.suma(4, 5, 6);")
        self.java_code.append("        System.out.println(respuesta);")
        self.java_code.append("    }")
        self.java_code.append("}")


    # Enter a parse tree produced by PythonToJavaParser#func_def.
    def enterFunc_def(self, ctx:PythonToJavaParser.Func_defContext):
        func_name = ctx.NAME().getText()
        params = ctx.params().getText().replace(",", ", int ")
        self.java_code.append(f"    public int {func_name}(int {params}) {{")
        self.indent_level += 1

    # Exit a parse tree produced by PythonToJavaParser#func_def.
    def exitFunc_def(self, ctx:PythonToJavaParser.Func_defContext):
        self.indent_level -= 1
        self.java_code.append("    }")


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
        var_name = ctx.NAME().getText()
        expr = ctx.expr().getText()
        indent = "    " * self.indent_level
        self.java_code.append(f"{indent}int {var_name} = {expr};")

    # Exit a parse tree produced by PythonToJavaParser#var_assign.
    def exitVar_assign(self, ctx:PythonToJavaParser.Var_assignContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#return_stmt.
    def enterReturn_stmt(self, ctx:PythonToJavaParser.Return_stmtContext):
        expr = ctx.expr().getText()
        indent = "    " * self.indent_level
        self.java_code.append(f"{indent}return {expr};")

    # Exit a parse tree produced by PythonToJavaParser#return_stmt.
    def exitReturn_stmt(self, ctx:PythonToJavaParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PythonToJavaParser#print_stmt.
    def enterPrint_stmt(self, ctx:PythonToJavaParser.Print_stmtContext):
        # No debería haber un print dentro de la función suma
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
        # No debería haber una llamada a la función dentro de la función suma
        pass

    # Exit a parse tree produced by PythonToJavaParser#func_call.
    def exitFunc_call(self, ctx:PythonToJavaParser.Func_callContext):
        pass

    def get_java_code(self):
        return "\n".join(self.java_code)

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.get_java_code())