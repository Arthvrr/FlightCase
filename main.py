import subprocess
import sys

def run_resolution_script(resolution):
    """Lance le fichier Python correspondant à la résolution demandée."""
    try:
        # Dictionnaire qui associe la résolution au fichier Python à exécuter
        resolution_scripts = {
            "720p": "720p.py",
            "1080p": "1080p.py",
            "1440p": "1440p.py",
            "best": "best.py",
            "worst": "worst.py"
        }

        # Vérifier si la résolution est valide
        if resolution not in resolution_scripts:
            print(f"Résolution {resolution} non valide. Choisissez parmi 720p, 1080p, 1440p, best, ou worst.")
            sys.exit(1)

        # Lancer le script correspondant à la résolution
        script_name = resolution_scripts[resolution]
        print(f"Lancement du téléchargement pour la résolution {resolution}...")
        subprocess.run(["python3", script_name], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script {script_name}: {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

def main():
    """Point d'entrée du programme."""
    # Demander la résolution à l'utilisateur
    resolution = input("Entrez la résolution (720p, 1080p, 1440p, best, worst) : ").strip().lower()

    # Lancer le script correspondant à la résolution
    run_resolution_script(resolution)

if __name__ == "__main__":
    main()