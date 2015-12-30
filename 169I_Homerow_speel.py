import sys

words_list = list(map(lambda x: x.rstrip('\n'), open('enable1.txt').readlines()))

keyboards = ['zxcvbnm', 'asdfghjkl', 'qwertyuiop', 'ZXCVBNM', 'ASDFGHJKL', 'QWERTYUIOP']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '.,'

# if __name__ == "__main__":
    # sentence = sys.argv[1:]
    # for index, word in enumerate(sentence):
        # if word.lower().strip(punctuation) not in words_list:
            # print(word)
            # get_charset = lambda c, i: [kb[(kb.index(c)+i)%len(kb)] for kb in keyboards if c in kb][0]
            # pos_words = [''.join( get_charset(c, i) if c.lower() in alphabet else c for c in word)  for i in (-2, -1, 1, 2)]
            # result = [ w for w in pos_words if w.lower().strip(punctuation) in words_list ]
            # sentence[index] = result

shifted_keyboards = [ [kb[i:] + kb[:i] for kb in keyboards] for i in (-2, -1, 1, 2)]

# if __name__ == "__main__":
    # sentence = sys.argv[1:]
    # for index, word in enumerate(sentence):
        # if word.lower().strip(punctuation) not in words_list:
            # get_charset = lambda c, skb: [ skb[index][srow.index(c)] for index, srow in enumerate(keyboards) if c in srow][0]
            # pos_words = [ "".join(get_charset(c, skb) if c.lower() in alphabet else c for c in word) for skb in shifted_keyboards ]
            # result = [w for w in pos_words if w.lower().strip(punctuation) in words_list]
            # sentence[index] = result

    # for word in sentence:
            # print('{' + ', '.join(w for w in word) + '}', end=' ') if isinstance(word, list) else print(word, end=" ")
    # print()

kb_str = ''.join(keyboards)
skb_strs = [''.join(skb) for skb in shifted_keyboards  ]
tables = [ str.maketrans(kb_str, skb_str) for skb_str in skb_strs ]

if __name__ == "__main__":
    sentence = sys.argv[1:]
    for index, word in enumerate(sentence):
        if word.lower().strip(punctuation) not in words_list:
           fixes = [ word.strip(punctuation).translate(table) for table in tables]
           result = [ fix for fix in fixes if fix.lower() in words_list ]
           sentence[index] = result
    for word in sentence:
        print('{' + ', '.join(w for w in word) +'}', end = ' ') if isinstance(word, list) else print(word, end=' ')

