class Health_info:
    def __init__(self, name, height, weight, bmi, status):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.status = status

    def get_bmi(self):
        bmi = self.weight / ((self.height / 100)**2)
        return bmi

    def bmi_to_text(self, bmi):
        if bmi <= 18.5:
            return "저체중"
        elif bmi <= 24.5:
            return "정상"
        elif bmi <= 30:
            return "과체중"
        else:
            return "비만"
