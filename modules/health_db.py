import json
# AI 사용
# 종류 및 목적: chatGPT, json 파일 사용 방법
# 사용한 프롬프트: json 파일로 데이터를 읽고 저장하는 법
import os

class Health_info:
    def __init__(self, id, name, birth, gender, height, weight, bmi, status):
        self.id = id
        self.name = name
        self.birth = birth
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.status = status

    def get_bmi(self):
        bmi = self.weight / ((self.height / 100)**2)
        return round(bmi,1)

    def bmi_to_text(self, bmi):
        if bmi <= 18.5:
            return "저체중"
        elif bmi <= 24.5:
            return "정상"
        elif bmi <= 30:
            return "과체중"
        else:
            return "비만"

class Health_Manager:
    def __init__(self):
        self.datas = []
        # AI 사용
        # 종류 및 목적: chatgpt, 파일이 존재하지 않는 경우 메세지 생성
        # 사용한 프롬프트: file_path에 존재하지 않는 파일을 적었는데 왜 except로 넘어가지 않아?
        try :
            # 상대경로(AI 사용)
            self.file_path = os.path.join(os.path.dirname(__file__), "..", "data", "data.json")
            #os.path.dirname(): 파일명을 제외하고 폴더 경로만 가져옴

            if not os.path.exists(self.file_path):
                raise FileNotFoundError
        except FileNotFoundError:
            print("존재하지 않는 파일입니다. 경로를 다시 확인해주세요")
        

    def load_file(self):
        global last_id
        with open(self.file_path, "r", encoding= "utf-8") as f:
            data = json.load(f)
            # 파일 읽기

        self.datas = []

        for item in data:
            info = Health_info(item["id"],
                               item["name"],
                               item["birth"],
                               item["gender"],
                               item["height"],
                               item["weight"],
                               item["bmi"],
                               item["status"])
            self.datas.append(info)
        last_id = int(item["id"].split("-")[1])

    def update_file(self):
        data = []

        for info in self.datas:
            print(type(info.id))
            data.append({"id": info.id,
                         "name":info.name,
                         "birth": info.birth,
                         "gender": info.gender,
                         "height": info.height,
                         "weight": info.weight,
                         "bmi": info.bmi,
                         "status": info.status})

        with open(self.file_path, "w", encoding= "utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent = 4)
            #json.dump(데이터, 파일 객체, 유니코드 변환 여부, 들여쓰기 칸)

    def random_id(self):
        # AI 사용
        # 종류 및 목적: ChatGPT, 0000 형식에 맞게 숫자 변환하기
        # 사용한 프롬프트: 0001, 0002와 같이 숫자를 입력하면 앞에 0이 붙게 하는 법
        return f"P2026-{(last_id + 1):04d}"

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
manager = Health_Manager()
manager.load_file()
#manager.random_id()
#manager.add_file()
#manager.update_file()
