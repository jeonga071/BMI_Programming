from modules import health_db
from modules import health_logic

manager = health_db.Health_Manager()
manager.load_file()

# 파일 저장 
# create = health_logic.Create_data(manager)
# create.add_file()
# manager.update_file()

# 파일 조회
retrieve = health_logic.Retrieve_data(manager)
retrieve.search()