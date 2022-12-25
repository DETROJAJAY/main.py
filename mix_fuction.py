# def jay(*a):
#     avg = []
#     for i in zip(*a):
#         avg.append(sum(i) / len(i))
#     return avg


jay = lambda *a : [(sum(i) / len(i)) for i in zip(*a) ]
print(jay([1,2,3],[4,5,6],[7,8,9]))