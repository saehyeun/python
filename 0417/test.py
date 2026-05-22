# lab : 성적처리 프로그램

STUDENT = 5
lst = []
count = 0

for i in range(STUDENT):
    value = int(input("성적을 입력하시오."))
    lst.append(value)

print("\n성적 평균=", sum(lst) / len(lst))
print("최대점수=", max(lst))
print("최소점수=", min(lst))
for score in lst:
    if score >= 80:
        count += 1
print("80점 이상=", count)

#lab : 리스트에서 2번째로 큰 수 찾기

list1 = [1, 2, 3, 4, 15, 99]
list1.sort()
print("두 번째로 큰 수=", list1[-2])
list1 = [1, 2, 3, 4, 15, 99]
list1.remove(max(list1)) 
print("두 번째로 큰 수=", max(list1)) 

#lab : 콘테스트 평가

scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print("제거전", scores)
scores.remove(max(scores))
scores.remove(min(scores))
print("제거후", scores)

# lab : 리스트로 스택 흉내내기

stack = []
for i in range(3) :
    f = input("과일을 입력하시오: ")
stack.append(f)
for i in range(3) :
    print( stack.pop() )

#lab : 친구관리 프로그램

menu = 0
friends = []
while menu != 9:
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        friends.append(name)
    elif menu == 3:
        del_name = input("삭제하고 싶은 이름을 입력하시오: ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("이름이 발견되지 않았음")

