package Hamming;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class ReceptorHam {
    public static void main(String[] args) {
        if (args.length > 0) {
            // revisar que si hayan parametros
            String jsonData = args[0];

            try {
                JSONArray jsonArray = new JSONArray(jsonData);
                int outerLength = jsonArray.length();

                for (int i = 0; i < outerLength; i++) {
                    JSONArray innerArray = jsonArray.getJSONArray(i);

                    // Posicion 0 mensajes y 1 codigos que se sacaran en cada iteracion del programa para asi decodificar y verificar cada letra

                    JSONArray firstInnerArray = innerArray.getJSONArray(0);
                    JSONArray secondInnerArray = innerArray.getJSONArray(1);
                    String[] mensajesCODED = new String[firstInnerArray.length()];
                    String[] codigosHAM = new String[secondInnerArray.length()];

                    // llenar arrays
                    for (int j = 0; j < firstInnerArray.length(); j++) {
                        mensajesCODED[j] = firstInnerArray.getInt(j);
                    }

                    for (int j = 0; j < secondInnerArray.length(); j++) {
                        codigosHAM[j] = secondInnerArray.getString(j);
                    }

                    // Ya que tenemos el mensaje y codigo de el caracter i especificamente...
                    
                    // Primero hay que convertir cada número de la cadena en una cadena en un arreglo de enteros
                    int[][] arregloMensajesEnteros = convertirArregloEntero(mensajesCODED);
                    int[][] arregloCodesEnteros = convertirArregloEntero(); // verificar
                    int[] decimalesporMensaje = new int[arregloMensajesInvertidos.length];

                    int[][] arregloMensajesInvertidos = new int[arregloMensajesEnteros.length][];
                    for (int j = 0; j < arregloMensajesEnteros.length; j++) {
                        int[] arregloInvertido = new int[arregloMensajesEnteros[j].length];
                        for (int k = 0; k < arregloMensajesEnteros[j].length; k++) {
                            arregloInvertido[k] = arregloMensajesEnteros[j][arregloMensajesEnteros[j].length - 1 - k];
                        }
                        arregloMensajesInvertidos[j] = arregloInvertido;
                    }



                }
            } catch (JSONException e) {
                System.err.println("Error parsing JSON: " + e.getMessage());
            }
        } else {
            System.out.println("No JSON data provided.");
        }

        // xdxdxdxd :)

        
        

        // proceso de decodificar


        // descodificar
        for (int i = 0; i < arregloMensajesInvertidos.length; i++) {
            
            int[] resultado_paridad = new int[arregloCodesEnteros.length];
            int[] contenido = arregloMensajesInvertidos[i];
            int[][] contenidoPorCodigo = obtenerContenidoDecodificado(contenido, arregloCodesEnteros);

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

        // buscar el error
        if (contieneSoloCeros(decimalesporMensaje)) {
            System.out.println("\n-------------------------------------------------------------------\n");
            System.out.println("Todo bien, el mensaje recibido exitosamente es:");
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
                if (indi > 0 && indi < elemento.length) {
                    int hh = elemento[indi-1];
                    int nuevo_num = (hh == 0) ? 1 : 0;
                    System.out.println("     --> Se ha cambiado el bit erroneo " + hh + " en el indice " + indi + " por " + nuevo_num + " para corregir el mensaje.");
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