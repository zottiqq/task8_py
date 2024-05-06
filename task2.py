def reverse(a):
    a1 = str(a)  
    a2 = a1[::-1]
    return a2

def palid(a):
    a1 = str(a)
    a2 = a1[::-1]
    if a1 == a2:
        print(a, 'является палидромом')

spisok =  [1234, 421, 4830, 888802, 987654321, 101]
sps = []
def process():
    for item in spisok:
        reversed_item = reverse(item)
        sps.append(reversed_item)
    print(sps)
    for i in sps:
        palid(i)
    

process()