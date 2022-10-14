# 상품 검색 화면
import json

path = "./data/IceBox_data.json"
def search_by_name() :
        special_character = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        cnt = 0
        while True : 
            print()
            product_name = input("검색할 상품명 : ")
            for validation in product_name :
                if validation in special_character :
                    print("특수문자를 사용할 수 없습니다")
                    break
            
            else :
                with open(path, "r", encoding='UTF8') as file :
            
                    data = json.load(file)
                    items = data['items']
                    packaged = items['packaged']
                    
                    print("분류\t\t상품명\t\t카테고리\t상품ID\t\t용량\t\t잔량\t\t온도\t\t유효기간")
                    for item in items["packaged"] :
                        if(product_name == item['name']) :
                            for value in item.values() :
                                print(value, end='\t\t')
                                cnt+=1
                            print()
                        else :
                            continue
                    
                    if cnt == 0 :
                        print("저장된 상품이 없습니다. 다시 입력해주세요.")
                    plus_search = input("추가 검색을 하시겠습니까 ? y/n : ")
                    additional_search(plus_search)
            cnt=0    
            
            
def additional_search(request) :
                
    if request == 'y' :
        search_by_name()
        
    elif request == 'n' :
        print("초기 화면 함수 대기")
        exit()
    else :
        print("y 또는 n을 입력해주세요.")
        plus_search = input("추가 검색을 하시겠습니까 ? y/n : ")
        additional_search(plus_search)

if __name__=="__main__":
    while True:
        print("0. 돌아가기")
        print("1. 상품명 검색")
        user_input = int(input())
        
        if user_input == 0 :
            print("함수 대기") # 관리화면 함수 기다리는중
        elif user_input == 1 :
            search_by_name()

    

    

# 상품 검색 목록 나열할 때 양식 수정
# 상품명 문법 형식에 특수문자 제외 추가
# 상품명 동치 비교 예를 들어 ~~ 없애기