rule = 90
print(bin(rule+256)[3::])
predict = ['***', '**_', '*_*', '*__', '_**', '_*_', '__*', '___']
prerule = ['*' if i == '1' else '_' for i in bin(rule+256)[3::]]
dic = dict([i,j] for i,j in zip(predict, prerule))
print(dic)