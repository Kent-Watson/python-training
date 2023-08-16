print(5.1)
song1 = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
###「　ｍ」を「 M」に変換したものを表示
print(song1.replace(" m", " M"))

print(5.2)
questions = [
    "名前は？",
    "年齢は？",
    "性別は？"
]
answers = [
    "女です。",
    "太郎です。",
    "1歳です。"
]
qa = ((0, 1), (1, 2), (2, 0))

for q, a in qa:
    print("Q:", questions[q])
    print("A:", answers[a])

print(5.3)
roastbeef = "roast beef"
ham = "ham"
head = "head"
clam = "clam"

song3 = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s."""

print(song3 % (roastbeef, ham, head, clam))