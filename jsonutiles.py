import json

Data="stud.json"

def read():
    f=open(Data)
    data=json.load(f)
    f.close()
    return data

  
def write(data_write):
    f=open(Data,"w")
    json.dump(data_write,f,indent=3)
    f.close()
    