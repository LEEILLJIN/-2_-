# 상품 수정 화면
# 상품 수정 화면
#냉장고 관리 화면에서 사용자가 ‘5’를 입력하면 나오는 화면입니다.

import datetime
import json
import os
import sys
from unicodedata import category
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import IceBox_menu

path = "./data/IceBox_data.json"

packaged_updatable_cate = {'상품명': 'name', '총량':'total-bulk', '현재량':'leftover-bulk', '카테고리':'category', '보관권장온도':'recommended-temp', '유통기한':'expiration-date'}
unpackaged_updatable_cate = {'상품명': 'name', '총량' : 'total-number', '현재량' : 'leftover-number', '카테고리':'category', '보관권장온도':'recommended-temp', '유통기한':'expiration-date'}
special_character = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
category_list = {
    '1' : '야채', '2':'과일', '3':'유제품', '4':'냉동식품', '5':'육류', '6':'어류', '7':'과자', '8':'음료', '9':'주류', '10':'빙과류', '11':'신선제품', '12':'소스', '13':'곡식류', '14':'가루류', '15':'기타'
}
def main_screen2() :
    with open(path, "r", encoding='UTF8') as file :
          
            data = json.load(file)
            today = data['today']
            IceBox_menu.MainMenu(today)

def search_by_id():
    #수정할 상품 ID 입력하여 해당 ID의 예외 처리 후 적법할 경우 상품을 찾는 함수
    cnt = 0
    while True:
        product_id = input("수정할 상품의 ID를 입력해주세요 : ")
        if product_id.isdigit() == False:
            #ID 입력 예외 처리
            continue
        else :
            #ID입력이 적합한 경우
                cnt = view_item_data(product_id)
                if cnt == 0 :
                    print("입력한 ID와 일치하는 상품이 존재하지 않습니다.")
                    continue
                else:
                    update_product(product_id)
        cnt=0 

def view_item_data(product_id):
    #상품의 정보를 보여주는 함수
    cnt = 0
    with open(path, "r", encoding='UTF8') as file :
                    data = json.load(file)
                    icebox = data['iceboxes']
                    items = icebox[0]["items"]
                    for item in items['packaged'] :
                        if(int(product_id) == item['ID']) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-bulk"], item["leftover-bulk"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1

                        else :
                            continue
                        
                    for item in items['unpackaged'] :
                        if(int(product_id) == item['ID']) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}개, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"],  item["total-number"], item["leftover-number"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1

                        else :
                            continue
    return cnt
def validate_cate(update_cate):
    #수정할 항목 입력 검사 함수
    if update_cate in packaged_updatable_cate.keys():
        return True
    else:
        return False

def validate_date(today):
    try:
        temp = today.split("-")
        year = int(temp[0])
        month = int(temp[1])
        day = int(temp[2])

        if 2000 > year or 2999 < year:
            return False
        for i in range(len(temp)):
            temp[i] = str(int(temp[i]))
        today='-'.join(temp)
        datetime.datetime.strptime(today,"%Y-%m-%d")
        return today
    except ValueError:
        # print("Incorrect data format({0}), should be YYYY-MM-DD".format(today))
        return False

def validate_data(update_cate,update_data):
    #수정할 항목의 정보 입력 검사 함수
    cnt = 0
    for i, item in enumerate( packaged_updatable_cate.keys()):
        if item == update_cate:
            if i == 0:
                #상품명 입력 검사
                for validation in update_data :
                    if validation in special_character :
                        print("특수문자를 사용할 수 없습니다.")
                        cnt += 1
                if cnt == 0:
                    return True
                else:
                    return False
            elif i == 1:
                #총량 입력 검사
                #packaged의 총량은 남은냉장고 부피보다 작아야되고
                #unpackaged의 총량은 현재 개수보다 작아야됨
                
                #둘다 1~100의 정수로 입력 규칙을 정하자
                if update_data.isalpha() or update_data.find(' ')>=0:
                    #숫자가 아니거나 공백류가 포함된 경우
                    return False
                elif 1 > int(update_data) or int(update_data) > 100 :
                    cnt += 1
                else:
                    for validation in update_data :
                        if validation in special_character :
                            #특수문자가 포함되어있는 경우
                            cnt += 1
            
                if cnt == 0:
                    #입력이 적법한 경우
                    return True
                else:
                    return False

            elif i ==2:
                #현재량 입력 검사
                #packaged의 현재량은 현재부피보다 작아야되고
                #unpackaged의 현재량은 현재개수보다 작아야됨
                if update_data.isalpha() or update_data.find(' ')>=0:
                    #숫자가 아니거나 공백류가 포함된 경우
                    return False
                elif 1 > int(update_data) or int(update_data) > 100 :
                    #입력 범위에 벗어난 경우
                    cnt += 1
                else:
                    for validation in update_data :
                        if validation in special_character :
                            #특수문자가 포함되어있는 경우
                            cnt += 1
                
                if cnt == 0:
                    #입력이 적법한 경우
                    return True
                else:
                    return False
            elif i ==3:
                #카테고리 입력 검사
                #1.야채, 2.과일, 3.유제품, 4.냉동식품, 5.육류, 6.어류, 7.과자, 8.음료, 9.주류, 10.빙과류, 11.신선제품, 12.소스, 13.곡식류, 14.가루류, 15.기타
                if update_data.isalpha() :
                    #숫자가 아닌 경우
                    return False
                elif 1 > int(update_data) or int(update_data) > 15:
                    #입력 범위에 벗어난 경우
                    cnt += 1
                else:
                    for validation in update_data :
                        if validation in special_character :
                            #특수문자가 포함되어있는 경우
                            cnt += 1

                if cnt == 0:
                    #입력이 적법한 경우
                    return True
                else:
                    return False
            elif i == 4:
                #보관 권장 온도 입력 검사
                #공백류가 들어있지 않고 선행 0을 허용하지 않음
                num = update_data.lstrip("-")
                num_remove_zero = num.lstrip("0")
                #선행 0 처리
                if num != '0' and (num.isdigit() == False or num != num_remove_zero):
                    cnt += 1
                
                if cnt == 0:
                #입력이 적법한 경우
                    return True
                else:
                    return False
            elif i == 5:
                #유통기한 입력 검사
                # import IceBox
                with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
                    json_data = json.load(file)
                today_data = json_data["today"]
                today = time.strptime(today_data,"%Y-%m-%d")
                
                if (type(validate_date(update_data)) == str):
                    temp = update_data.split("-")
                    for i in range(len(temp)):
                        temp[i] = str(int(temp[i]))
                    update_data='-'.join(temp)
                    input_date = time.strptime(update_data,"%Y-%m-%d")
                    if today > input_date:
                        return False
                    else :
                        return True
                else: 
                    return False

def update_product(product_id):

    while True:
        print()
        update_cate = input("수정할 항목을 입력해주세요 :")
        if update_cate == '카테고리':
            print("1.야채, 2.과일, 3.유제품, 4.냉동식품, 5.육류, 6.어류, 7.과자, 8.음료, 9.주류, 10.빙과류, 11.신선제품, 12.소스, 13.곡식류, 14.가루류, 15.기타")
        update_data = input("수정 정보를 입력해주세요 :")
        # print(f"validate_cate : {validate_cate(update_cate)}")
        # print(f"validate_data : {validate_data(update_cate, update_data)}")
        if validate_cate(update_cate):
            if validate_data(update_cate, update_data):
                #올바른 수정 항목과 수정 정보가 입력된 경우
                with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
                    json_data = json.load(file)

                icebox = json_data['iceboxes']
                items = icebox[0]["items"]
                packaged_itemlist = items["packaged"]
                unpackaged_itemlist = items["unpackaged"]

                for i,item in enumerate(packaged_itemlist):
                    if  int(product_id) == item["ID"]:
                        if update_cate == '카테고리':
                            update_data = category_list[update_data]
                        elif update_cate in ['총량','현재량','보관권장온도']:
                            update_data = int(update_data)
                        elif update_cate == '유통기한':
                            temp = update_data.split("-")
                            for i in range(len(temp)):
                                temp[i] = str(int(temp[i]))
                            update_data='-'.join(temp)

                        item[packaged_updatable_cate[update_cate]] = update_data
                        with open('./data/IceBox_data.json', 'w', encoding='utf-8') as make_file:

                            json.dump(json_data, make_file, indent="\t", ensure_ascii=False)

                for i,item in enumerate(unpackaged_itemlist):
                    if  int(product_id) == item["ID"]:
                        if update_cate == '카테고리':
                            update_data = category_list[update_data]
                        elif update_cate in ['현재량','보관권장온도','총량']:
                             update_data = int(update_data)
                        item[unpackaged_updatable_cate[update_cate]] = update_data
                        with open('./data/IceBox_data.json', 'w', encoding='utf-8') as make_file:

                            json.dump(json_data, make_file, indent="\t", ensure_ascii=False)
                view_item_data(product_id)
                while True:
                    print("0.돌아가기")
                    print("1.추가수정")
                    user_input = input("메뉴를 입력하세요 : ")
                    print()
                    if user_input == '0':
                        main_screen2()
                        break
                        exit(0)
                    elif user_input == '\n':
                        continue
                    elif user_input == '1':
                        search_by_id()
            else:
                #잘못된 수정 항목이나 수정 정보가 입력된 경우
                print("잘못된 수정 항목이거나 수정 정보 값입니다. 다시 입력해주세요.")
                continue
        else:
            #잘못된 수정 항목이나 수정 정보가 입력된 경우
            print("잘못된 수정 항목이거나 수정 정보 값입니다. 다시 입력해주세요.")
            continue

def product_update():
   search_by_id()


search_by_id()