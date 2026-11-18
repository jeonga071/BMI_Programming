from modules import health_db

class Create_data:
    def __init__(self, manager:health_db.Health_Manager):
         self.manager = manager
         
    def add_file(self):
        # AI 사용
        # 종류 및 목적: ChatGPT, 오류 반복 해결
        # 프롬프트: 'Health_Manager' has no attribute 'last_id'와 'Health_Manager' object is not callable 반복 해결방법
        id = self.random_id()
        name = input("이름을 입력하세요: ")
        birth = int(input("태어난 연도를 입력하세요: "))
        gender = input("성별을 입력하세요(남/여): ")
        height = float(input("키를 입력하세요: "))
        weight = float(input("몸무게를 입력하세요: "))
        temp = health_db.Health_info(id, name, birth, gender, height, weight, 0, "")
        bmi = temp.get_bmi()
        status = temp.bmi_to_text(bmi)

        user_info = health_db.Health_info(id, name, birth, gender, height, weight, bmi, status)
        if (self.check_name(name, birth, gender)):
            self.manager.datas.append(user_info)
        else:
            print("이미 존재하는 회원입니다.")

    def random_id(self):
        # AI 사용
        # 종류 및 목적: ChatGPT, 0000 형식에 맞게 숫자 변환하기
        # 사용한 프롬프트: 0001, 0002와 같이 숫자를 입력하면 앞에 0이 붙게 하는 법
        return f"P2026-{(self.manager.last_id + 1):04d}"

    def check_name(self, name, birth, gender):
        for data in self.manager.datas:
            if data.name == name and int(data.birth) == birth and data.gender == gender:
                return False
        return True

class Retrieve_data:
    def __init__(self, manager:health_db.Health_Manager):
        self.manager = manager
        self.number = int(input(""))
        self.name = ""
    def full_search(self):
        for data in self.manager.datas:
            print(f"id: {data.id}, name: {data.name}, birth: {data.birth}, gender: {data.gender}, height: {data.height}, weight: {data.weight}, bmi: {data.bmi}, status: {data.status}")
    
    