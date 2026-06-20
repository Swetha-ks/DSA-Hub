from flask import Blueprint, render_template, request

playlist_app = Blueprint("playlist_app", __name__, template_folder="templates")

class Song:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class CircularPlaylist:
    def __init__(self):
        self.current = None

    def add_song(self, title):
        new_song = Song(title)
        if self.current is None:
            self.current = new_song
            new_song.next = new_song
            new_song.prev = new_song
        else:
            last = self.current.prev
            last.next = new_song
            new_song.prev = last
            new_song.next = self.current
            self.current.prev = new_song

    def play(self):
        if self.current:
            return f"🎶 Now Playing: {self.current.title}"
        return "No songs in playlist."

    def next_song(self):
        if self.current:
            self.current = self.current.next
            return self.play()

    def prev_song(self):
        if self.current:
            self.current = self.current.prev
            return self.play()

    def get_playlist(self):
        if not self.current:
            return []
        temp = self.current
        songs = []
        while True:
            songs.append(temp.title)
            temp = temp.next
            if temp == self.current:
                break
        return songs

playlist = CircularPlaylist()

@playlist_app.route("/", methods=["GET", "POST"])
def playlist_index():
    if request.method == "POST":
        title = request.form["song"]
        playlist.add_song(title)
    songs = playlist.get_playlist()
    status = playlist.play()
    return render_template("playlist.html", songs=songs, status=status)

@playlist_app.route("/next")
def playlist_next():
    status = playlist.next_song()
    songs = playlist.get_playlist()
    return render_template("playlist.html", songs=songs, status=status)

@playlist_app.route("/prev")
def playlist_prev():
    status = playlist.prev_song()
    songs = playlist.get_playlist()
    return render_template("playlist.html", songs=songs, status=status)
