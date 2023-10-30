def word_counter():
    txt = "I like apples apples are my my favourite fruits"
    words = txt.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(word," : ",count)


word_counter()
