from dateutil.parser import *
from datetime import *

tmp = """Thu Jun 27
Close Bench 265 5, 275 5
Two stage iso bench 225 6,4 185 6, 5
Rolling db extension 35 4x10
BB Row 315 4 x 4
Pull ups -100 4x 10
hammer curls 35 5 x10
db lateral raise 10 5x10"""

def parse_and_rm_date(workout):
    """in: list of workout entries.
       out: list with date removed, date"""

    wo = []
    date_line = ''
    date = None
    for w in workout:
        try:
            date = parse(w)
            date_line = w
        except:
            wo.append(w)

    if date is None:
        date = date.today()

    # XXX check if the date line has more than just the date in it.

    return (wo, date)


def get_lift_entries(workout):
    for w in workout:
        pass


def process_text(text):
    """ in: raw text from user
        out: list of dictionaries describing the workout"""

    tokens = text.split('\n')

    #workouts = split_workouts()
    workouts = [tokens]

    dict_list = []
    for w in workouts:
        w, date = parse_and_rm_date(w)
        d['date'] = date  # TODO format string here?

        w, lif_entries = get_lift_entries(w)

        dict_list.append(d)

    return dict_list

process_text(tmp)
