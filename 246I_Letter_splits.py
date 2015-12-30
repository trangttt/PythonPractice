# text = '1234'
text = '1234567899876543210'

def partition(text):
    if len(text) == 0:
        return [[]]
    elif len(text) == 1:
        return [[text[0]]]
    elif len(text) >= 2:
        result = []
        for i in partition(text[1:]):
            result.append([text[0]]+i)
        for i in partition(text[2:]):
            result.append([text[:2]]+i)
        return result

mapping = dict( (str(index), c) for index, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ',start=1))
for candidate in partition(text):
    if all( int(c)<=26 and int(c)>0 for c in candidate ):
        print(candidate)
        print("".join(mapping.get(c) for c in candidate))


