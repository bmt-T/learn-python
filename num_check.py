num_check = int(input("nhap vao so cua ban: "))
if num_check ==0:
    print('0')
else:
    msg = "even" if num_check %2 ==0 else "odd"
    print(msg)
