import cv2
import easyocr
import os

# Initialisation (Russe + Anglais)
print("Initialisation de l'IA...")
reader = easyocr.Reader(['ru', 'en']) 

def extraction_ia(video_path):
    if not os.path.exists(video_path):
        print(f"Erreur : Le fichier est introuvable ici : {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    print(f"--- Analyse en cours sur : {video_path} ---")

    # On scanne toutes les 5 secondes jusqu'à la fin
    for sec in range(0, 100, 5): 
        cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        success, frame = cap.read()
        
        if not success: break
        
        # L'IA analyse toute l'image
        resultats = reader.readtext(frame)
        
        if resultats:
            # On extrait juste le texte de chaque résultat
            phrases = [res[1] for res in resultats]
            print(f"[{sec}s] : {' | '.join(phrases)}")
        else:
            print(f"[{sec}s] : (Rien)")

    cap.release()
    print("--- Fin de l'analyse ---")

# --- L'APPEL QUI LANCE TOUT ---
chemin_final = r"C:\Users\Exenia\Videos\projet 20025\jour3.mp4"
extraction_ia(chemin_final)
