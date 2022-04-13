A= [[2,3], [4,2]]
B= [10,4]

input =[]

k = A[0][0] * A[1][1] - A[0][1] * A[1][0]

input.append([A[1][1]/k, -A[1][0]/k])
input.append([-A[0][1]/k, A[0][0]/k])

sum=0
answer=[]
for x in range(2):
    for y in range(2):
        sum = sum + input[y][x]*B[y]
    answer.append(sum)
    sum=0
print(answer)