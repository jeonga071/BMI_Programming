from health_db import *

class Create_data(Health_info):
    def add_file(self):
        id = self.random_id()
        name = input("이름을 입력하세요: ")
        birth = int(input("태어난 연도를 입력하세요: "))
        gender = input("성별을 입력하세요(남/여): ")
        height = float(input("키를 입력하세요: "))
        weight = float(input("몸무게를 입력하세요: "))
        temp = Health_info(id, name, birth, gender, height, weight, 0, "")
        bmi = temp.get_bmi()
        status = temp.bmi_to_text(bmi)

        user_info = Health_info(id, name, birth, gender, height, weight, bmi, status)
        self.datas.append(user_info)

    def random_id(self):
            # AI 사용
            # 종류 및 목적: ChatGPT, 0000 형식에 맞게 숫자 변환하기
            # 사용한 프롬프트: 0001, 0002와 같이 숫자를 입력하면 앞에 0이 붙게 하는 법
            return f"P2026-{(self.last_id + 1):04d}"