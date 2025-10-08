

from lib.music_tracker import *

# test list is initially empty list

def test_initially_empty_list():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []


# test adding single track creates list of one

def test_add_single_track_creates_list():
    tracker = MusicTracker()
    tracker.add_track("Rainbow High - Rachel Zegler")
    assert tracker.list_tracks() == ["Rainbow High - Rachel Zegler"]


# test multiple tracks added in order

def test_add_multiple_tracks_preserves_order():
    tracker = MusicTracker()
    tracker.add_track("Rainbow High - Rachel Zegler")
    tracker.add_track("Poetry - Devin Kennedy")
    tracker.add_track("Papasito - Karol G")
    assert tracker.list_tracks() == ["Rainbow High - Rachel Zegler", "Poetry - Devin Kennedy", "Papasito - Karol G"]


# doesn't add duplicate tracks (case insensitive)

def test_does_not_add_duplicate_tracks_case_insensitive():
    tracker = MusicTracker()
    tracker.add_track("Papasito - Karol G")
    tracker.add_track("papasito - KAROL G")
    assert tracker.list_tracks() == ["Papasito - Karol G"]

    
