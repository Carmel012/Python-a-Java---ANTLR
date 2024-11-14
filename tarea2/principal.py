from antlr4 import *
from PythonToJavaLexer import PythonToJavaLexer
from PythonToJavaParser import PythonToJavaParser
from convertJava import ConvertJava

def clean_input(text):
    # Eliminar espacios extra y normalizar saltos de línea
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Mantener solo un espacio entre tokens y eliminar espacios al final
        cleaned = ' '.join(token for token in line.split() if token)
        if cleaned:
            cleaned_lines.append(cleaned)
    return '\n'.join(cleaned_lines)

def main():
    in_code = input(">")
    # Leer archivo de entrada
    with open(in_code) as file:
        content = file.read()
    
    # Limpiar el contenido antes de procesarlo
    cleaned_content = clean_input(content)
    
    lexer = PythonToJavaLexer(InputStream(cleaned_content))
    t_stream = CommonTokenStream(lexer)

    parser = PythonToJavaParser(t_stream)
    tree = parser.program()

    converter = ConvertJava()
    walker = ParseTreeWalker()
    walker.walk(converter, tree)

    # Escribir el código Java en un archivo
    converter.write_to_file("Miclase.java")

if __name__ == '__main__':
    main()