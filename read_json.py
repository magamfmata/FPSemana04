import json



try:
    caminho = input()
    file=open(caminho, "rt", encoding= "utf-8")
    json_data=file.read()
    data=json.loads(json_data)
    print(data)  
    file.close()
except:
    print("Ocorreu um erro! ")
finally:
    print("Processo concluído! ")
