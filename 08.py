def cipher(sentence):
    result = []
    for i in range(len(sentence)):
        n = ord(sentence[i])
        if n >= ord('a') & n <= ord('z'):
            result.append(chr(219-n))
        else:
            result.append(sentence[i])

    return "".join(result)


sentence = 'I am an Engineer'
encripted_sentence = cipher(sentence)
unencripted_sentence = cipher(encripted_sentence)
print(sentence)
print(encripted_sentence)
print(unencripted_sentence)
