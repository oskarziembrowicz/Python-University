l1 = ["abc", "cd3", "f7g", ";h*"]

# l1 = [''.join(i for i in j if i.isalpha()) for j in l1]
l1 = list(map(lambda j: ''.join(filter(lambda x: x.isalpha(), j)), l1))
print(l1)