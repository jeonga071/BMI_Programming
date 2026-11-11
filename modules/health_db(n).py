# 파일 읽기

def read_file():
    global last_id
    global datas
    with open(r"C:\Users\user\Desktop\Repo\BMI_Programming\data\data.txt", "r", encoding= "UTF-8") as f:
        hearder = f.readline()
        data = []
        for line in f:
            data.append(line.strip().split(","))
        print(data)
        last_id = line.split(",")[0].split("-")[1]

def get_bmi(height, weight):
    bmi = weight / ((height / 100)**2)
    return bmi

def bmi_to_text(bmi):
    if bmi <= 18.5:
        return "저체중"
    elif bmi <= 24.5:
        return "정상"
    elif bmi <= 30:
        return "과체중"
    else:
        return "비만"


#def random_id():
    print(int(last_id) + 1)

#def input_data():
#    name = input("이름을 입력해주세요: ")
#    birth = int(input("태어난 년도를 입력해주세요: "))
#    gender = input("성별을 입력해주세요: ")
#    height = float(input("키를 입력해주세요: "))
#    weight = float(input("몸무게를 입력해주세요:"))
#    bmi = get_bmi(height, weight)



read_file()
#random_id()