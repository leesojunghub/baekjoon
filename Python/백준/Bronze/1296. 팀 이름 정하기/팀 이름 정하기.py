import sys
from collections import Counter
input = sys.stdin.readline

name = input().strip()
name_cnt = Counter(name)
n = int(input())
best_per = -1
best_team = ''
for _ in range(n):
    team = input().strip()
    team_cnt = Counter(team)
    l = name_cnt['L'] + team_cnt['L']
    o = name_cnt['O'] + team_cnt['O']
    v = name_cnt['V'] + team_cnt['V']
    e = name_cnt['E'] + team_cnt['E']
    percent = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100
    if percent > best_per:
        best_per = percent
        best_team = team
    elif percent == best_per:
        if team < best_team:
            best_team = team
print(best_team)