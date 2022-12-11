# 상품 수정 화면
#냉장고 관리 화면에서 사용자가 ‘5’를 입력하면 나오는 화면입니다.

import datetime
import json
import os
import sys
from unicodedata import category
import time
import IceBox
from IceBox import validate_date

from .product_register import getBulk, getValidSize

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import IceBox_menu

path = "./data/IceBox_data.json"

packaged_updatable_cate = {'상품명': 'name', '총량':'total-bulk', '현재량':'leftover-bulk', '카테고리':'category', '보관권장온도':'recommended-temp', '유통기한':'expiration-date'}
unpackaged_updatable_cate = {'상품명': 'name', '총량' : 'total-number', '현재량' : 'leftover-number', '카테고리':'category', '보관권장온도':'recommended-temp', '유통기한':'expiration-date'}
special_character = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
category_list = {
    '1' : '야채', '2':'과일', '3':'유제품', '4':'냉동식품', '5':'육류', '6':'어류', '7':'과자', '8':'음료', '9':'주류', '10':'빙과류', '11':'신선제품', '12':'소스', '13':'곡식류', '14':'가루류', '15':'기타'
}

category_list_english_to_korean = {
    '야채' : 'vegetable', '과일' : 'fruit' , '유제품': 'dairy-product', '냉동식품':'frozen-food', '육류':'meat', '어류':'seafood', '과자':'snack', '음료':'beverage', '주류':'alcohol', '빙과류':'ice-cream', '신선제품':'fresh-product', '소스':'sauce', '곡식류':'grains', '가루류':'powder', '기타':'etc'
}

global global_product_id
global global_user_id
global global_item
global global_icebox



def main_screen2() :
    with open(path, "r", encoding='UTF8') as file :          
            data = json.load(file)
            today = data['today']
            IceBox_menu.MainMenu(today,global_user_id)

def search_by_id():
    #수정할 상품 ID 입력하여 해당 ID의 예외 처리 후 적법할 경우 상품을 찾는 함수
    #user_by_id
    cnt = 0
    global global_product_id 
    while True:
        global_product_id = input("수정할 상품의 ID를 입력해주세요 : ")
        if global_product_id.isdigit() == False:
            #ID 입력 예외 처리
            global_product_id = global_product_id.lstrip()
            global_product_id = global_product_id.rstrip()
            if len(global_product_id) == 0:
                print("입력한 값이 없습니다.")
            else :
                print("입력한 ID와 일치하는 상품이 존재하지 않습니다.")
            continue
        else :
            #ID입력이 적합한 경우
                cnt = view_item_data(global_product_id)
                if cnt == 0 :
                    print("입력한 ID와 일치하는 상품이 존재하지 않습니다.")
                    continue
                else:
                    update_product()
        cnt=0 


def view_item_data(global_product_id):
    global global_user_id
    #상품의 정보를 보여주는 함수
    cnt = 0
    with open(path, "r", encoding='UTF8') as file :
                    data = json.load(file)
                    icebox_select = data['iceboxes'][0] #일단 0번째 냉장고로 초기화

                    for icebox in data['iceboxes'] :
                        if str(global_user_id) == icebox['id']: 
                            icebox_select = icebox
                            break
                        

                    items = icebox_select["items"]
                    for item in items['packaged'] :
                        if(int(global_product_id) == item['ID']) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}L, 현재량: {}L, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-bulk"], item["leftover-bulk"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1
                        else :
                            continue
                        
                    for item in items['unpackaged'] :
                        if(int(global_product_id) == item['ID']) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}개, 현재량: {}개, 개당부피: {}L, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"],  item["total-number"], item["leftover-number"],item["bulk-for-unit"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1
                        else :
                            continue
    return cnt


def validate_cate(update_cate):
    #수정할 항목 입력 검사 함수
    if update_cate in packaged_updatable_cate.keys():
        return True
    else:
        if len(update_cate) == 0:
            print("입력한 값이 없습니다.")
        return False


def get_item_by_id(g):
    global global_user_id
    global global_item
    global global_icebox
    global global_product_id

    with open(path, "r", encoding='UTF8') as file :
        data = json.load(file)
        icebox_select = data['iceboxes'][0]

        for icebox in data['iceboxes'] :
            if str(global_user_id) == icebox['id']: 
                icebox_select = icebox
                break
                        # else:
                        #     ice_box_index += 1

        global_icebox = icebox_select
        items = icebox_select["items"]

        for item in items['packaged'] :
            if int(global_product_id) == item['ID'] :
                global_item = item
                return item
            else : 
                continue
            
        for item in items['unpackaged'] :
            if int(global_product_id) == item['ID'] :
                global_item = item
                return item
            else :
                continue

def CalculateUsedSize(partition, category, icebox): 

    #냉장,냉동 #한국말카테고리(과일) #냉장고
    PackagedList = icebox["items"]["packaged"]
    UnpackagedList = icebox["items"]["unpackaged"]
    UsedSize = 0

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


# def getLeftoverBulk(inpartition): #냉장고,냉동고 남은부피 계산하기
#     with open(path, "r", encoding='UTF8') as file :
#         data = json.load(file)
#         icebox = data['iceboxes']
#         items = icebox[0]["items"]
#         rtotalsize = int(icebox[0]['refrigerator-size'])
#         ftotalsize = int(icebox[0]['freezer-size'])

#         rleftsize = rtotalsize
#         fleftsize = ftotalsize

#     if inpartition == '냉장':
#         for item in items['packaged'] :
#             if item['partition'] == '냉장':
#                 rleftsize -= item['total-bulk']
        
#         for item in items['unpackaged'] :
#             if item['partition'] == '냉장':
#                 rleftsize -= item['leftover-number']*item['bulk-for-unit']

#         return rleftsize
    
#     else :
#         for item in items['packaged'] :
#             if item['partition'] == '냉동':
#                 fleftsize -= item['total-bulk']
        
#         for item in items['unpackaged'] :
#             if item['partition'] == '냉동':
#                 fleftsize -= item['leftover-number']*item['bulk-for-unit']
        
#         return fleftsize



def packaged_isitvalid_total_bulk(global_product_id,update_data):
    cnt = 0
    #아이템이 냉동인지 냉장인지
    #아이템이 패키지인지 언패키지인지
    selected_item = get_item_by_id(global_product_id)
    global global_item
    global global_icebox
    
    partition = global_item['partition'] #냉장인지 냉동인지
    category = global_item['category'] #카테고리(한국말)
    category_english = category_list_english_to_korean.get(category) #카테고리(영어)

    
    if partition == '냉장':
        if global_icebox['refrigerator-size'][category_english] - CalculateUsedSize(partition, category, global_icebox) + global_item['total-bulk'] < int(update_data) :
            cnt += 1
    else :
        if global_icebox['freezer-size'][category_english] - CalculateUsedSize(partition, category, global_icebox) + global_item['total-bulk'] < int(update_data) :
            cnt += 1
    
    if cnt <= 0:
        return True
    else :
        return False



def unpackaged_isitvalid_leftover_number(global_product_id,update_data):
    cnt = 0
    #아이템이 냉동인지 냉장인지
    #아이템이 패키지인지 언패키지인지
    #패키지가 없는경우
    #냉장고에서 남은 부피 >= update_data(수량) * selected_item['bulk-for-unit'] 

    global global_item
    global global_icebox
    
    partition = global_item['partition'] #냉장인지 냉동인지
    category = global_item['category'] #카테고리(한국말)
    category_english = category_list_english_to_korean.get(category) #카테고리(영어)

    if partition == '냉장':
        if global_icebox['refrigerator-size'][category_english] - CalculateUsedSize(partition, category, global_icebox) + global_item['bulk-for-unit']*global_item['leftover-number'] < int(update_data) * global_item['bulk-for-unit'] :
            cnt += 1
    else :
        if global_icebox['freezer-size'][category_english] - CalculateUsedSize(partition, category, global_icebox) + global_item['bulk-for-unit']*global_item['leftover-number'] < int(update_data) * global_item['bulk-for-unit'] :
            cnt += 1
    
    if cnt <= 0:
        return True
        
    else :
        return False




def validate_data(update_cate,update_data):
    #수정할 항목의 정보 입력 검사 함수
    global global_product_id
    cnt = 0
    for i, item in enumerate(packaged_updatable_cate.keys()):
        if item == update_cate:

            selected_item = get_item_by_id(global_product_id)

            d = update_data.strip()
            if len(d) == 0:
                print("입력한 값이 없습니다.")
                return False

            if i == 0: 
                #상품명 입력 검사
                if update_data.find(' ')==0 or update_data.find(' ') == len(update_data)-1 or len(update_data) <= 0:
                #공백류가 맨앞이나 맨뒤에 있다면
                    print("잘못된 수정 정보입니다. 앞뒤에 공백류를 포함할 수 없습니다.")
                    cnt += 1
                for validation in update_data :
                    if validation in special_character :
                        cnt += 1
                

                if cnt == 0:
                    return True
                else:
                    return False

            elif i == 1:
                #총량 입력 검사
                #패키지드
                if update_data.isdigit() == False or update_data.find('-') >= 0:
                    #숫자가 아닌 경우
                    if update_data.find(' ') < 0:
                        print("잘못된 수정 정보입니다. 숫자로 입력해주세요.")
                        
                    cnt += 1

                if update_data.find(' ')>=0 :
                    #공백류가 포함된 경우
                    print("잘못된 수정 정보입니다. 공백류를 포함할 수 없습니다.")
                    cnt += 1
                
                if update_data.find('0') == 0:
                    print("잘못된 수정 정보입니다. 선행0을 포함하지 않아야 합니다.")
                    cnt += 1

                

                if cnt == 0:
                    if 'total-bulk' in selected_item :
                        if int(update_data) < selected_item['leftover-bulk']:
                            print("잘못된 수정 정보입니다. 현재량은 총량을 넘길 수 없습니다.")
                            cnt += 1

                        if packaged_isitvalid_total_bulk(global_product_id,update_data) == False:
                            print('잘못된 수정 정보입니다. 해당 칸의 공간이 부족합니다.')
                            cnt += 1
                
                #언패키지드
                    else :
                        if int(update_data) < selected_item['leftover-number'] :
                            print("잘못된 수정 정보입니다. 현재량은 총량을 넘길 수 없습니다.")
                            cnt += 1
                        
                        if int(update_data) < 1 or int(update_data) > 100:
                            print("잘못된 수정 정보입니다. 1이상 100이하의 정수로 입력해주세요.")
                            cnt += 1

                if cnt == 0:
                    #입력이 적법한 경우
                    return True
                else:
                    return False

            elif i ==2:
                #현재량 입력 검사
                if update_data.isdigit() == False or update_data.find('-') >= 0:
                    #숫자가 아닌 경우
                    if update_data.find(' ') < 0:
                        print("잘못된 수정 정보입니다. 숫자로 입력해주세요.")

                    cnt += 1

                if update_data.find(' ')>=0:
                    #공백류가 포함된 경우
                    print("잘못된 수정 정보입니다. 공백류를 포함할 수 없습니다.")
                    cnt += 1
                
                if update_data.find('0') == 0:
                    print("잘못된 수정 정보입니다. 선행0을 포함하지 않아야 합니다.")
                    cnt += 1
                                

                if cnt == 0 : 
                    #패키지드
                    if 'total-bulk' in selected_item :
                        if selected_item['total-bulk'] < int(update_data):
                            print('잘못된 수정 정보입니다. 현재량은 총량을 넘길 수 없습니다.')
                            cnt += 1

                    #언패키지드
                    else :
                        if unpackaged_isitvalid_leftover_number(global_product_id,update_data) == False:
                            print("잘못된 수정 정보입니다. 해당 칸의 공간이 부족합니다.")
                            cnt += 1
                        
                        if selected_item['total-number'] < int(update_data): 
                            print("잘못된 수정 정보입니다. 현재량은 총량을 넘길 수 없습니다.")
                            cnt += 1
                        
                        if int(update_data) < 1 or int(update_data) > 100:
                            print("잘못된 수정 정보입니다. 1이상 100이하의 정수로 입력해주세요.")
                            cnt += 1

                            
                #입력이 적법한 경우            
                if cnt == 0:
                    return True
                else:
                    return False

            elif i ==3:
                #카테고리 입력 검사
                #1.야채, 2.과일, 3.유제품, 4.냉동식품, 5.육류, 6.어류, 7.과자, 8.음료, 9.주류, 10.빙과류, 11.신선제품, 12.소스, 13.곡식류, 14.가루류, 15.기타
                if update_data.isdigit() == False:
                    #숫자가 아닌 경우
                    if update_data.find(' ') < 0:
                        print("잘못된 수정 정보입니다. 숫자로 입력해주세요.")

                    cnt += 1

                if update_data.find(' ')>=0:
                    #공백류가 포함된 경우
                    print("잘못된 수정 정보입니다. 공백류를 포함할 수 없습니다.")
                    cnt += 1
                
                if update_data.find('0') == 0:
                    print("잘못된 수정 정보입니다. 선행0을 포함하지 않아야 합니다.")
                    cnt += 1

                if cnt == 0 : 
                    if 1 > int(update_data) or int(update_data) > 15:
                        #입력 범위에 벗어난 경우
                        print("잘못된 수정 정보입니다. 1부터 15이하의 정수로 입력해주세요.")
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

                if num.isdigit() == False:
                    #숫자가 아닌 경우
                    if update_data.find(' ') < 0:
                        print("잘못된 수정 정보입니다. 숫자로 입력해주세요.")

                    cnt += 1

                if num.find(' ')>=0:
                    #공백류가 포함된 경우
                    print("잘못된 수정 정보입니다. 공백류를 포함할 수 없습니다.")
                    cnt += 1
                
                if num.find('0') == 0:
                    print("잘못된 수정 정보입니다. 선행0을 포함하지 않아야 합니다.")
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
                        print("잘못된 수정 정보입니다. 오늘 날짜 이후로 입력해주세요.")
                        return False
                    else :
                        return True
                else: 
                    print("잘못된 수정 정보입니다. 날짜 입력규칙에 맞지 않습니다.")
                    return False

def update_product():
    cate_pass = 0
    global global_user_id
    global global_icebox

    while True:
        print()
        if cate_pass == 0:
            update_cate = input("수정할 항목을 입력해주세요 :")
            update_cate = update_cate.lstrip()
            update_cate = update_cate.rstrip()
            if len(update_cate) == 0: #여기서는 탭은 안걸림
                    print("입력한 값이 없습니다.")
                    continue
            if update_cate == '카테고리':
                print("1.야채, 2.과일, 3.유제품, 4.냉동식품, 5.육류, 6.어류, 7.과자, 8.음료, 9.주류, 10.빙과류, 11.신선제품, 12.소스, 13.곡식류, 14.가루류, 15.기타")

        if validate_cate(update_cate):
            cate_pass += 1
            update_data = input("수정 정보를 입력해주세요 :")


            if validate_data(update_cate, update_data):
                #올바른 수정 항목과 수정 정보가 입력된 경우
                with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
                    json_data = json.load(file)


                icebox_select = json_data['iceboxes'][0] #일단 0번째 냉장고로 초기화

                for icebox in json_data['iceboxes'] :
                    if str(global_user_id) == icebox['id']: 
                        icebox_select = icebox
                        break

                items = icebox_select["items"]
                packaged_itemlist = items["packaged"]
                unpackaged_itemlist = items["unpackaged"]

                for i,item in enumerate(packaged_itemlist):
                    if  int(global_product_id) == item["ID"]:
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
                    if  int(global_product_id) == item["ID"]:
                        if update_cate == '카테고리':
                            update_data = category_list[update_data]
                        elif update_cate in ['현재량','보관권장온도','총량']:
                             update_data = int(update_data)
                        item[unpackaged_updatable_cate[update_cate]] = update_data
                        with open('./data/IceBox_data.json', 'w', encoding='utf-8') as make_file:

                            json.dump(json_data, make_file, indent="\t", ensure_ascii=False)
                view_item_data(global_product_id)
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
                continue
        else:
            #잘못된 수정 항목이나 수정 정보가 입력된 경우
            print("잘못된 수정 항목 값입니다.")
            continue
        
#처음 호출되는 함수
def product_update(user_id_in):
    global global_user_id 
    global_user_id = user_id_in
    search_by_id()






