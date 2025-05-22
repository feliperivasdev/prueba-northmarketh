import requests
from bs4 import BeautifulSoup

def buscar_productos(palabra_clave=""):
    url = f"https://listado.mercadolibre.com.co/{palabra_clave}"
    headers = {"User-Agent": "Mozilla/5.0"}

    respuesta = requests.get(url, headers=headers)
    soup = BeautifulSoup(respuesta.text, "html.parser")

    resultados = soup.select("li.ui-search-layout__item")[:5]
    print(f"Resultados encontrados: {len(resultados)}")

    for producto in resultados:
        # Título
        titulo_tag = producto.select_one("h3.poly-component__title-wrapper a.poly-component__title")
        titulo = titulo_tag.text.strip() if titulo_tag else "No encontrado"

        # Precio actual
        precio_tag = producto.select_one("div.poly-price__current span.andes-money-amount__fraction")
        precio = precio_tag.text.strip() if precio_tag else "No encontrado"

        print(f"Título: {titulo}")
        print(f"Precio: {precio}\n")

if __name__ == "__main__":
    palabra = input("Ingrese la palabra clave a buscar: ")
    buscar_productos(palabra)
