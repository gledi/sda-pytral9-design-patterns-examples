import datetime

from calendar import Event, Student


def test_event_calc_amount_should_calculate_payment():
    # Arrange (Given)
    expected = 100
    student = Student("John Lennon", 100)
    sut = Event(
        student,
        "Lecture on Math with John",
        datetime.datetime(2023, 1, 15, 15, 0, 0),
        datetime.datetime(2023, 1, 15, 16, 0, 0),
    )
    # Act (When)
    actual = sut.calc_amount()
    # Assert (Then)
    assert actual == expected
