

from lib.counter import *

def test_counter_reports_zero_initially():
    self = Counter()
    assert self.count == 0


def test_add_increases_count_by_number():
    self = Counter()
    self.add(4)
    assert self.count == 4

def test_add_multiple_times_count():
     self = Counter()
     self.add(2)
     self.add(11)
     assert self.count == 13

def test_report_returns_correct_message():
    self = Counter()
    self.add(10)
    result = self.report()
    assert result == "Counted to 10 so far."


