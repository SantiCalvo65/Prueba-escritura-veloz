#importamos los modulos necesarios
import tkinter as tk
import time
import random as rm

#hacemos una funcion que genere un texto random y pida que se escriba el mismo.
def iniciar_prueba():
    palabras = ["tierra", "comida", "sol", "flor", "lluvia", "montaña", "noche", "musica"]
    texto_aleatorio = " ".join(rm.sample(palabras, 8))
    
    #Comenzamos la prueba y mostramos el texto
    print("--------------------------")
    print("Comienza la prueba de texto veloz!")
    print("Texto a escribir: ", texto_aleatorio)
    input("Presiona Enter para comenzar")

    return texto_aleatorio

def medir_tiempo(texto):
    tiempo_inicio = time.time()  # Registrar el tiempo de inicio
    
    texto_usuario = input("\nEscribe el texto: ") # Solicitar que el usuario escriba el texto

    tiempo_fin = time.time()# Registrar el tiempo de fin

    tiempo_total = tiempo_fin - tiempo_inicio# Calcular el tiempo que tardó

    aciertos = sum(1 for i in range(min(len(texto), len(texto_usuario))) if texto[i] == texto_usuario[i])
    porcentaje_aciertos = (aciertos / len(texto)) * 100 # Comparar el texto ingresado con el original

    return tiempo_total, porcentaje_aciertos

def mostrar_resultado(tiempo_total, porcentaje_aciertos):
      # Mostrar los resultados
    print(f"\n¡Prueba terminada!")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")
    
    # Proporcionar una retroalimentación extra
    if porcentaje_aciertos == 100:
        print("¡Excelente! Escribiste todo correctamente.")
    else:
        print("¡Sigue practicando!")


# Creamos el programa
bucle = True
while bucle:

  #pidamos que elijan una opcion

  print("Bienvenido al programa de escritura veloz.")
  print("Comenzar prueba de escritura veloz.")
  print("1. Comenzar prueba.")
  print("2. Salir del programa")
  opcion=input("Elije una opcion(1 o 2): ")

  #Si la opcion es 1, comenzamos el programa
  if opcion == "1":
      
    texto = iniciar_prueba()
    tiempo, aciertos = medir_tiempo(texto)
    mostrar_resultado(tiempo, aciertos)

  #Si la opcion es 2, finalizamos el programa
  elif opcion == "2":
     print("Saliendo del programa")
     print("Gracias por jugar!")
     print("--------------------------")
     bucle=False  




    
