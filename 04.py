sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split(" ")

single_words = [(idx, words[idx-1][0]) for idx in [1, 5, 6, 7, 8, 9, 15, 16, 19]]
double_words = [(idx, words[idx-1][:2]) for idx in [2, 3, 4, 10, 11, 12, 13, 14, 17, 18, 20]]

words_dict = {x: y for x, y in single_words + double_words}
dict = sorted(words_dict.items())
print(dict)
