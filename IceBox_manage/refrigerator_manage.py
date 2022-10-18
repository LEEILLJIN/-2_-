#냉장고 관리 화면(초기화면) - 샤에디

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import IceBox_menu
import json
import os
from IceBox_manage.product_delete import product_delete
from IceBox_manage.product_register import register_product
from IceBox_manage.product_search import product_search
from IceBox_manage.product_show import product_show
from IceBox_manage.product_update import search_by_id

def openManageMenu(today):
    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    items = json_data['iceboxes'][0]['items']

    print("-" * 20) #-- Line
    print("[냉장]")
    for i in items:
        print(i.capitalize())
        for j in range(len(items[i])):
            if items[i][j]["partition"] == "냉장":
                for k in items[i][j]:
                    print(f"  {k}: {items[i][j][k]}  ", end = "")
                print("\n",end="")
            else:
                continue
    print("-" * 20) #--- Line
    print("[냉동]")
    for i in items:
        print(i.capitalize())
        for j in range(len(items[i])):
            if items[i][j]["partition"] == "냉동":
                for k in items[i][j]:
                    print(f"  {k}: {items[i][j][k]}  ", end = "")
                print("\n",end="")
            else:
                continue
    print("-" * 20) #-- Line

    print("\n0. 돌아가기")
    print("1. 등록")
    print("2. 조회")
    print("3. 삭제")
    print("4. 검색")
    print("5. 수정")

    while True:
        subMenuInput = str(input("\n번호를 입력하세요. >> "))
        if subMenuInput == '0':
            print("")
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
            search_by_id()
        else:
            print("0이상 5이하의 숫자로 입력해주세요.")
            continue
