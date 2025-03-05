import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import threading
import sys

class RedirectOutput:
    """Classe pour rediriger stdout/stderr vers un widget Text."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)  # Scroll automatique

    def flush(self):
        pass  # Nécessaire pour certaines bibliothèques


def run_resolution_script(resolution, video_url, output_text):
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
            output_text.insert(tk.END, f"Erreur: Résolution {resolution} non valide.\n")
            output_text.see(tk.END)
            return

        if not video_url:
            output_text.insert(tk.END, "Erreur: Veuillez entrer une URL valide.\n")
            output_text.see(tk.END)
            return

        script_name = resolution_scripts[resolution]
        output_text.insert(tk.END, f"Lancement du téléchargement pour la résolution {resolution} avec l'URL {video_url}...\n")
        output_text.see(tk.END)

        # Processus pour exécuter le script avec forçage de l'overwrite
        process = subprocess.Popen(
            ["python3", script_name, video_url, "--force-overwrites", "--no-continue"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Envoyer "y\n" pour forcer l'overwrite
        process.stdin.write("y\n")
        process.stdin.flush()
        process.stdin.close()

        # Lire les sorties stdout et stderr
        def read_output(pipe, prefix=""):
            for line in iter(pipe.readline, ""):
                output_text.insert(tk.END, f"{prefix}{line}")
                output_text.see(tk.END)
            pipe.close()

        threading.Thread(target=read_output, args=(process.stdout, "")).start()
        threading.Thread(target=read_output, args=(process.stderr, "Erreur: ")).start()

        process.wait()

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur inattendue est survenue : {e}")


def create_gui():
    """Crée l'interface graphique."""
    root = tk.Tk()
    root.title("FlightCase")
    root.geometry("600x300")  # Taille initiale de la fenêtre
    root.minsize(600,300)

    try:
        root.iconbitmap('icon.ico')  # Assurez-vous d'avoir un fichier "icon.ico" dans le même dossier
    except:
        pass  # Ignore l'erreur si l'icône n'est pas trouvée

    # Créer un conteneur principal qui s'étend sur toute la fenêtre
    root_frame = tk.Frame(root)
    root_frame.pack(expand=True, fill=tk.BOTH)

    # Créer un sous-conteneur pour centrer les widgets
    frame = tk.Frame(root_frame)
    frame.pack(expand=True)

    # Créer un label pour l'URL
    url_label = tk.Label(frame, text="Entrez l'URL de la vidéo YouTube :")
    url_label.pack(pady=5)

    # Champ de saisie pour l'URL
    url_entry = tk.Entry(frame, width=50)
    url_entry.pack(pady=5)

    # Créer un label pour la résolution
    resolution_label = tk.Label(frame, text="Choisissez la résolution du téléchargement :")
    resolution_label.pack(pady=5)

    # Créer un menu déroulant pour choisir la résolution
    resolution_var = tk.StringVar(value="720p")
    resolutions = ["720p", "1080p", "1440p", "BEST", "MP3"]
    resolution_menu = tk.OptionMenu(frame, resolution_var, *resolutions)
    resolution_menu.pack(pady=5)

    # Zone de texte pour afficher les sorties
    output_text = ScrolledText(frame, wrap=tk.WORD, height=5, width=63)
    output_text.pack(padx=10, pady=10)

    # Rediriger stdout et stderr vers le widget Text
    sys.stdout = RedirectOutput(output_text)
    sys.stderr = RedirectOutput(output_text)

    # Fonction pour récupérer l'URL, la résolution et exécuter le script
    def on_submit():
        resolution = resolution_var.get().strip().lower()
        video_url = url_entry.get().strip()
        threading.Thread(target=run_resolution_script, args=(resolution, video_url, output_text)).start()

    # Ajouter un bouton pour soumettre la sélection
    submit_button = tk.Button(frame, text="Lancer", command=on_submit)
    submit_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()