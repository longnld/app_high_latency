import os
from datetime import datetime,timedelta
import pickle


if __name__ == "__main__":
    settings = {
        "delay":0,
        "expired": datetime.now() + timedelta(days=30),
        "uuid":""
        }
    data = pickle.dumps(settings)
    with open("settings.dat", "wb") as f:
        f.write(data)
