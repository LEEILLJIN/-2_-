#main menu
import json
import IceBox_create
from IceBox_manage import refrigerator_manage
import IceBox_update
import IceBox_remove


def MainMenuContent(isIceBox, today):
    print("1. 냉장고 생성")
    print("2. 냉장고 관리")
    print("3. 냉장고 수정")
    print("4. 냉장고 삭제")
    print("5. 종료")

    while True:
        MainMenuInput = str(input("\n번호를 입력하세요. >> "))
        if MainMenuInput == '1':
            if isIceBox:
                print("이미 냉장고가 생성되어 있습니다.")
                continue
            else:
                IceBox_create.createIceBox(today)

        elif MainMenuInput == '2':
            if isIceBox:
                refrigerator_manage.openManageMenu(today)
            else:
                print("냉장고를 먼저 생성해주세요.")
                continue
        elif MainMenuInput == '3':
            if isIceBox:
                IceBox_update.icebox_updater()
            else:
                print("냉장고를 먼저 생성해주세요.")
                continue
        elif MainMenuInput == '4':
            if isIceBox:
                IceBox_remove.icebox_remover()
            else:
                print("냉장고를 먼저 생성해주세요.")
                continue
        elif MainMenuInput == '5':
            print("프로그램이 종료되었니다.")
            exit(0)
        else:
            print("1이상 5이하의 숫자로 입력해주세요.")
            continue


def MainMenu(today):
<<<<<<< HEAD
    
=======
>>>>>>> 9db3aac1bb3d7578f202f93dda30ccbe2fee6962
    isIceBox = False
    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    if json_data["iceboxes"]:
        isIceBox = True
        print("현재 냉장고")
        iceBox = json_data['iceboxes']
        iceBoxSizeData = ["refrigerator-size","freezer-size"]
        iceBoxtmpData = ["refrigerator-temp", "freezer-temp"]
        partion = ["냉장", "냉동"]
        for i in range(len(partion)):
            print(f"{partion[i]} - <{iceBox[0][iceBoxSizeData[i]]}L, {iceBox[0][iceBoxtmpData[i]]}°C>")
        MainMenuContent(isIceBox,today)
    else:
        print("냉장고를 생성해주세요.")
<<<<<<< HEAD
        MainMenuContent(isIceBox, today)

# def MainMenu(today):
#     with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
#         json_data = json.load(file)

#     iceBox = json_data["iceboxes"]
#     isIceBox = iceBox[0]["creation-status"]

#     if isIceBox:
#         print("\n현재 냉장고")
#         iceBox = json_data['iceboxes']
#         sizeData = ["refrigerator-size","freezer-size"]
#         tempData = ["refrigerator-temp", "freezer-temp"]
#         partition = ["냉장", "냉동"]

#         for i in range(len(partition)):
#             print(f"{partition[i]} - <{iceBox[0][sizeData[i]]}L, {iceBox[0][tempData[i]]}°C>")
#         print("")
#         MainMenuContent(isIceBox,today)

#     else:
#         print("냉장고를 생성해주세요.")
#         MainMenuContent(isIceBox, today)
=======
        MainMenuContent(isIceBox, today)
>>>>>>> 9db3aac1bb3d7578f202f93dda30ccbe2fee6962
