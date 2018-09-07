/* Your Python Program will come here */
N = int(input())
def feb(n):
    if n ==1 or n == 0:
        return 1
    return feb(n-1)+feb(n-2)

def prime(m):
    arr = []
    for i in range(m):
        for j in range(i):
            isprime = True
            if i%j ==0:
                isprime=False
         if isprime:
         arr.append(i)
    return arr

febo = feb(N/2)
primo = primr(N/2)

final =[]
for i in range(N)
    if i%2 == 0:
        final.append(primo[i/2]
    else:
        final.append(febo[i/2])

print(final[N-])


        