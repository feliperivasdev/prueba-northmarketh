# Prueba de Ingreso - Desarrollador Junior North Marketh

Este repositorio contiene la solución a la prueba técnica para el rol de Desarrollador Junior en North Marketh. A continuación, se detallan los ejercicios realizados y las instrucciones para ejecutar cada uno de ellos.

---
## 📬 Autor

Desarrollado por **David Felipe Gustin Rivas**  
Correo: gustinrivasdavid@gmail.com  
GitHub: [https://github.com/feliperivasdev](https://github.com/feliperivasdev)
## 📦 Instalación y Configuración
---
### Prerrequisitos

- Python 3.9 o superior
- pip

### Pasos de Instalación

```bash
git clone https://github.com/feliperivasdev/prueba-northmarketh.git
cd prueba-northmarketh
pip install -r requirements.txt
```

---
## 🚀 Ejercicios Implementados

### ✅ Ejercicio 1: Número Más Frecuente
**Archivo:** [`ejercicio1/numero_mas_frecuente.py`](ejercicio1/numero_mas_frecuente.py) 
- **Descripción:** Función que identifica el número que más veces se repite en una lista.
- **Características:**
  - Si hay empate, retorna el menor número.
  - Manejo de errores si la lista está vacía.
- **Tecnologías Utilizadas:** Python, `collections.Counter`
- **Ejecución del Ejercicio**
```bash
python numero_mas_frecuente.py
```

**Salida esperada:**
```
1
4
```
---

### ✅ Ejercicio 2: Web Scraping
**Archivo:** [`ejercicio2/scraping_mercadolibre.py`](ejercicio2/scraping_mercadolibre.py) 
- **Descripción:** Script para extraer los títulos y precios de productos desde MercadoLibre Colombia.
- **Características:**
  - Extrae los primeros 5 resultados de búsqueda.
  - Permite modificar fácilmente la palabra clave.
  - Imprime los resultados por consola.
- **Tecnologías Utilizadas:** Python, `requests`, `BeautifulSoup`
- **Ejecución del Ejercicio**
```bash
python scraping_mercadolibre.py
```

**Para cambiar la palabra de búsqueda:**

En la consola cada que ejecutes el script te pedira la palabra clave:

```bash
Ingrese la palabra clave a buscar: telefono  # Cambiar por el término deseado
```

**Salida esperada:**

```
Resultados encontrados: 5
Título: Telefono De Flecha Mobulaa M2406 Dual Sim 4g Estilo Flip
Precio: 179.800

Título: Teléfono Inteligente Pequeño Y Práctico Soyes Xs11 - Doble C
Precio: 203.354
...
```
---

### ✅ Ejercicio 3: Aplicación GUI
**Archivos:**  
- [`ejercicio3/app.py`](ejercicio3/app.py): Aplicación de escritorio con Tkinter que permite iniciar sesión de forma segura (hash SHA-256) y, tras autenticación, muestra la imagen astronómica del día de la NASA (APOD) usando su API pública.
- [`ejercicio3/db.sqlite3`](ejercicio3/db.sqlite3): Base de datos SQLite con la tabla de usuarios.
- **Descripción:** Aplicación con interfaz gráfica para login y visualización de datos desde una API pública.
- **Características:**
  - Ventana de login con validación.
  - Autenticación contra base de datos SQLite.
  - Tras un login exitoso, muestra la imagen astronómica del día de la NASA.
  - Interfaz limpia y funcional usando Tkinter.
- **Tecnologías Utilizadas:** Python, `tkinter`, `sqlite3`, `requests`
- **Ejecución del Ejercicio**
```bash
python app.py
```

**Usuarios de prueba disponibles:**

- *Usuario:* `DavidGustin`
- *Contraseña:* `prueba2025`

**Funcionalidades:**

- Ventana de login con validación.
- Autenticación contra base de datos SQLite.
- Después del login exitoso, se muestra una ventana emergente con una imagen  de del dia desde la API de la Nasa.
- Interfaz limpia y profesional con `tkinter`.
---

## 🔒 Seguridad

- La contraseña se almacenano hasheada.
- Las consultas SQL están parametrizadas para evitar inyección SQL.

---
## 📚 Estructura del Proyecto

```
prueba-northmarketh/
│
├── ejercicio1/
│   └── numero_mas_frecuente.py
│
├── ejercicio2/
│   └── scraping_mercadolibre.py
│
├── ejercicio3/
│   ├── app.py
│   ├── db.sqlite3
│
├── requirements.txt
└── README.md
```


