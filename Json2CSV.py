import os
import csv
import json
def extractJson(path):
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            printFileName(filename)

def printFileName(filename):
    name=filename.split('.')[0]+".csv"
    print(name)
    data = json.load(open(filename))
    key1,value1=list(data.items())[0]
    new_arr=[]
    for row in value1:
        row1=[]
        for key,value in row.items():
            row1.append(str(key))
    new_arr.append((list(set(row1))))
    # print(new_arr)
    l=len(list(data.items())[0])
    arr2=[]
    for i in range(0,l):
        for heading in new_arr[0]:
            arr2.append(value1[i][heading])
        new_arr.append(arr2)
        arr2=[]
    output_dir = os.path.join(os.pardir, 'Output',name)
    with open(output_dir, "w") as f:
        print()
        writer = csv.writer(f)
        writer.writerows(new_arr)

if __name__ == '__main__':
    user_input = input("Enter the path of your file: ")
    extractJson(user_input)
