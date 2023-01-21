import datetime


class Student:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate


class Event:
    def __init__(self, student, title, start, end):
        self.student = student
        self.title = title
        self.start = start
        self.end = end

    def calc_amount(self):
        duration = (self.end - self.start).seconds / 3_600
        return self.student.rate * duration


class Calendar:
    def __init__(self, events):
        self.events = []

    def schedule(self, student, start, duration):
        event = Event(
            student,
            f"{student.name} session",
            start,
            start + datetime.timedelta(hours=duration),
        )
        self.events.append(event)

    def calculate_payment_amount(self, name, start_date, end_date):
        events_of_interest = []
        for event in self.events:
            s = datetime.datetime.combine(start_date, datetime.time.min)
            e = datetime.datetime.combine(end_date, datetime.time.max)
            if event.student.name == name:
                if s < event.start < e:
                    events_of_interest.append(event)

        return sum(e.calc_amount() for e in events_of_interest)
