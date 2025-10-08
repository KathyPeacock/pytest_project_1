



# add tracks to list of tracks and be able to return that list.
# added tracks include artist (string)
# added tracks must be unique

class MusicTracker():
    def __init__(self):
        self.tracks = []

# NB I had to change this lower case method for checking duplicates
# so it deals with self.tracks which holds OBJECTS not strings.

    def add_track(self, track):
        track_str = track.format().lower()
        track_list_lower = [tr.format().lower() for tr in self.tracks]
        if track_str not in track_list_lower:
            self.tracks.append(track)

    def list_tracks(self):
        return [tr.format() for tr in self.tracks]
    


# if __name__ == "__main__":
#     my_tracker = MusicTracker()
#     my_tracker.add_track("Poetry - Devin Kennedy")
#     my_tracker.add_track("Papasito - Karol G")
#     print(my_tracker.list_tracks())
    

# MusicTracker class stored strings with both artist and song name.
# class Track will represent a song as an object
# in this object attributes for each track will be Title and Artist.
# MusicTracker will store a collection of Track objects.

class Track():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

# Make sure a nice string is returned with the track attribute info.

    def format(self):
        return f"{self.title} by {self.artist}"

if __name__ == "__main__":
    my_tracker = MusicTracker()
    track_1 = Track("Poetry", "Devin Kennedy")
    track_2 = Track("Papasito", "Karol G")

    my_tracker.add_track(track_1)
    my_tracker.add_track(track_2)

    print(my_tracker.list_tracks())