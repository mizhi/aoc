# https://adventofcode.com/2022/day/2

CODING = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

SCORING = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

def winner(p1, p2):
    if p1 == p2:
        return 0
    elif (p1 == "Rock" and p2 == "Paper") or \
         (p1 == "Paper" and p2 == "Scissors") or \
         (p1 == "Scissors" and p2 == "Rock"):
        return 1
    elif (p1 == "Rock" and p2 == "Scissors") or \
         (p1 == "Paper" and p2 == "Rock") or \
         (p1 == "Scissors" and p2 == "Paper"):
        return -1

WINNER_SCORES = [3, 6, 0]
def score(p1, p2):
    return WINNER_SCORES[winner(p1, p2)] + SCORING[p2]

total_score = 0
with open("input.txt", "r") as f:
    for hand in f:
        play = hand.strip().split()
        play[0], play[1] = CODING[play[0]], CODING[play[1]]
        hs = score(*play)
        print(play, hs)
        total_score += hs

print(total_score)
