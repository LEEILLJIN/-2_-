#냉장고 생성 화면 - 샤에디

import json
import os

import IceBox_menu


def createIceBox(today):
    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    json_data['today'] = today
    iceBox = json_data['iceboxes']

    with open("./data/IceBox_data.json", 'w', encoding='UTF8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2)

    inputData = {
        "refrigerator-size": ["냉장 크기", "(단위 : 리터(L))"],
        "refrigerator-temp": ["냉장 온도", "(단위 : 섭씨(°C))"],
        "freezer-size": ["냉동 크기", "(단위 : 리터(L))"],
        "freezer-temp": ["냉동 온도", "(단위 : 섭씨(°C))"]
    }

    for key in inputData:
        while True:
            try:
                i = float(input(f"{inputData[key][0]}를 입력해주세요 {inputData[key][1]} : "))
                if (key in ["refrigerator-size", "freezer-size"] and i < 0):
                    raise ValueError
                else:
                    inputData[key] = i
                    break
            except ValueError:
                print("다시 입력해주세요.")

    inputData["name"] = "home"
    inputData["items"] = {"packaged" : [], "unpackaged":[]}
    iceBox.append(inputData)
   

    #JSON 파일 업데이트
    with open("./data/IceBox_data.json", 'w', encoding='UTF8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2)

    print("")
    # 냉장고 정보 출력
    # print("\n현재 냉장고")
    # sizeData = ["refrigerator-size","freezer-size"]
    # tempData = ["refrigerator-temp", "freezer-temp"]
    # partition = ["냉장", "냉동"]
    #
    # for i in range(len(partition)):
    #     print(f"{partition[i]} - <{iceBox[0][sizeData[i]]}L, {iceBox[0][tempData[i]]}°C>")
    # print("")

    # 메인 메뉴로 이동
    IceBox_menu.MainMenu(today)
