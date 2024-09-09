from yt_dlp import YoutubeDL
import os


class YoutubeDownloader:

    def __init__(self):

        # self.nom_dossier = input("Entrer le nom du dossier qui contiendra votre téléchargement\n\n   ==> ")
        
        self.ydl_opts_video = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        self.ydl_opts_playlist = {
            'format': 'best',
            'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
            'noplaylist': False,
        }


    # Pour recuperer l'url d'une seul video
    def url_video(self):
        url = input("\n ----- Lien ==  ")  # Remplace par l'URL de la playlist
        self._telechargeur(url, self.ydl_opts_video)


    # Pour recuperer l'url d'une seul video
    def url_playlist(self):
        url = input("\n ----- Lien ==  ")  # Remplace par l'URL de la playlist
        self._telechargeur(url, self.ydl_opts_playlist)


    def _telechargeur(self, url, option):
        # self._creation_dossier(self.nom_dossier)
        ydl = YoutubeDL(option)
        ydl.download([url])
        print("Téléchargement terminé!")


    # def _creation_dossier(self, nom_dossier):
    #     if not os.path.exists(nom_dossier):
    #         os.mkdir(nom_dossier)
    
    





"""
Info sur le package from yt_dlp import YoutubeDL :

# Extraire les informations sur la vidéo
info_dict = ydl.extract_info(url, download=False)

print()

# Afficher les métadonnées de la vidéo
print("Titre: ", info_dict.get('title', 'Titre non disponible'))
print("Nombre de vues: ", info_dict.get('view_count', 'Nombre de vues non disponible'))
print("Durée: ", info_dict.get('duration', 'Durée non disponible'), "secondes")
print("Auteur: ", info_dict.get('uploader', 'Auteur non disponible'))
print("Date de publication: ", info_dict.get('upload_date', 'Date non disponible'))
        
"""




