
# from autre_fichier import MaClasse
from youtube_downloader import YoutubeDownloader

# ---------------------------------- Groupe declaration de variable -------------------------------------------------

bienvenu = "\n\n----------------------- Bienvenu dans mon programme Scraping by Vido -------------------------------"
annonce = """

  Fait votre choix (1, 2 ou 3):
      
  1 - Telecharger une seul video
  2 - Telecharger une plalist de videos
  3 - Sortie 
"""
erreur_message = "ERREUR!!! Veuillez choisir un nombre entre 1 et 3"


def verifie_choix_utilisateur():
  while True:
    choix_telechargement = input("   => ")
    try:
      choix_telechargement_int = int(choix_telechargement)
    except:
      print(erreur_message)
    else:
      if 1 <= choix_telechargement_int <= 3:
        break
      else:
        print(erreur_message)

  return choix_telechargement_int





# ---------------------------------- Programme principal -------------------------------------------------

youtube = YoutubeDownloader()

print(bienvenu)

while True:
  print(annonce)
  choix_telechargement = verifie_choix_utilisateur()

  match choix_telechargement:
    case 1:
      youtube.url_video()
    case 2:
      youtube.url_playlist()
    case 3:
      exit()

