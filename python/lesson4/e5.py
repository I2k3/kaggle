def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    l=len(arrivals)//2
    return name in arrivals[-l:-1]

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(fashionably_late(party_attendees,"Adela"))
print(fashionably_late(party_attendees,"Mona"))