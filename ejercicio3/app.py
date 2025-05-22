import tkinter as tk
from tkinter import messagebox
import sqlite3
import requests
from PIL import Image, ImageTk
from io import BytesIO
import hashlib

def verificar_usuario(usuario, contraseña):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (usuario, hash_contraseña))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def obtener_apod_nasa():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        # Solo mostrar si es imagen (no video)
        if datos.get("media_type") == "image":
            return datos["title"], datos["url"], datos.get("explanation", "")
    return None, None, None

def mostrar_apod_nasa():
    titulo, url_img, descripcion = obtener_apod_nasa()
    if not titulo or not url_img:
        messagebox.showerror("Error", "No se pudo obtener la imagen de la NASA")
        return
    ventana_apod = tk.Toplevel()
    ventana_apod.title("NASA Astronomy Picture of the Day")
    ventana_apod.geometry("600x700")
    bg_color = "#1a1a1a"
    ventana_apod.configure(bg=bg_color)

    try:
        img_data = requests.get(url_img).content
        pil_img = Image.open(BytesIO(img_data)).resize((500, 400))
        tk_img = ImageTk.PhotoImage(pil_img)
        label_img = tk.Label(ventana_apod, image=tk_img, bg=bg_color)
        label_img.image = tk_img  # Mantener referencia
        label_img.pack(pady=20)
    except Exception:
        label_img = tk.Label(ventana_apod, text="No se pudo cargar la imagen", fg="white", bg=bg_color)
        label_img.pack(pady=20)

    label_titulo = tk.Label(ventana_apod, text=titulo, font=("Arial", 18, "bold"), fg="white", bg=bg_color, wraplength=550)
    label_titulo.pack(pady=10)
    label_desc = tk.Label(ventana_apod, text=descripcion, font=("Arial", 12), fg="white", bg=bg_color, wraplength=550, justify="left")
    label_desc.pack(pady=10)

def login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    if verificar_usuario(usuario, contraseña):
        mostrar_apod_nasa()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("300x150")

tk.Label(ventana, text="Usuario").pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

tk.Label(ventana, text="Contraseña").pack()
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()

tk.Button(ventana, text="Login", command=login).pack(pady=10)

ventana.mainloop()
