text = """A B B C C D D E E F F G G G G A A A A A E A a b c A C C C C """

print(text.split())

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count [word] = 1

print(word_count)