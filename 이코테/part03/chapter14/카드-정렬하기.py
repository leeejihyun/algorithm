n = int(input())
cards = []
for _ in range(n):
    m = int(input())
    cards.append(m)

cards.sort()
if n == 1:
    print(cards[0])
else:
    answer = cards[0] + cards[1]
    i = 2
    while i < n:
        prev_answer = answer + cards[i]
        answer += prev_answer
        i += 1
    print(answer)