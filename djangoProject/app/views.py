
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# funkcja odpowiadająca z logikę
def index(request, *args, **kwargs):
        #id playlisty oraz dane potrzebne do "zalogowania się" aby pobierać dane z API
        playlist_uri = 'spotify:playlist:37i9dQZEVXbMDoHDwVN2tF'
        client = '...'
        secret = '...'
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=client,
            client_secret=secret))
        #wyszukanie playlisty z top 10 utworów
        results = spotify.playlist_items(playlist_uri, fields='items.track.id, items.track.name, items.track.artists.name, total')
        final_result = results['items'][:10]
        #pobranie wszystkich gatunków muzycznych na spotify
        results_Genre = spotify.recommendation_genre_seeds()
        final_result_Genre = results_Genre['genres']

        #metoda POST jeśli ktoś wybrał dany gatunek
        if request.method == 'POST':
                genre_uri = request.POST.get("uri")
                results_Rec = spotify.recommendations(seed_genres=[genre_uri])
                final_result_Rec = results_Rec['tracks']

                return render(request, 'appgenre.html', {"results_Genre": final_result_Genre, "results_Rec": final_result_Rec, "genre": genre_uri})

        elif request.method == 'GET':
                return render(request, 'appbase.html', {"results": final_result, "results_Genre": final_result_Genre})
        else:
                #to zwróci się jeśli przycisk nie jest kliknięty
                return render(request, 'appbase.html', {"results": final_result, "results_Genre": final_result_Genre})
