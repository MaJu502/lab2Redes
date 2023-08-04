package Hamming;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane.SystemMenuBar;

import java.util.Arrays;

public class ReceptorHam {
    public static void main(String[] args) {
        // Ruta del archivo de texto a leer
        String rutaArchivo = "Hamming//codedMessageHamming.txt";

        // Lista para almacenar las líneas del archivo
        List<String> lineasArchivo = new ArrayList<>();

        try {
            // Abrir el archivo y leer su contenido
            BufferedReader lector = new BufferedReader(new FileReader(rutaArchivo));
            String linea;

            while ((linea = lector.readLine()) != null) {
                lineasArchivo.add(linea);
            }

            // Cerrar el lector después de leer el archivo
            lector.close();
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }

        // Imprimir el contenido del archivo línea por línea
        String mensajes = lineasArchivo.get(0);
        String codes = lineasArchivo.get(1);
        String[] arregloMensajes = mensajes.split(" ");
        String[] arregloCodes = codes.split(" ");

        // Convertir cada número en una cadena en un arreglo de enteros
        int[][] arregloMensajesEnteros = convertirArregloEntero(arregloMensajes);

        int[][] arregloMensajesInvertidos = new int[arregloMensajesEnteros.length][];
        for (int i = 0; i < arregloMensajesEnteros.length; i++) {
            int[] arregloInvertido = new int[arregloMensajesEnteros[i].length];
            for (int j = 0; j < arregloMensajesEnteros[i].length; j++) {
                arregloInvertido[j] = arregloMensajesEnteros[i][arregloMensajesEnteros[i].length - 1 - j];
            }
            arregloMensajesInvertidos[i] = arregloInvertido;
        }

        int[][] arregloCodesEnteros = convertirArregloEntero(arregloCodes);
        int[] decimalesporMensaje = new int[arregloMensajesInvertidos.length];

        // proceso de decodificar


        // descodificar
        for (int i = 0; i < arregloMensajesInvertidos.length; i++) {
            
            int[] resultado_paridad = new int[arregloCodesEnteros.length];
            int[] contenido = arregloMensajesInvertidos[i];
            int[][] contenidoPorCodigo = obtenerContenidoDecodificado(contenido, arregloCodesEnteros);


            for (int p = 0; p < contenidoPorCodigo.length; p++) {
                for (int b = 0; b < contenidoPorCodigo[p].length; b++) {
                    System.out.print(contenidoPorCodigo[p][b] + " ");
                }
                System.out.println(); // Nueva línea después de imprimir una fila completa
            }

            for (int j = 0; j < contenidoPorCodigo.length; j++) {
                int[] codigo = contenidoPorCodigo[j];
                int cantidadUnos = contarUnos(codigo);
                int cantidadCeros = codigo.length - cantidadUnos;
                // Verificar si hay par o impar en la cantidad de 1's y 0's
                if (cantidadUnos % 2 == 0 && cantidadCeros % 2 == 0) {
                    resultado_paridad[j] = 0;
                } else {
                    resultado_paridad[j] = 1;
                }
                
            }
            
            String resultado = Arrays.toString(resultado_paridad).replaceAll("\\[|\\]|,|\\s", "");
            int gg = Integer.parseInt(resultado, 2);
            decimalesporMensaje[i] = gg;
        }

        System.out.println(Arrays.toString(decimalesporMensaje));

        // buscar el error
        if (contieneSoloCeros(decimalesporMensaje)) {
            System.out.println("\n-------------------------------------------------------------------\n");
            System.out.println("Todo bien, el array decimalporMensaje contiene únicamente 0's:");
            for (String x : arregloMensajes) {
                System.out.println("     " + x);
            }
            System.out.println("\n-------------------------------------------------------------------\n");
        } else {
            for (String x : arregloMensajes) {
                System.out.println("  Mensaje original -> " + x);
            }
            for (int i = 0; i < arregloMensajesInvertidos.length; i++) {
                int[] elemento = arregloMensajesInvertidos[i];
                int indi = decimalesporMensaje[i];
                System.out.println(indi);
                if (indi > 0 && indi < elemento.length) {
                    int hh = elemento[indi-1];
                    int nuevo_num = (hh == 0) ? 1 : 0;
                    System.out.println("     --> Se ha cambiado el bit erroneo " + hh + " por " + nuevo_num + " para corregir.");
                    elemento[indi-1] = nuevo_num;
                    arregloMensajesInvertidos[i] = elemento;

                } else if (indi == 0){
                    // No se hace nada
                } else {
                    System.out.println("Error: el índice " + i + " está fuera del rango del arregloMensajes.");
                }
            }
            
            
            int[][] arregloMensajesDesinvertidos = new int[arregloMensajesInvertidos.length][];
            for (int i = 0; i < arregloMensajesInvertidos.length; i++) {
                int[] arregloDesinvertido = new int[arregloMensajesInvertidos[i].length];
                for (int j = 0; j < arregloMensajesInvertidos[i].length; j++) {
                    arregloDesinvertido[j] = arregloMensajesInvertidos[i][arregloMensajesInvertidos[i].length - 1 - j];
                }
                arregloMensajesDesinvertidos[i] = arregloDesinvertido;
            }

            StringBuilder mensajeFinalDesinvertido = new StringBuilder();

            for (int i = 0; i < arregloMensajesDesinvertidos.length; i++) {
                int[] mensajeDesinvertido = arregloMensajesDesinvertidos[i];
                for (int j = 0; j < mensajeDesinvertido.length; j++) {
                    mensajeFinalDesinvertido.append(mensajeDesinvertido[j]);
                }
            }

            System.out.println("  Mensaje final -> " + mensajeFinalDesinvertido.toString());
            System.out.println("\n-------------------------------------------------------------------\n");

        }

        // mensajes de adios


    }

    // Función para verificar si un array contiene únicamente 0's
    public static boolean contieneSoloCeros(int[] array) {
        for (int elemento : array) {
            if (elemento != 0) {
                return false;
            }
        }
        return true;
    }

    // Método para obtener el contenido por código
    private static int[][] obtenerContenidoDecodificado(int[] contenido, int[][] arregloCodesEnteros) {
        int[][] resultado = new int[arregloCodesEnteros.length][];
        for (int i = 0; i < arregloCodesEnteros.length; i++) {
            int[] codigo = arregloCodesEnteros[i];
            resultado[i] = new int[codigo.length];
            for (int j = 0; j < codigo.length; j++) {
                resultado[i][j] = contenido[codigo[j]];
            }
        }
        return resultado;
    }

    // Método para contar la cantidad de 1's en un arreglo
    private static int contarUnos(int[] arreglo) {
        int contadorUnos = 0;
        for (int elemento : arreglo) {
            if (elemento == 1) {
                contadorUnos++;
            }
        }
        return contadorUnos;
    }

    // Método para convertir un arreglo de cadenas de números a un arreglo de arreglos de enteros
    private static int[][] convertirArregloEntero(String[] arregloCadenas) {
        int[][] resultado = new int[arregloCadenas.length][];
        for (int i = 0; i < arregloCadenas.length; i++) {
            resultado[i] = new int[arregloCadenas[i].length()];
            for (int j = 0; j < arregloCadenas[i].length(); j++) {
                resultado[i][j] = Character.getNumericValue(arregloCadenas[i].charAt(j));
            }
        }
        return resultado;
    }
}