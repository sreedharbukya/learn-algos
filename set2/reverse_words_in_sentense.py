def reverse_words_in_string(sentence):
    if not sentence:
        return

    if sentence and len(sentence) < 0:
        return
    output = []
    words = sentence.split(" ")
    for word in words:
        output.append(word[::-1])
    return " ".join(output)
