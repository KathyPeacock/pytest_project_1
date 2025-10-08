

from lib.music_tracker import *

# test list is initially empty list

def test_initially_empty_list():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []


# test adding single track creates list of one

def test_add_single_track_creates_list():
    tracker = MusicTracker()
    tracker.add_track(Track("Rainbow High", "Rachel Zegler"))
    assert tracker.list_tracks() == ["Rainbow High by Rachel Zegler"]

def test_add_and_list_multiple_tracks_preserves_order():
    tracker = MusicTracker()
    track_1 = Track("Poetry", "Devin Kennedy")
    track_2 = Track("Papasito", "Karol G")
    track_3 = Track("Nothing", "Bruno Major")

    tracker.add_track(track_1)
    tracker.add_track(track_2)
    tracker.add_track(track_3)

    assert tracker.list_tracks() == ["Poetry by Devin Kennedy", "Papasito by Karol G", "Nothing by Bruno Major"]


# test multiple tracks added in order

# def test_add_multiple_tracks_preserves_order():
#     tracker = MusicTracker()
#     tracker.add_track("Rainbow High - Rachel Zegler")
#     tracker.add_track("Poetry - Devin Kennedy")
#     tracker.add_track("Papasito - Karol G")
#     assert tracker.list_tracks() == ["Rainbow High - Rachel Zegler", "Poetry - Devin Kennedy", "Papasito - Karol G"]


# doesn't add duplicate tracks (case insensitive)

def test_does_not_add_duplicate_tracks_case_different():
    tracker = MusicTracker()
    tracker.add_track(Track("Papasito", "Karol G"))
    tracker.add_track(Track("papasito", "KAROL G"))
    assert tracker.list_tracks() == ["Papasito by Karol G"]

def test_does_not_add_duplicate_tracks_case_same():
    tracker = MusicTracker()
    tracker.add_track(Track("Papasito", "Karol G"))
    tracker.add_track(Track("Papasito", "Karol G"))
    assert tracker.list_tracks() == ["Papasito by Karol G"]

    
def test_track_format_returns_title_by_artist():
    track = Track("Nothing", "Bruno Major")
    assert track.format() == "Nothing by Bruno Major"
