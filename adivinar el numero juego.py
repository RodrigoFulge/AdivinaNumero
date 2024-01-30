import random

class JuegoAdivinaNumero:
    def __init__(self, limite_inferior, limite_superior,name):
        # Inicializa el juego con un número secreto aleatorio entre los límites proporcionados.
        self.numero_secreto = random.randint(limite_inferior, limite_superior)
        print(self.numero_secreto) #Debug
        # Establece el número máximo de intentos permitidos.
        self.intentos_maximos = 5
        # Inicializa el contador de intentos actuales.
        self.intentos_actuales = 0
        self.name = name

    def adivinar_numero(self, numero):
        # Método para procesar el intento de adivinar un número.
        self.intentos_actuales += 1
        print(numero) #debug

        for i in range(len(numero)):
            if numero[i] > self.numero_secreto:
                print(f"El número {numero[i]} mayor al número secreto. Intenta de nuevo")
            if numero[i] < self.numero_secreto:
                print(f"El número {numero[i]} es menor al número secreto. Intenta de nuevo")
            if numero[i] == self.numero_secreto:
                print(f"¡Felicidades {self.name}. Has adivinado el número {self.numero_secreto} en {self.intentos_actuales} intentos.")
                return True

        


        if self.intentos_actuales == self.intentos_maximos:
            print(f"Te has quedado sin intentos {self.name}. El número correcto era {self.numero_secreto}.")
            return True

        return False

    def jugar(self):
        # Método principal para ejecutar el juego.
        print(f"Adivina el número entre {limite_inferior} y {limite_superior}")
        
        while True:
            try:
                # Solicita al usuario que ingrese un número y procesa el intento.
                intento = []
                print("Ingresa tres números")
                for i in range(0,3):
                    attempt = int(input("Introuce un número: "))
                    intento.append(attempt)
                if self.adivinar_numero(intento):
                    break
            except ValueError:
                print("Por favor, ingresa un número válido.")

# Ejemplo de uso
if __name__ == "__main__":
    limite_inferior = 1
    limite_superior = 100
    nombre = input("Introduce tu nombre: ")
    juego = JuegoAdivinaNumero(limite_inferior, limite_superior,nombre)
    juego.jugar()
