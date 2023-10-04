# Madlibs Generator
with open ("story.txt", "r") as f:
    story = f.read()

words = set()
# to get unique words, if you use [], it is a list, keep repetitive items
start_of_word = -1
target_start = "<"
target_end = ">"
# 查找需要替换的词
for i, char, in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# 遍历
answers = {}

for word in words:
    answer = input("Enter a word for" + word + ":")# input, use +; print, use ,to auto add blank in between
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)