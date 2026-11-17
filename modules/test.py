import pickle
import os

datas = [
    {
        "id": "P2026-0001",
        "name": "홍길동",
        "birth": 1995,
        "gender": "남",
        "height": 175.0,
        "weight": 72.5,
        "bmi": 23.67,
        "status": "과체중"
    }
]

# 저장
with open(os.path.join(os.path.dirname(__file__), "..", "data", "data.pkl"), "wb") as f:
    pickle.dump(datas, f)