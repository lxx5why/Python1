#아래 프로그램은 사용자로부터 이름과 나이를 입력 받아서 출력하는 프로그램입니다.
name = input("이름을 입력하세요 : ")
age = input("나이를 입력하세요 : ")
print("안녕하세요." + name +"님, 반갑습니다. 입력하신 나이는 " + age + "살 입니다.")
print(f"{name}은 {age}살 입니다.")