# -150
n = [i for i in input() if i != '0']
z = []
if not n[0].isdigit():
    z = [n.pop(0)]
r = n[::-1]
print(''.join(z + r))
