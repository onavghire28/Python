# n = int(input("Enter the number: "))

# sum = 0
# for i in range(1,n-1):
#     if n%i ==0:
#         sum = sum+i

# print(sum)

#Reverse the string

a = input("Enter the string: ")

b = ""
for i in range(len(a)-1,-1,-1):
    b = b+a[i]

print(b)

if b == a:
    print("Palindrom")
else:
    print("not") 




    