l1 = ["abc", "cd3", "f7g", ";h*45"]

# l1 = [''.join(filter(str.isnumeric, i)) for i in l1]
# l1 = list(filter(lambda x: x != '', l1))
# l1 = list(map(int, l1))

#l1 = [int(j) for j in [''.join(i for i in j if i.isdigit()) for j in l1] if j]
l1 = list(map(int, filter(bool, map(lambda x: ''.join(filter(lambda i: i.isdigit(), x)), l1))))

print(l1)