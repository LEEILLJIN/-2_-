# 상품 검색 화면
import json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import product_delete

path = "./data/IceBox_data.json"
def search_by_name() :
        special_character = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        cnt = 0
        while True : 
            print()
            product_name = input("검색할 상품명 : ")
            print()
            for validation in product_name :
                if validation in special_character :
                    print("특수문자를 사용할 수 없습니다")
                    break
            
            else :
                with open(path, "r", encoding='UTF8') as file :
            
                    data = json.load(file)
                    iceboxes = data['iceboxes']
                    items = iceboxes[0]['items']
                    
                    for item in items['packaged'] :
                        if(product_name == item['name']) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-bulk"], item["leftover"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1
                        else :
                            continue
                        
                    for item in items['unpackaged'] :
                        if(product_name == item['name']) :
                            print("<상품 ID: {}, 상품명: {}, 총량: {}, 단위 수량: {}, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-number"], item["bulk-for-unit"],item["leftover-number"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
                            cnt+=1
                        else :
                            continue
                    
                    if cnt == 0 :
                        print("저장된 상품이 없습니다.")
                    print()
                    plus_search = input("추가 검색을 하시겠습니까 ? y/n : ")
                    additional_search(plus_search)
            cnt=0    
            
            
def additional_search(request) :
                
    if request == 'y' :
        search_by_name()
        
    elif request == 'n' :
        product_delete.main_screen()
    else :
        print("y 또는 n을 입력해주세요.")
        plus_search = input("추가 검색을 하시겠습니까 ? y/n : ")
        additional_search(plus_search)

if __name__=="__main__":
    while True:
        print("0. 돌아가기")
        print("1. 상품명 검색")
        user_input = input()
        
        if user_input == '0' :
            product_delete.main_screen()
            break
        elif user_input == '1' :
            search_by_name()
        else :
            print()
            print("0 또는 1을 입력해주세요")

