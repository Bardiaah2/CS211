from datetime import datetime
#import intervals

class Appt:
    """An appointment has a start time, an end time, and a title.
    The start and end time should be on the same day.
    Usage example:
        appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
        appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
        if appt2 > appt1:
            print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
        elif appt1.overlaps(appt2):
            print("Oh no, a conflict in the schedule!")
            print(appt1.intersect(appt2))
    Should print:
        Oh no, a conflict in the schedule!
        2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def __init__(self, start: datetime, finish: datetime, desc: str):
        """An appointment from start time to finish time, with description desc.
        Start and finish should be the same day.
        """
        assert finish > start, f"Period finish ({finish}) must be after start ({start})"
        self.start = start
        self.finish = finish
        self.desc = desc

    def __eq__(self, other: 'Appt') -> bool:
            """Equality means same time period, ignoring description"""
            return self.start == other.start and self.finish == other.finish

    def __lt__(self, __value: 'Appt') -> bool:
        return self.start < __value.start

    def overlaps(self, other: 'Appt') -> bool:
        """Is there a non-zero overlap between these periods?"""
        int_start = max(self.start, other.start)
        int_finish = min(self.finish, other.finish)

        return int_start<int_finish

    def intersect(self, other: 'Appt') -> 'Appt':
        """The overlapping portion of two Appt objects"""
        assert self.overlaps(other)  # Precondition
        int_start = max(self.start, other.start)
        int_finish = min(self.finish, other.finish)

        return Appt(int_start, int_finish, self.desc + " & " + other.desc)

    def __str__(self) -> str:
        """The textual format of an appointment is
        yyyy-mm-dd hh:mm hh:mm | description
        Note that this is accurate only if start and finish
        are on the same day.
        """
        return f"{self.start.date().isoformat()} {self.start.time().isoformat('minutes')} {self.finish.time().isoformat('minutes')} | {self.desc}"

    def __repr__(self) -> str:
        return f"Appt({self.start}, {repr(self.finish)}, {repr(self.desc)})"



class Agenda:
    """An Agenda is a collection of appointments,
    similar to a list.

    Usage:
    appt1 = Appt(datetime(2023, 3, 15, 13, 30), datetime(2023, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2023, 3, 15, 15, 00), datetime(2023, 3, 15, 16, 00), "Coffee break")
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda.text()}")
        print(f"Conflicts:\n {ag_conflicts}")

    Expected output:
    In agenda:
    2023-03-15 13:30 15:30 | Early afternoon nap
    2023-03-15 15:00 16:00 | Coffee break
    Conflicts:
    2023-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def __init__(self):
        self.elements = [ ]

    def __eq__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        self.sort()
        other.sort()
        return self.elements == other.elements

    def __lt__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        pass

    def __str__(self):
        """Each Appt on its own line"""
        lines = [ str(e) for e in self.elements ]
        return "\n".join(lines)

    def __repr__(self) -> str:
        """String representation for debugging"""
        return f"Agenda({self.elements})"

    def append(self, an_appt: Appt) -> None:
        """Append the appointments in two agendas"""
        self.elements.append(an_appt)

    def sort(self) -> None:
        """Sort agenda by appointment start times.
        This method sorts the appointments in-place."""
        self.elements.sort(key=lambda appt: appt.start)

    def __len__(self) -> int:
        """Returns the length of the Agenda."""
        return len(self.elements)

    def conflicts(self) -> 'Agenda':  # TODO
        """Returns an agenda consisting of the conflicts
        (overlaps) between appointments in this agenda.
        Side effect: This agenda is sorted.
        """
        self.sort()
        result: Agenda = Agenda()
        for appt in self.elements:
            for appt2 in self.elements[self.elements.index(appt)+1:]:
                appt: Appt
                appt2: Appt
                if appt2.start > appt.finish:
                    break
                elif appt.overlaps(appt2):
                    result.append(appt.intersect(appt2))

        return result


if __name__ == "__main__":
    print("Running usage examples")
    appt1 = Appt(datetime(2023, 3, 15, 13, 30), datetime(2023, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2023, 3, 15, 15, 00), datetime(2023, 3, 15, 16, 00), "Coffee break")
    appt3 = Appt(datetime(2023, 3, 15, 15, 00), datetime(2023, 3, 15, 16, 00), "Coffee break")
    appt4 = Appt(datetime(2023, 3, 15, 16, 00), datetime(2023, 3, 15, 17, 00), "Coffee break")

    print(appt3 < appt4)
    if appt2 > appt1:
        print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
    elif appt1.overlaps(appt2):
        print("Oh no, a conflict in the schedule!")
        print(appt1.intersect(appt2))
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda}")
        print(f"Conflicts:\n {ag_conflicts}")
