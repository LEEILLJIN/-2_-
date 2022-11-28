#냉장고 생성 화면 - 샤에디

import json
import os
import IceBox_menu
import time


def createIceBox(today, UserID):
    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    json_data['today'] = today
    iceBoxes = json_data['iceboxes']

    with open("./data/IceBox_data.json", 'w', encoding='UTF8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2)

    # iceBox 검색
    userIceBox = {}
    p = 0
    while (p < len(iceBoxes)):
        if (iceBoxes[p]["id"] == UserID):
            userIceBox = iceBoxes[p]
            break
        else:
            p += 1
    else:
        print("사용자 아이디가 존재하지 않습니다.")
        time.sleep(1.5)
        IceBox_menu.MainMenu(today, UserID)

    inputData = {
        "refrigerator-size": {
            "vegetable": 0,
            "fruit": 0,
            "dairy-product": 0,
            "frozen-food": 0,
            "meat": 0,
            "seafood": 0,
            "snack": 0,
            "beverage": 0,
            "alcohol": 0,
            "ice-cream": 0,
            "fresh-product": 0,
            "sauce": 0,
            "grains": 0,
            "powder": 0,
            "etc": 0,
            "total": 0
        },
        "refrigerator-temp": ["냉장 온도", "(단위 : 섭씨(°C))"],
        "freezer-size": {
            "vegetable": 0,
            "fruit": 0,
            "dairy-product": 0,
            "frozen-food": 0,
            "meat": 0,
            "seafood": 0,
            "snack": 0,
            "beverage": 0,
            "alcohol": 0,
            "ice-cream": 0,
            "fresh-product": 0,
            "sauce": 0,
            "grains": 0,
            "powder": 0,
            "etc": 0,
            "total": 0
        },
        "freezer-temp": ["냉동 온도", "(단위 : 섭씨(°C))"]
    }

    categoryRef = ["vegetable", "fruit", "dairy-product", "frozen-food", "meat", "seafood", "snack", "beverage", "alcohol", "ice-cream", "fresh-product", "sauce", "grains", "powder", "etc", "total"]
    categoryName = {
        "vegetable": "야채",
        "fruit": "과일",
        "dairy-product": "유제품",
        "frozen-food": "냉동식품",
        "meat": "육류",
        "seafood": "어류",
        "snack": "과자",
        "beverage": "음료",
        "alcohol": "주류",
        "ice-cream": "빙과류",
        "fresh-product": "신선제품",
        "sauce": "소스",
        "grains": "곡식류",
        "powder": "가루류",
        "etc": "기타",
        "total": "총 크기"
    }

    for key in inputData:
        while True:
            try:
                # 냉장, 냉동 크기 설정 할 때
                if (key in ["refrigerator-size", "freezer-size"]):
                    # 어느 파티션 확인
                    partition = None
                    if (key == "freezer-size"):
                        partition = "냉동"
                    else:
                        partition = "냉장"
                    # 안내 문자열 출력
                    print(f"\n{partition}의 각 카테고리 크기를 입력해주세요(단위 : 리터(L))")
                    print("(이전 카테고리 크기를 다시 입력하는 경우, 'b' 입력, 냉장 생성 취소하는 경우 'x' 입력)")

                    totalSize = 0
                    index = 0
                    i = None

                    # for category in inputData[key]:
                    while (index < 16):
                        if (categoryRef[index] == "total"):
                             inputData[key][categoryRef[index]] = totalSize
                             index += 1
                             continue

                        while True:
                            try:
                                i = input(f"  {categoryName[categoryRef[index]]} : ")

                                if (i == "x"):
                                    print("\n냉장고 생성이 취소되었습니다.")
                                    time.sleep(1)
                                    IceBox_menu.MainMenu(today)
                                elif (i == "b"):
                                    print("이전 카테고리 크기를 다시 입력해주세요.")
                                    break

                                i = float(i)
                                if (type(i) != float or i < 0):
                                    raise ValueError
                                else:
                                    inputData[key][categoryRef[index]] = i
                                    totalSize = totalSize + i
                                    break
                            except ValueError:
                                print("다시 입력해주세요.")

                        if (i == 'b'):
                            index -= 1
                        else:
                            index += 1
                    break
                # 냉장, 냉동 온도 설정 할 때
                elif (key in ["refrigerator-temp", "freezer-temp"]):
                    i = input(f"\n{inputData[key][0]}를 입력해주세요 {inputData[key][1]} : ")

                    if (i == "x"):
                        print("\n냉장고 생성이 취소되었습니다.")
                        time.sleep(1)
                        IceBox_menu.MainMenu(today)

                    i = float(i)
                    if (type(i) != float):
                        raise ValueError
                    else:
                        inputData[key] = i
                        break
            except ValueError:
                print("다시 입력해주세요.")

    userIceBox["refrigerator-size"] = inputData["refrigerator-size"]
    userIceBox["refrigerator-temp"] = inputData["refrigerator-temp"]
    userIceBox["freezer-size"] = inputData["freezer-size"]
    userIceBox["freezer-temp"] = inputData["freezer-temp"]
    userIceBox["items"] = {"packaged" : [], "unpackaged" : []}

    #JSON 파일 업데이트
    with open("./data/IceBox_data.json", 'w', encoding='UTF8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2)

    print("")

    IceBox_menu.MainMenu(today, UserID)
