from collections import Counter
from typing import List

def numero_mas_frecuente(lista: List[int]) -> int:
    if not lista:
        raise ValueError("La lista no puede estar vacía.")

    frecuencia = Counter(lista)
    max_frecuencia = max(frecuencia.values())
    numeros_mas_comunes = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    return min(numeros_mas_comunes)

# Ejemplos de uso
if __name__ == "__main__":
    print(numero_mas_frecuente([1, 3, 1, 3, 2, 1]))  # 1
    print(numero_mas_frecuente([4, 4, 5, 5]))        # 4
