import datetime

today=datetime.date.today()
current_time=datetime.datetime.now().hour
print(today,current_time)

#operating system
import os

current_dir=os.getcwd()
print(current_dir)

#json data
import json
data={"name":"alice","age":30}
json_string=json.dumps(data)
print(json_string)