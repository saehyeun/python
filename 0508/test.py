# 중간점검

## 1. 리스트는 시퀀스에 속하는가? => 속한다
## 2. 시퀀스의 특징에는 어떤것이 있는가? => 순서가 있다, 인덱싱이 가능하다, 슬라이싱이 가능하다, 반복이 가능하다

## 중간점검

### 1. 리스트와 튜플의 다른 점은 무엇인가? =>  리스트는 변경이 가능하지만, 튜플은 변경이 불가능하다.
### 2. 리스트를 튜플로 바꾸려면 어떤 함수를 사용해야 하는가? => tuple() 함수를 사용해야 한다.
### 3. 패킹과 언패킹을 설명해보자 => 여러 값을 하나로 묶거나, 반대로 하나에 들어있는 값을 꺼내는 기능
### 4. enumerate() 함수는 무엇을 하는 함수인가? => 반복문에서 인덱스와 값을 동시에 얻을 수 있게 해주는 함수

### 중간점검

#### 1. 리스트와 세트의 차이점은 무엇인가? => 리스트는 순서가 있고 중복이 혀용되지만, 세트는 순서가 없고 중복이 허용되지 않는다.
#### 2. 세트에 저장된 항목에 접근할 때 인덱스를 사용할 수 있는가? => 사용할 수 없다.
#### 3. 세트 A와 세트 B의 교집합을 계산하는 수식을 만들어 보자. => A & B
#### 4. 세트에 항목을 추가하는 함수는? => add() 함수를 사용한다.

# lab : 문자열의 공통 문자
s1=input("첫 번째 문자열:")
s2=input("두 번째 문자열:")

list1 = list( set(s1) & set(s2) ) # 세트로 만들고 교집합 연산을 한다.

print("\n공통적인 글자:", end=" ")
for i in list1:
    print(i, end=" ")

# lab : 문자열의 공통 문자

txt = input("입력 텍스트: ")
words = txt.split(" ")
unique = set(words)    # 집합으로 만들면 자동적으로 중복을 제거한다.

print("사용된 단어의 개수= ", len(unique))
print(unique)

# 중간점검

## 1. 공백 딕셔너리를 생성하는 명령문을 만들어 보자. => dict() 함수를 사용.
## 2. 딕셔너리에 존재하는 모든 키(key)를 방문하는 코드를 작성해보자. => for key in dict: print(key)
## 3. 딕셔너리 d에 (k,v)를 저장하는 명령문을 만들어보자. => d[k] = v

# lab : 영한 사전

english_dict ={}           # 공백 딕셔너리를 생성한다.

english_dict["one"]="하나" # 딕셔너리에 단어와 의미를 추가한다.
english_dict["two"]="둘'"
english_dict["three"]="셋"

word =input("단어를 입력하시오: ");
print (english_dict[word])

# lab : 학생 성적 처리

def display_menu():
    print("\n1: 연락처 추가")
    print("2: 연락처 삭제")
    print("3: 연락처 검색")
    print("4: 연락처 모두 보기")
    print("5: 종료")
    try:
        return int(input("메뉴를 선택하세요: "))
    except ValueError:
        return 0

def get_contact():
    name = input("이름을 입력하세요: ")
    number = input("전화번호를 입력하세요: ")
    return name, number

def main():
    address_book ={}                      # 공백 딕셔너리를 생성한다.
    while True :
        user = display_menu();
        if user ==1 :
            name, number = get_contact()
            address_book[name]= number    # name과 number를 추가한다.
        elif user ==2 :                     
            name, number = get_contact()
            address_book.pop(name)        # name을 키로 가지고 항목을 삭제한다.
        elif user ==3 :
            pass                          # 도전 문제 참조
        elif user ==4 :
            for key in sorted(address_book):
                print(key,"의 전화번호:", address_book[key])
        else:
            break