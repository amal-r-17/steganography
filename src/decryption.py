image = steg1
result = []
for i in range(image[0][0][0]):
    result.append(image[i+1][i+1][0])

msg = ''
for i in result:
    i = chr(i)
    msg+=i
print("The message : ",msg)    