#!/bin/python3

words = input().split()

indent = 0
result = ""

for i, w in enumerate(words):
  if i%2 == 0 :
      result += w[1:] + "\n" if i > 0 else w + "\n"
      indent += len(w)-1
  else :
      for i, c in enumerate(w[1:]):
          result += " "* indent + c  if i == len(w[1:])-1 else " "*indent + c + '\n'

print(result)
