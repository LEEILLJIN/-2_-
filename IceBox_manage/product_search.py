# 상품 검색 화면
import json
import os
import sys
import platform

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import IceBox_menu

path = "./data/IceBox_data.json"
global global_id

def search_by_name(global_id) :

        special_character = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        cnt = 0
        while True :
            print()
            product_name = input("검색할 상품명 : ")
            print()
            for validation in product_name :
                if validation in special_character :
                    print("상품명은 한글,영어, 숫자만 입력 가능합니다.")
                    break
            
            else :
                with open(path, "r", encoding='UTF8') as file :
            
                    data = json.load(file)
                    iceboxes = data['iceboxes'][int(global_id)-1]

                    items = iceboxes['items']
                    
                    
                    for item in items['packaged'] :
                        if(product_name == item['name'] ) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}L, 현재량: {}L, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-bulk"], item["leftover-bulk"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1
                        else :
                            continue
                        
                    for item in items['unpackaged'] :
                        if(product_name == item['name']) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}개, 단위 수량: {}개, 현재량: {}개, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-number"], item["bulk-for-unit"],item["leftover-number"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1
                        else :
                            continue
                    
                    if cnt == 0 :
                        print("저장된 상품이 없습니다.")
                    print()
                    plus_search = input("추가 검색을 하시겠습니까? (Y/N) : ")
                    additional_search(plus_search)
            cnt=0
            
            
def additional_search(request) :

    if request == 'Y' :
        search_by_name(global_id)
        
    elif request == 'N' :
        main_screen2()
    else :
        print("Y 또는 N을 입력해주세요.")
        plus_search = input("추가 검색을 하시겠습니까? (Y/N) : ")
        additional_search(plus_search)


def main_screen2() :
    with open(path, "r", encoding='UTF8') as file :

            data = json.load(file)
            iceboxes = data['iceboxes'][int(global_id)-1]
            today = data['today']
        
            IceBox_menu.MainMenu(today, global_id)

def product_search(UserId):
    global global_id
    global_id = UserId

    while True:
        print("0. 돌아가기")
        print("1. 상품명 검색")
        user_input = input()
        
        if user_input == '0' :
            main_screen2()
            break
        elif user_input == '1' :
            search_by_name(global_id)
        else :
            print()
            print("0, 1 이외의 값은 입력할 수 없습니다.")