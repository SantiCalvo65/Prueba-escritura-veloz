#importamos los modulos necesarios
import tkinter as tk
import time
import random as rm

#hacemos una funcion que genere un texto random y pida que se escriba el mismo.
def prueba_velocidad():
    palabras = ["tierra", "comida", "sol", "flor", "lluvia", "montaña", "noche", "musica"]
    texto_aleatorio = " ".join(rm.sample(palabras, 8))
    
    #Comenzamos la prueba y mostramos el texto
    print("Comienza la prueba de texto veloz!")
    print("Texto a escribir: ", texto_aleatorio)
    input("Presiona Enter para comenzar")

    # Registrar el tiempo de inicio
    tiempo_inicio = time.time()

    # Solicitar que el usuario escriba el texto
    texto_usuario = input("\nEscribe el texto: ")

    # Registrar el tiempo de fin
    tiempo_fin = time.time()

    # Calcular el tiempo que tardó
    tiempo_total = tiempo_fin - tiempo_inicio

    # Comparar el texto ingresado con el original
    aciertos = sum(1 for i in range(min(len(texto_aleatorio), len(texto_usuario))) if texto_aleatorio[i] == texto_usuario[i])
    porcentaje_aciertos = (aciertos / len(texto_aleatorio)) * 100

      # Mostrar los resultados
    print(f"\n¡Prueba terminada!")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")
    
    # Proporcionar una retroalimentación extra
    if porcentaje_aciertos == 100:
        print("¡Excelente! Escribiste todo correctamente.")
    else:
        print("¡Sigue practicando!")

# Llamar a la función para iniciar la prueba

prueba_velocidad()



    
