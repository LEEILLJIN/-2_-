#main menu
import json

def MainMenuContent(isIceBox, today):
    print("1. 냉장고 생성")
    print("2. 냉장고 관리")
    print("3. 냉장고 수정")
    print("4. 냉장고 삭제")
    print("5. 종료")

    while True:
        MainMenuInput = int(input())
        if MainMenuInput == 1:
            if isIceBox:
                print("이미 냉장고가 생성 되어 있습니다.")
                continue
            else:
                print("IceBox_creat로 이동")
                print(f"today : {today}")
                print("이때 today를 인자로 전달하여 json파일을 생성할 때 data로 넣어야함")
        elif MainMenuInput == 2:
            if isIceBox:
                print("IceBox_manage로 이동")
            else:
                print("냉장고를 먼저 생성해주세요")
                continue
        elif MainMenuInput == 3:
            if isIceBox:
                print("IceBox_update로 이동")
            else:
                print("냉장고를 먼저 생성해주세요")
                continue
        elif MainMenuInput == 4:
            if isIceBox:
                print("IceBox_remove로 이동")
            else:
                print("냉장고를 먼저 생성해주세요")
                continue
        elif MainMenuInput == 5:
            exit(0)
        else:
            print("1이상 5이하의 숫자로 입력해주세요.")
            continue

        

def MainMenu(today):
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
        MainMenuContent(isIceBox, today)

