import random

def typoglycemia(text):
    result = []
    words = text.split(" \n")
    print(words)
    shuffle_word = lambda w, beg, end: list(w) if len(w) <=3 else [w[:beg]] + random.sample(w[beg:end], len(w)-2) + [w[end:]]
    for word in words:
        beg = 1
        end = -1
        if '\n' in word:
            beg = 2
        if "," in word or "." in word:
            end = -2
        elif "'" in word:
            end = -2
        result.append("".join(shuffle_word(word, beg, end)))

    print(" ".join(result))



if __name__ == "__main__":
    text = open("240E_input.txt").read()
    typoglycemia(text)
