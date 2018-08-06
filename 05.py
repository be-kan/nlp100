def gen_character_ngram(sentence, N):
    ngram = []
    for i in range(len(sentence)-N+1):
        ngram.append(sentence[i:i+N])

    return ngram


def gen_word_ngram(sentence, N):
    ngram = []
    sentence = sentence.split(" ")
    for i in range(len(sentence)-N+1):
        ngram.append(sentence[i:i+N])

    return ngram


sentence = input()
print(gen_word_ngram(sentence, 2))
print(gen_character_ngram(sentence, 2))
