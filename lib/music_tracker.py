



# add tracks to list of tracks and be able to return that list.
# added tracks include artist (string)
# added tracks must be unique

class MusicTracker():
    def __init__(self):
        self.tracks = []

    def add_track(self, name: str):

        tracks_lower = [tr.lower() for tr in self.tracks] 
        if name.lower() not in tracks_lower:
            self.tracks.append(name)

    def list_tracks(self):
        return self.tracks
    


if __name__ == "__main__":
    my_tracker = MusicTracker()
    my_tracker.add_track("Poetry - Devin Kennedy")
    my_tracker.add_track("Papasito - Karol G")
    print(my_tracker.list_tracks())
    
