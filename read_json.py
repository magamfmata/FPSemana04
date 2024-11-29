import json

file=str(input())

try:
    file=open("data.json", "rt")
    json_data=file.read()

    data=json.loads(json_data)
        
    print(data)

except:
    print("Ocorreu um erro")
finally:
    print("Processo concluído!")