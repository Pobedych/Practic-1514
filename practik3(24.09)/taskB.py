line1 = input().strip().lower()
line2 = input().strip().lower()

words1 = set(line1.split())
words2 = set(line2.split())

common_words = sorted(words1 & words2)

for word in common_words:
    print(word)
