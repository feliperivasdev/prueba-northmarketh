import instaloader
import re
import time
import random
import pandas as pd
import json
from datetime import datetime


# Configuración de sesión


L = instaloader.Instaloader(
    dirname_pattern=".",
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False
)

# Leer credenciales desde JSON 
try:
    with open("insta_credentials.json") as f:
        creds = json.load(f)
        USERNAME = creds["USERNAME"]
        PASSWORD = creds["PASSWORD"]
except Exception as e:
    print(f" Error al cargar las credenciales: {e}")
    exit()

# Iniciar sesión o cargar sesión guardada
try:
    L.load_session_from_file(USERNAME)
    print(f"Sesión cargada correctamente para: {USERNAME}")
except FileNotFoundError:
    print("  No se encontró sesión guardada. Iniciando login manual...")
    L.login(USERNAME, PASSWORD)
    L.save_session_to_file()
    print("Sesión guardada exitosamente.")
    time.sleep(10)  # Pausa preventiva tras el login


# Scraping de seguidores


cuentas_objetivo = ["elcorteingles", "mercadona", "carrefoures"]
seguidores_datos = []

for cuenta in cuentas_objetivo:
    print(f"\n🔍 Procesando cuenta: @{cuenta}")
    try:
        perfil = instaloader.Profile.from_username(L.context, cuenta)
        seguidores = perfil.get_followers()
        total = perfil.followers
        print(f"   Total seguidores: {total}")
    except instaloader.exceptions.ConnectionException as e:
        print(f"Error al acceder a @{cuenta}: {e}")
        print("Espera unos minutos e intenta de nuevo.")
        continue

    count = 0
    for seguidor in seguidores:
        if count >= 10:
            break
        try:
            data = {
                "Cuenta Origen": cuenta,
                "Usuario": seguidor.username,
                "Nombre Completo": seguidor.full_name
            }

            if seguidor.is_private:
                data.update({
                    "Correo(s)": "Perfil privado",
                    "Teléfono(s)": "Perfil privado",
                    "Fecha Primera Publicación": "Perfil privado"
                })
            else:
                bio = seguidor.biography
                correos = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", bio)
                telefonos = re.findall(r"\+?\d[\d\s.-]{7,}\d", bio)

                publicaciones = seguidor.get_posts()
                primera_fecha = None
                for post in publicaciones:
                    primera_fecha = post.date_utc.strftime("%Y-%m-%d")
                    break

                data.update({
                    "Correo(s)": ", ".join(correos) if correos else "No disponible",
                    "Teléfono(s)": ", ".join(telefonos) if telefonos else "No disponible",
                    "Fecha Primera Publicación": primera_fecha or "No disponible"
                })

            seguidores_datos.append(data)
            count += 1

            time.sleep(random.uniform(2, 4))  # Pausa aleatoria entre seguidores

        except Exception as e:
            print(f"   Error con @{seguidor.username}: {e}")

    time.sleep(random.uniform(10, 15))  # Pausa aleatoria entre cuentas


# Exportar a Excel


try:
    df = pd.DataFrame(seguidores_datos)
    df.to_excel("seguidores_instagram.xlsx", index=False)
    print("\n Archivo 'seguidores_instagram.xlsx' generado con éxito.")
except Exception as e:
    print(f" Error al guardar Excel: {e}")
