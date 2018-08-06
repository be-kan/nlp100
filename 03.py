sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sentence.replace(",", "").replace(".", "").split(" ")

print([len(word) for word in words])
