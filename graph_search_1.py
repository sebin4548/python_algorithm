a, b = map(int, input().split())
inpu = list(map(int, input().split()))
n = inpu[0] #"""알고 있는 사람 명수"""
know_list = list(inpu[1:]) #"""알고 있는 사람 리스트"""
now_list = [1]
answer = [True] * b
lis = [] #"""파티 명단"""
for _ in range(b):
    inpu = list(map(int, input().split()))
    lis.append(inpu[1:])
total = know_list
while (know_list):
    now_list = []


    for x in range(len(lis)):
        for num in know_list:
            if num in lis[x]:
                answer[x] = False
            if answer[x] == False:
                for y in lis[x]:
                    if y not in now_list and y not in know_list and y not in total:
                        now_list.append(y)
                        total.append(y)

    now_list,know_list = [], now_list


answer_number = 0
for _ in answer:
    if _ == True:
        answer_number += 1

print(answer_number)

