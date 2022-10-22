#냉장고 관리 화면(초기화면) - 샤에디

import json
import os

import IceBox_menu
from IceBox_manage.product_delete import product_delete
from IceBox_manage.product_register import register_product
from IceBox_manage.product_search import product_search
from IceBox_manage.product_show import product_show
from IceBox_manage.product_update import product_update
from datetime import datetime, timedelta

def openManageMenu(today):
    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    items = json_data['iceboxes'][0]['items']
    today = datetime.strptime(today, '%Y-%m-%d').date()
    # print("오늘 날짜:", today, "\n")

    keyNames = {
        "partition": "파티션",
        "name": "상품명",
        "category": "카테고리",
        "ID": "상품ID",
        "total-bulk": "총량",
        "leftover-bulk": "현재량",
        "recommended-temp": "보관권장온도",
        "expiration-date": "유통기한",
        "bulk-for-unit": "한개당 수량",
        "total-number": "총량",
        "leftover-number": "현재량"
    }

    # keyNames = {
    #     "partition": "파티션",
    #     "name": "상품명",
    #     "category": "카테고리",
    #     "ID": "상품ID",
    #     "total-bulk": "총부피",
    #     "leftover-bulk": "남은 부피",
    #     "recommended-temp": "보관권장온도",
    #     "expiration-date": "유통기한",
    #     "bulk-for-unit": "한개당 수량",
    #     "total-number": "총수량",
    #     "leftover-number": "현재수량"
    # }

    print("냉장")
    for i in items:
        for j in range(len(items[i])):
            expDate = datetime.strptime(items[i][j]['expiration-date'], '%Y-%m-%d').date()
            cnt = 0;
            if items[i][j]["partition"] == "냉장":
                if (today >= expDate):
                    print('\u001b[2;31m', end="")
                elif (today < expDate and (today + timedelta(5)) >= expDate):
                    print('\u001b[2;33m', end="")
                print("<",end="")
                for k in items[i][j]:
                    cnt += 1
                    if (k in ["partition", "bulk-for-unit"]):
                        continue
                    else:
                        print(f"{keyNames[k]}: {items[i][j][k]}", end = "")
                        if (cnt != len(items[i][j])):
                            print(", ", end = "")
                print(">\u001b[0;0m")
        else:
            continue

    print("\n냉동")
    for i in items:
        for j in range(len(items[i])):
            expDate = datetime.strptime(items[i][j]['expiration-date'], '%Y-%m-%d').date()
            cnt = 0;
            if items[i][j]["partition"] == "냉동":
                if (today >= expDate):
                    print('\u001b[2;31m', end="")
                elif (today < expDate and (today + timedelta(5)) > expDate):
                    print('\u001b[2;33m', end="")
                print("<",end="")
                for k in items[i][j]:
                    cnt += 1
                    if (k in ["partition", "bulk-for-unit"]):
                        continue
                    else:
                        print(f"{keyNames[k]}: {items[i][j][k]}", end = "")
                        if (cnt != len(items[i][j])):
                            print(", ", end = "")
                print(">\u001b[0;0m")
        else:
            continue

    # str로 다시 바꾸기
    today = str(today)

    print("\n0. 돌아가기")
    print("1. 등록")
    print("2. 조회")
    print("3. 삭제")
    print("4. 검색")
    print("5. 수정")

    while True:
        subMenuInput = str(input("\n번호를 입력하세요. >> "))
        if subMenuInput == '0':
            IceBox_menu.MainMenu(today)
        elif subMenuInput == '1':
            register_product()
        elif subMenuInput == '2':
            product_show()
        elif subMenuInput == '3':
            product_delete()
        elif subMenuInput == '4':
            product_search()
        elif subMenuInput == '5':
            product_update()
        else:
            print("0이상 5이하의 숫자로 입력해주세요.")
            continue
