#main menu
import json

import os
import platform
import IceBox_create
import IceBox_remove
import IceBox_update
from IceBox_manage import refrigerator_manage


def MainMenuContent(isIceBox, today, UserID):

    print("1. 냉장고 생성")
    print("2. 냉장고 관리")
    print("3. 냉장고 수정")
    print("4. 냉장고 삭제")
    print("5. 종료")
    while True:
        MainMenuInput = input("\n번호를 입력하세요. >> ")
        if MainMenuInput.isspace() or MainMenuInput == "":
            print("입력된 값이 없습니다.")
            continue
        else:
            MainMenuInput = str(MainMenuInput)
            if MainMenuInput == '1':
                if isIceBox:
                    print("이미 냉장고가 생성되어 있습니다.")
                    continue
                else:
                    if platform.system() == "Windows":
                        os.system("cls")
                    elif platform.system() == "Darwin":
                        os.system("clear")
                    IceBox_create.createIceBox(today, UserID)

            elif MainMenuInput == '2':
                if isIceBox:
                    if platform.system() == "Windows":
                        os.system("cls")
                    elif platform.system() == "Darwin":
                        os.system("clear")
                    refrigerator_manage.openManageMenu(today, UserID)
                else:
                    print("냉장고를 먼저 생성해주세요.")
                    continue
            elif MainMenuInput == '3':
                if isIceBox:
                    if platform.system() == "Windows":
                        os.system("cls")
                    elif platform.system() == "Darwin":
                        os.system("clear")
                    IceBox_update.icebox_updater(UserID)
                else:
                    print("냉장고를 먼저 생성해주세요.")
                    continue
            elif MainMenuInput == '4':
                if isIceBox:
                    if platform.system() == "Windows":
                        os.system("cls")
                    elif platform.system() == "Darwin":
                        os.system("clear")
                    IceBox_remove.icebox_remover()
                else:
                    print("냉장고를 먼저 생성해주세요.")
                    continue
            elif MainMenuInput == '5':
                print("프로그램이 종료되었습니다.")
                exit(0)
            else:
                print("1이상 5이하의 숫자로 입력해주세요.")
                continue

def CalculateUsedSize(partition, category, icebox):
    PackagedList = icebox["items"]["packaged"]
    UnpackagedList = icebox["items"]["unpackaged"]
    UsedSize = 0
    # print(f"partition = {partition}, category = {category}", end = " ")
    if PackagedList :
        for i in PackagedList:
            if (i["category"] == category) and (i["partition"] == partition):
                UsedSize += i["total-bulk"]
    else :
        UsedSize += 0

    if UnpackagedList :
        for i in UnpackagedList:
            if (i["category"] == category) and (i["partition"] == partition): 
                UsedSize += i["leftover-number"] * i["bulk-for-unit"]  
    else :
        UsedSize += 0

    return UsedSize  



def MainMenu(today,UserID):
    #today랑 userID도 같이 인자로 받아와야함
    isIceBox = False
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")

    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    json_data['today'] = today
    with open("./data/IceBox_data.json", 'w', encoding='UTF8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2)
    iceBox = json_data['iceboxes']
   
    if len(iceBox[int(UserID)-1]) == 2:
        # len가 2이면(id, password) 아직 냉장고를 생성하지 않은 것
        print("냉장고를 생성해주세요.")
        MainMenuContent(isIceBox, today, UserID)
    else:
        isIceBox = True
        print("현재 냉장고")
        iterator = [3,2]
        PartitionSizeDataList = {
            "vegetable" : "야채", 
            "beverage" : "음료", 
            "etc" : "기타",
            "fruit" : "과일", 
            "alcohol" : "주류",
            "dairy-product" : "유제품", 
            "ice-cream" : "빙과류", 
            "frozen-food" : "냉동식품", 
            "fresh-product" : "신선제품", 
            "meat" : "육류", 
            "sauce" : "소스", 
            "seafood" : "어류", 
            "grains" : "곡식류", 
            "snack" : "과자", 
            "powder" : "가루류"
            }
        PrintLine = 7
        refriPartitionSizeData = iceBox[int(UserID)-1]["refrigerator-size"]
        freezerPartitionSizeData = iceBox[int(UserID)-1]["freezer-size"]

        iceBoxSizeData = [refriPartitionSizeData, freezerPartitionSizeData ]
        iceBoxtmpData = ["refrigerator-temp", "freezer-temp"]
        partition = ["냉장", "냉동"]
        for i in range(len(partition)):
            cnt =3 
            iteratorCheck = True
            print()
            print(f"{partition[i]} - <{iceBoxSizeData[i]['total']}L, {iceBox[0][iceBoxtmpData[i]]}°C>")
            print()
            print("사용 부피/총 부피")
            print()
            for _ in range(PrintLine):
                if iteratorCheck:
                    for j in range(iterator[0]):
                        # print(f"{j}", end=" ")
                        print(f"{list(PartitionSizeDataList.values())[j]} - {CalculateUsedSize(partition[i],list(PartitionSizeDataList.values())[j],iceBox[int(UserID)-1])}L/{iceBoxSizeData[i][list(PartitionSizeDataList.keys())[j]]}L", end="\t\t\t")
                    iteratorCheck = False
                else:
                    for j in range(iterator[1]):
                        if (list(PartitionSizeDataList.values())[cnt+j] == "유제품") or (list(PartitionSizeDataList.values())[cnt+j] == "냉동식품") :
                            print(f"{list(PartitionSizeDataList.values())[cnt+j]} - {CalculateUsedSize(partition[i], list(PartitionSizeDataList.values())[cnt+j],iceBox[int(UserID)-1])}L/{iceBoxSizeData[i][list(PartitionSizeDataList.keys())[cnt+j]]}L", end="\t\t")
                        else :
                            print(f"{list(PartitionSizeDataList.values())[cnt+j]} - {CalculateUsedSize(partition[i], list(PartitionSizeDataList.values())[cnt+j],iceBox[int(UserID)-1])}L/{iceBoxSizeData[i][list(PartitionSizeDataList.keys())[cnt+j]]}L", end="\t\t\t")

                    cnt += iterator[1]
                print()
        MainMenuContent(isIceBox,today, UserID)

