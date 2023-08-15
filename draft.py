arrs = ['10', 'a', '20', '40', '80', 'b']

res = [int(a) for a in arrs if a.isdigit()]
print(res)