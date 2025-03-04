# import subprocess
# import os
# import platform

# def convert_webm_to_mp4(webm_path, mp4_path):
#     try:
#         # Utilisation de ffmpeg pour convertir le fichier webm en mp4
#         print(f"Conversion de {webm_path} en {mp4_path}...")
#         subprocess.run(["ffmpeg", "-i", webm_path, "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", mp4_path], check=True)
#         print("Conversion terminée avec succès !")
#     except subprocess.CalledProcessError as e:
#         print(f"Une erreur s'est produite lors de la conversion : {e}")
#     except Exception as e:
#         print(f"Une erreur inattendue s'est produite : {e}")

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

#         # Commande yt-dlp pour télécharger le meilleur fichier disponible dans le dossier Downloads
#         output_path = os.path.join(downloads_folder, "%(title)s.%(ext)s")
#         command = [
#             "yt-dlp",
#             "--output", output_path,  # Télécharger dans le dossier Downloads
#             url
#         ]
        
#         # Exécuter la commande
#         print("Téléchargement en cours...")
#         subprocess.run(command, check=True)
#         print("Téléchargement terminé avec succès !")

#         # Vérifier si le fichier téléchargé est en .webm
#         downloaded_file = None
#         for file in os.listdir(downloads_folder):
#             if file.endswith(".webm"):
#                 downloaded_file = os.path.join(downloads_folder, file)
#                 break

#         if downloaded_file:
#             # Nom du fichier de sortie en mp4
#             mp4_file = downloaded_file.replace(".webm", ".mp4")
#             # Convertir le fichier .webm en .mp4
#             convert_webm_to_mp4(downloaded_file, mp4_file)
#             # Optionnel: supprimer le fichier .webm après conversion
#             os.remove(downloaded_file)
#             print(f"Le fichier mp4 a été enregistré sous {mp4_file}")
#         else:
#             print("Aucun fichier .webm n'a été trouvé après le téléchargement.")

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

def convert_webm_to_mp4(webm_path, mp4_path):
    try:
        print(f"Conversion de {webm_path} en {mp4_path}...")
        subprocess.run(["ffmpeg", "-i", webm_path, "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", mp4_path], check=True)
        print("Conversion terminée avec succès !")
    except subprocess.CalledProcessError as e:
        print(f"Une erreur s'est produite lors de la conversion : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

def download_youtube_video(url):
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

        # Commande yt-dlp pour télécharger
        output_path = os.path.join(downloads_folder, "%(title)s.%(ext)s")
        command = [
            "yt-dlp",
            "--output", output_path,
            url
        ]
        
        print("Téléchargement en cours...")
        subprocess.run(command, check=True)
        print("Téléchargement terminé avec succès !")

        # Vérifier si le fichier téléchargé est en .webm
        downloaded_file = None
        for file in os.listdir(downloads_folder):
            if file.endswith(".webm"):
                downloaded_file = os.path.join(downloads_folder, file)
                break

        if downloaded_file:
            # Nom du fichier de sortie en mp4
            mp4_file = downloaded_file.replace(".webm", ".mp4")
            convert_webm_to_mp4(downloaded_file, mp4_file)
            os.remove(downloaded_file)
            print(f"Le fichier mp4 a été enregistré sous {mp4_file}")
        else:
            print("Aucun fichier .webm n'a été trouvé après le téléchargement.")

    except subprocess.CalledProcessError as e:
        print(f"Une erreur s'est produite lors du téléchargement : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erreur : Veuillez fournir une URL YouTube comme argument.")
        sys.exit(1)

    video_url = sys.argv[1]
    download_youtube_video(video_url)