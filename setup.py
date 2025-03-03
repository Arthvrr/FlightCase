import subprocess
import tkinter as tk
from tkinter import messagebox

def run_resolution_script(resolution, video_url):
    """Lance le fichier Python correspondant à la résolution demandée."""
    try:
        resolution_scripts = {
            "720p": "720p.py",
            "1080p": "1080p.py",
            "1440p": "1440p.py",
            "best": "best.py",
            "mp3": "mp3.py"
        }

        if resolution not in resolution_scripts:
            messagebox.showerror("Erreur", f"Résolution {resolution} non valide. Choisissez parmi 720p, 1080p, 1440p, best, ou mp3.")
            return

        if not video_url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL valide.")
            return

        script_name = resolution_scripts[resolution]
        print(f"Lancement du téléchargement pour la résolution {resolution} avec l'URL {video_url}...")
        subprocess.run(["python3", script_name, video_url], check=True)

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'exécution du script {script_name}: {e}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur inattendue est survenue : {e}")

def create_gui():
    """Crée l'interface graphique."""
    root = tk.Tk()
    root.title("FlightCase")
    root.geometry("600x300")
    root.minsize(600,300)

    # Ajouter une icône à la fenêtre (ici, "icon.ico" est le fichier d'icône)
    try:
        root.iconbitmap('./icon.ico')  # Assurez-vous d'avoir un fichier "icon.ico" dans le même dossier
    except:
        pass  # Ignore l'erreur si l'icône n'est pas trouvée

    # Créer un conteneur centré
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Créer un label pour l'URL
    url_label = tk.Label(frame, text="Entrez l'URL de la vidéo YouTube :")
    url_label.pack(pady=10)

    # Champ de saisie pour l'URL
    url_entry = tk.Entry(frame, width=50)
    url_entry.pack(pady=10)

    # Créer un label pour la résolution
    resolution_label = tk.Label(frame, text="Choisissez la résolution du téléchargement :")
    resolution_label.pack(pady=10)

    # Créer un menu déroulant pour choisir la résolution
    resolution_var = tk.StringVar(value="720p")
    resolutions = ["720p", "1080p", "1440p", "BEST", "MP3"]
    resolution_menu = tk.OptionMenu(frame, resolution_var, *resolutions)
    resolution_menu.pack(pady=10)

    # Fonction pour récupérer l'URL, la résolution et exécuter le script
    def on_submit():
        resolution = resolution_var.get().strip().lower()
        video_url = url_entry.get().strip()
        run_resolution_script(resolution, video_url)

    # Ajouter un bouton pour soumettre la sélection
    submit_button = tk.Button(frame, text="Lancer", command=on_submit)
    submit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


