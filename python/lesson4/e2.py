def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]
l=[['Paul', 'John', 'Ringo', 'George']]
[['Paul', 'John', 'Ringo', 'George'], ['Jen', 'Jamie']]
[['Who', 'What', "I don't Know", "I'll tell you later"], ['Al', 'Bonnie', 'Clyde']]

print(losing_team_captain(l))