DNA1 = "acctgattgaggc"
d = {"a":"c", "c":"a", "g":"t", "t":"g"}
DNA2 = ''.join([d[i] for i in DNA1])    #join connects elements of the list in argument with the character given in front
print(DNA1)
print(DNA2)