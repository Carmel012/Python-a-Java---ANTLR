public class Miclase {
    public int suma(int a, int b, int c) {
    int result = a+b+c;
    return result;
    }
    public static void main(String[] args) {
        Miclase miObjeto = new Miclase();
        int respuesta = miObjeto.suma(4, 5, 6);
        System.out.println(respuesta);
    }
}