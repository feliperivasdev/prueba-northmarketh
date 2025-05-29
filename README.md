# Prueba de Ingreso - Desarrollador Junior North Marketh

Este repositorio contiene la solución a la prueba técnica para el rol de Desarrollador Junior en North Marketh. A continuación, se detallan los ejercicios realizados, las instrucciones de instalación y ejecución, y los datos del autor.

---

## 📬 Autor

Desarrollado por **David Felipe Gustin Rivas**  
Correo: gustinrivasdavid@gmail.com  
GitHub: [https://github.com/feliperivasdev](https://github.com/feliperivasdev)

---

## 📦 Instalación y Configuración

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
**Archivo:** `ejercicio1/numero_mas_frecuente.py`  
- **Descripción:** Identifica el número que más veces se repite en una lista.
- **Características:**
  - Devuelve el menor si hay empate.
  - Manejo de errores si la lista está vacía.
- **Tecnologías Utilizadas:** Python, `collections.Counter`
- **Ejecución:**
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
**Archivo:** `ejercicio2/scraping_mercadolibre.py`  
- **Descripción:** Extrae títulos y precios de productos en MercadoLibre Colombia.
- **Características:**
  - Los primeros 5 resultados.
  - Entrada de palabra clave desde la consola.
- **Tecnologías Utilizadas:** Python, `requests`, `BeautifulSoup`
- **Ejecución:**
```bash
python scraping_mercadolibre.py
```
**Entrada:**
```
Ingrese la palabra clave a buscar: telefono
```
**Salida esperada:**
```
Resultados encontrados: 5
Título: Teléfono XYZ
Precio: $123.456
...
```

---

### ✅ Ejercicio 3: Aplicación GUI + API NASA
**Archivos:**  
- `ejercicio3/app.py`  
- `ejercicio3/db.sqlite3`  
- **Descripción:** Login con interfaz gráfica y consumo de la API APOD (NASA).
- **Características:**
  - Validación de usuario.
  - Visualización de imagen astronómica del día.
- **Tecnologías Utilizadas:** Python, `tkinter`, `sqlite3`, `requests`
- **Usuario de prueba:**
```bash
Usuario: DavidGustin
Contraseña: prueba2025
```
- **Ejecución:**
```bash
python app.py
```

---

### ✅ Ejercicio 4: Scraping de Seguidores de Instagram
**Archivo:** `ejercicio4_instagram/scrape_instagram.py`  
- **Descripción:** Obtiene la lista de seguidores de las cuentas:
  - `@elcorteingles`, `@mercadona`, `@carrefoures`
- **Características:**
  - Para perfiles públicos: extrae nombre, correos, teléfonos, fecha de primera publicación.
  - Para perfiles privados: solo nombre; los demás campos se marcan como `Perfil privado`.
  - Evita bloqueos usando intervalos entre bloques de 100.
- **Tecnologías Utilizadas:** Python, `instaloader`, `re`, `pandas`, `Excel`
- **Ejecución:**
```bash
python scrape_instagram.py
```

**Requisitos especiales:**
- Iniciar sesión con tu cuenta de Instagram la primera vez (se guarda sesión).
- Archivo de salida: `seguidores_instagram.xlsx`

**Advertencia ética:**
- Este script es solo con fines educativos. No debe usarse para fines maliciosos.
- Respeta la privacidad y condiciones de uso de Instagram.

---

## 🔒 Seguridad

- Contraseñas no se almacenan en código fuente (se recomienda usar sesión guardada).
- Scraping responsable con limitación de solicitudes.

---

## 📚 Estructura del Proyecto

```
prueba-northmarketh/
├── ejercicio1/
│   └── numero_mas_frecuente.py
├── ejercicio2/
│   └── scraping_mercadolibre.py
├── ejercicio3/
│   ├── app.py
│   ├── db.sqlite3
├── ejercicio4_instagram/
│   └── scrape_instagram.py
│   └── seguidores_instagram.xlsx (se genera tras ejecutar)
├── requirements.txt
└── README.md
```
