import instaloader
import re
import time
import random
import pandas as pd
from datetime import datetime

# Inicializar Instaloader y login con sesión guardada
L = instaloader.Instaloader(dirname_pattern=".", download_pictures=False,
                            download_videos=False, download_video_thumbnails=False,
                            download_geotags=False, download_comments=False)

USERNAME = "_felidev"

try:
    L.load_session_from_file(USERNAME)
except FileNotFoundError:
    print("⚠️  No se encontró sesión guardada. Inicia sesión manualmente una vez:")
    L.login(USERNAME, "m5HRcuhl4u*-")
    L.save_session_to_file()

# Cuentas objetivo
cuentas_objetivo = ["elcorteingles", "mercadona", "carrefoures"]
seguidores_datos = []

for cuenta in cuentas_objetivo:
    print(f"🔍 Procesando cuenta: @{cuenta}")
    perfil = instaloader.Profile.from_username(L.context, cuenta)
    seguidores = perfil.get_followers()
    total = perfil.followers
    print(f"   Total seguidores: {total}")

    count = 0
    for seguidor in seguidores:
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

                # Obtener fecha de la primera publicación (si existe)
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

            if count % 100 == 0:
                print(f"   Procesados: {count}/{total}")
                time.sleep(random.uniform(5, 10))  # pausa anti-baneo

        except Exception as e:
            print(f"   ⚠️ Error al procesar @{seguidor.username}: {e}")

# Exportar a Excel
df = pd.DataFrame(seguidores_datos)
df.to_excel("seguidores_instagram.xlsx", index=False)
print("✅ Archivo 'seguidores_instagram.xlsx' generado con éxito.")
