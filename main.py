from modules import health_db
from modules import health_logic

manager = health_db.Health_Manager()
logic = health_logic()
manager.load_file()
logic.Create_data()
manager.update_file()
