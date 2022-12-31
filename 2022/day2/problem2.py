# https://adventofcode.com/2022/day/2

OPPONENT_MOVE = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

NEEDED_RESULT = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

SCORING = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

BEATS = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

# encoding of (opponent move, needed result) => my play
MOVE_ORACLE = {
    ("Rock", "Win"): "Paper",
    ("Rock", "Lose"): "Scissors",

    ("Paper", "Win"): "Scissors",
    ("Paper", "Lose"): "Rock",

    ("Scissors", "Win"): "Rock",
    ("Scissors", "Lose"): "Paper"
}

def winner(p1, p2):
    if p1 == p2:
        return 0
    elif BEATS[p1] == p2:
        return -1
    elif BEATS[p2] == p1:
        return 1

def decide_play(move, result):
    return MOVE_ORACLE.get((move, result), move)

WINNER_SCORES = [3, 6, 0]
def score(p1, p2):
    return WINNER_SCORES[winner(p1, p2)] + SCORING[p2]

total_score = 0
with open("input.txt", "r") as f:
    for hand in f:
        play = hand.strip().split()
        play[0], play[1] = OPPONENT_MOVE[play[0]], NEEDED_RESULT[play[1]]

        my_move = decide_play(*play)

        hs = score(play[0], my_move)
        total_score += hs

print(total_score)
