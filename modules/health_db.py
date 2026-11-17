# AI 사용
# 종류 및 목적: chatGPT, json 파일 사용 방법
# 사용한 프롬프트: json 파일로 데이터를 읽고 저장하는 법
import json
import csv
import pickle

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
            # json
            self.file_path_json = os.path.join(os.path.dirname(__file__), "..", "data", "data.json")
            #os.path.dirname(): 파일명을 제외하고 폴더 경로만 가져옴

            # csv
            self.file_path_csv = os.path.join(os.path.dirname(__file__), "..", "data", "data.csv")

            # txt
            self.file_path_txt = os.path.join(os.path.dirname(__file__), "..", "data", "data.txt")

            # pkl
            # 목적: pkl 사용법
            # 프롬프트: pkl 파일 생성 및 데이터를 읽어오는 법
            self.file_path_pkl = os.path.join(os.path.dirname(__file__), "..", "data", "data.pkl")

            if not os.path.exists(self.file_path_json):
                raise FileNotFoundError
        except FileNotFoundError:
            print("존재하지 않는 파일입니다. 경로를 다시 확인해주세요")
        

    def load_file(self):
        global last_id

        self.datas = []

        # json
        with open(self.file_path_json, "r", encoding= "utf-8") as f:
            data = json.load(f)
            # 파일 읽기

        # csv
        # 데이터 읽을 때: stf-8-sig(BOM 문자가 포함 될 경우 사용)
        # with open(self.file_path_csv, "r", encoding="utf-8-sig") as f:
        #     data = csv.DictReader(f)
        
        # pkl
        # with open(self.file_path_pkl, "rb") as f:
        #     data = pickle.load(f)

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

        #txt
        # with open(self.file_path_txt, "r", encoding="utf-8") as f:
        #     f.readline()
        #     for item in f:
        #         info = item.strip().split()

        #         user = Health_info(info[0], info[1], int(info[2]), info[3], float(info[4]), float(info[5]), float(info[6]), info[7])
        #         self.datas.append(user)
        # last_id = int(info[0].split("-")[1])



    def update_file(self):
        data = []

        for info in self.datas:
            data.append({"id": info.id,
                         "name":info.name,
                         "birth": info.birth,
                         "gender": info.gender,
                         "height": info.height,
                         "weight": info.weight,
                         "bmi": info.bmi,
                         "status": info.status})

        # json
        with open(self.file_path_json, "w", encoding= "utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent = 4)
            #json.dump(데이터, 파일 객체, 유니코드 변환 여부, 들여쓰기 칸)
        
        # csv
        # newline: 열마다 들어갈 값?, DictWriter: 데이터가 디렉토리 형태일 때 사용(Writer은 list형태), 헤더 사용 필요, rows: 데이터 다수일 때
        # with open(self.file_path_csv, "w", newline = "", encoding="utf-8-sig") as f:
        #     field = ["id", "name", "birth", "gender", "height", "weight", "bmi", "status"]
        #     writer = csv.DictWriter(f, fieldnames=field)
        #     writer.writeheader()
        #     writer.writerows(data)

        # pkl
        # with open(self.file_path_pkl, "wb") as f:
        #     pickle.dump(data, f)

        # txt
        # with open(self.file_path_txt, "w", encoding="utf-8") as f:
        #     f.write("id name birth gender height weight bmi status\n")

        #     for info in data:
        #         f.write(f"{info["id"]} {info["name"]} {info["birth"]} {info["gender"]} {info["height"]} {info["weight"]} {info["bmi"]:.2f} {info["status"]}\n")