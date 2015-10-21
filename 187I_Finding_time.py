import re
import arrow
from collections import namedtuple
from itertools import groupby
from datetime import timedelta

Note = namedtuple("Note", ("start", "end", "text"))


def parse_file(file):
    raw_notes = file.read()
    pattern = re.compile(r'(\d+-\d+-\d+): (.+) to (.+) -- (.+)')
    all_notes = pattern.findall(raw_notes)
    pattern = 'M-D-YYYY HH:mm A'
    notes = [Note(arrow.get(date + " " + start, pattern),
                  arrow.get(date + " " + end, pattern),
                  text) for date, start, end, text in all_notes]
    # for line in file.readlines():
        # match = re.match(r'(?P<start>[0-9:\- AMP]+) to (?P<end>[0-9: AMP]+) -- (?P<text>.*)', line.strip(" \n"))
        # start = arrow.get(match.group("start"), "MM-D-YYYY: HH:mm A")
        # end = arrow.get(match.group("start").split(":")[0] + " " + match.group("end"),
                        # "MM-D-YYYY HH:mm A")
        # note = Note(start, end, match.group("text"))
        # notes.append(note)
    return notes


def find_free_time(notes):
    sorted_notes = sorted(notes, key=lambda note: note.start.datetime)
    for date, group in groupby(sorted_notes, lambda note: note.start.date()):
        sorted_group = sorted(group, key=lambda note: note.start)
        duration = max([items for items in zip(sorted_group[:-1], sorted_group[1:])],
                       key=lambda notes: notes[1].start - notes[0].end)
        notes.append(Note(duration[0].end, duration[1].start, "Reddit"))
    return notes


def calculate_percentage(notes):
    notes = sorted(notes, key=lambda note: note.text)
    totalDelta = sum([note.end - note.start for note in notes], timedelta(0))
    for taskName, tasks in groupby(notes, lambda note: note.text):
        deltas = [note.end - note.start for note in tasks]
        taskDelta = sum(deltas, timedelta(0))
        print(taskName.rjust(30), str(taskDelta).rjust(10), " : {:.2f}%".format(taskDelta/totalDelta * 100))


if __name__ == "__main__":
    notes = parse_file(open("187I_input.txt"))
    reddit_notes = find_free_time(notes)
    sorted_reddit_notes = sorted(reddit_notes, key=lambda note: note.start.datetime)
    for date, group in groupby(sorted_reddit_notes, lambda note: note.start.date()):
        print(str(date).center(30, "*"))
        fs = 'HH:mm A'
        for item in group:
            print(item.start.format(fs) + "--" + item.end.format(fs) + " : " + item.text)
    calculate_percentage(sorted_reddit_notes)
