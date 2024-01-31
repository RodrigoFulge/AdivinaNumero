import random

class JuegoAdivinaNumero:
    def __init__(self, limite_inferior, limite_superior):
        # Inicializa el juego con un número secreto aleatorio entre los límites proporcionados.
        self.numero_secreto = random.randint(limite_inferior, limite_superior)
        # Establece el número máximo de intentos permitidos.
        self.intentos_maximos = 5
        # Inicializa el contador de intentos actuales.
        self.intentos_actuales = 0

    def adivinar_numero(self, numero):
        # Método para procesar el intento de adivinar un número.
        self.intentos_actuales += 1

        if numero == self.numero_secreto:
            print(f"¡Felicidades! Has adivinado el número {self.numero_secreto} en {self.intentos_actuales} intentos.")
            return True
        elif numero < self.numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

        if self.intentos_actuales == self.intentos_maximos:
            print(f"Te has quedado sin intentos. El número correcto era {self.numero_secreto}.")
            return True

        return False

    def jugar(self):
        # Método principal para ejecutar el juego.
        print("Créditos del juego:")
        creditos = [
            "Versión: 1.0",
            "Fecha de lanzamiento: 30 de enero de 2024"
        ]
        #Los creditos
        print(f"{creditos}\nHecho por: Avila Delgado José Daniel, Luna Soberanes Isai, Meneses Canales Maria Fernanda, Quintanar Ruis Luis Rodrigo")

        print(f"\nAdivina el número entre {limite_inferior} y {limite_superior}")

        while True:
            try:
                # Solicita al usuario que ingrese un número y procesa el intento.
                intento = int(input("Ingresa tu número: "))
                if self.adivinar_numero(intento):
                    break
            except ValueError:
                print("Por favor, ingresa un número válido.")

# Ejemplo de uso
if __name__ == "__main__":
    limite_inferior = 1
    limite_superior = 100
    juego = JuegoAdivinaNumero(limite_inferior, limite_superior)
    juego.jugar()
