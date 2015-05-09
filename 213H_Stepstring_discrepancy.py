

#lines = open("213H_Stepstring_discrepancy_input.txt").readlines()





##############################################################
#STUPID SOLUTION                                            #
##############################################################

##############################################################
#STUPID SOLUTION                                            #
##############################################################


line='bbaaaababbbaababbbbabbabababababaaababbbbbbaabbaababaaaabaaa' #12




#line='bbaaabababbaabbaaaabbbababbaabbbaabbaaaaabbababaaaabaabbbaaa' #9
line='bbaaaababbbaababbbbabbabababababaaababbbbbbaabbaababaaaabaaa' #12

get_discrepancy = lambda x: abs(x[2][x[0]:x[1]+1].count('a') - x[2][x[0]:x[1]+1].count('b'))
#for line in lines :
(x,y, _) = max([(i,j,line) for i in range(len(line)) for j in range(i, len(line))], key=get_discrepancy)
print(x, y)
print(line[x:y])
print(get_discrepancy((x,y,line)))




