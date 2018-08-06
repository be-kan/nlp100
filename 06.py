def gen_character_ngram(sentence, N):
    ngram = []
    for i in range(len(sentence)-N+1):
        ngram.append(sentence[i:i+N])

    return ngram


s1 = "paraparaparadise"
s2 = "paragraph"

X = gen_character_ngram(s1, 2)
Y = gen_character_ngram(s2, 2)

sum_set = set(X + Y)
common_set = set(X) & set(Y)
diff_set = list(set(X) - set(Y)) + list(set(Y) - set(X))

print(sum_set)
print(common_set)
print(diff_set)
