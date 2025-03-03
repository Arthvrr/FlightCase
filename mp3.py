# import subprocess
# import os
# import platform

# def download_youtube_video():
#     try:
#         # Demander l'URL de la vidéo
#         url = input("Entrez l'URL de la vidéo YouTube : ").strip()

#         # Si pas d'URL fournie, télécharge cette vidéo par défaut (Wii Party Soundtrack)
#         if not url:
#             url = "https://youtu.be/fzepGtfHL9A?si=Hl0fUqO4KVCcmxi7"

#         # Détecter le système d'exploitation et obtenir le chemin du dossier "Downloads"
#         if platform.system() == "Darwin" or platform.system() == "Linux":
#             # Sur macOS et Linux, utiliser le dossier Downloads dans le répertoire utilisateur
#             downloads_folder = os.path.expanduser("~/Downloads")
#         elif platform.system() == "Windows":
#             # Sur Windows, utiliser le chemin de l'environnement de l'utilisateur
#             downloads_folder = os.path.join(os.environ["USERPROFILE"], "Downloads")
#         else:
#             raise Exception("Système d'exploitation non pris en charge")

#         # Commande yt-dlp pour télécharger l'audio MP3 de la meilleure qualité disponible dans le dossier Downloads
#         command = [
#             "yt-dlp",
#             "-f", "bestaudio",  # Télécharger le meilleur flux audio
#             "--extract-audio",  # Extraire l'audio de la vidéo
#             "--audio-format", "mp3",  # Convertir l'audio en MP3
#             "--audio-quality", "0",  # Meilleure qualité audio possible (0 = qualité maximale)
#             "--output", os.path.join(downloads_folder, "%(title)s.%(ext)s"),  # Télécharger dans le dossier Downloads
#             url
#         ]
        
#         # Exécuter la commande
#         print("Téléchargement en cours...")
#         subprocess.run(command, check=True)
#         print("Téléchargement terminé avec succès !")
#     except subprocess.CalledProcessError as e:
#         print(f"Une erreur s'est produite lors du téléchargement : {e}")
#     except Exception as e:
#         print(f"Une erreur inattendue s'est produite : {e}")

# if __name__ == "__main__":
#     download_youtube_video()

import sys
import subprocess
import os
import platform

def download_youtube_audio(url):
    try:
        if not url:
            raise ValueError("L'URL de la vidéo YouTube est obligatoire.")

        # Détecter le système d'exploitation et obtenir le chemin du dossier "Downloads"
        if platform.system() == "Darwin" or platform.system() == "Linux":
            downloads_folder = os.path.expanduser("~/Downloads")
        elif platform.system() == "Windows":
            downloads_folder = os.path.join(os.environ["USERPROFILE"], "Downloads")
        else:
            raise Exception("Système d'exploitation non pris en charge")

        # Commande yt-dlp pour télécharger l'audio MP3 de la meilleure qualité disponible
        command = [
            "yt-dlp",
            "-f", "bestaudio",  # Télécharger le meilleur flux audio
            "--extract-audio",  # Extraire l'audio de la vidéo
            "--audio-format", "mp3",  # Convertir l'audio en MP3
            "--audio-quality", "0",  # Meilleure qualité audio possible (0 = qualité maximale)
            "--output", os.path.join(downloads_folder, "%(title)s.%(ext)s"),  # Télécharger dans le dossier Downloads
            url
        ]

        print("Téléchargement en cours...")
        subprocess.run(command, check=True)
        print("Téléchargement terminé avec succès !")
    except subprocess.CalledProcessError as e:
        print(f"Une erreur s'est produite lors du téléchargement : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erreur : Veuillez fournir une URL YouTube comme argument.")
        sys.exit(1)

    video_url = sys.argv[1]
    download_youtube_audio(video_url)