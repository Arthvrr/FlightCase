import subprocess

def download_youtube_video():
    try:
        # Demander l'URL de la vidéo
        url = input("Entrez l'URL de la vidéo YouTube : ").strip()
        
        # Commande yt-dlp pour télécharger le meilleur fichier MP4 disponible
        command = [
            "yt-dlp",
            "-S", "height:720",  # Prioriser les résolutions à partir de 720p
            "-f", "best[ext=mp4]",  # Télécharger le meilleur flux MP4 (vidéo + audio combinés)
            "--output", "%(title)s.%(ext)s",  # Utiliser le titre de la vidéo pour nommer le fichier
            url
        ]
        
        # Exécuter la commande
        print("Téléchargement en cours...")
        subprocess.run(command, check=True)
        print("Téléchargement terminé avec succès !")
    except subprocess.CalledProcessError as e:
        print(f"Une erreur s'est produite lors du téléchargement : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    download_youtube_video()

#https://youtu.be/fzepGtfHL9A?si=Hl0fUqO4KVCcmxi7

print("Hello, World!")
