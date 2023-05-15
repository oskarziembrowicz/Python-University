dna1 = "aabgtbbaggt"
dna2 = "tggaccaggat"
#pierwszy ciąg + zaznacza komplementarnośc pary(komplementarna:'.', niekomplementarna:'|') + drugi ciąg
d = {"a":"c", "c":"a", "g":"t", "t":"g"}

#better
# for i,j in zip(dna1, dna2):
#     if (i,j) in d:
#         print("|", end:='')
#     else:
#         print(".", end:='')

#best
print(dna1)
print(''.join(["|" if {i,j} in d else "." for i,j in zip(dna1, dna2)]))
print(dna2)


#PRACA DOMOWA:
#Poczytać o automatach komówrkowych(przypadek jednowymiarowy)
#Elementary cellular automaton