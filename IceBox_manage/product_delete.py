# 상품 삭제 화면

# 상품 검색 화면
import json

path = "./data/IceBox_data.json"
def delete_by_id() :
        special_character = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        cnt = 0
        while True : 
            print()
            product_id = input("삭제할 상품 id : ")
            if product_id.isdigit() == False:
                if product_id.isalpha() :
                    print("한글이나, 영어를 사용할 수 없습니다.")
                    continue
                else:
                    for validation in product_id :
                        if validation in special_character :
                            print("특수문자를 사용할 수 없습니다.")
                            break
                
            
            else :
                with open(path, "r", encoding='UTF8') as file :
            
                    data = json.load(file)
                    items = data['items']
                    
                    for i, item in enumerate(items["packaged"]) :
                        if(int(product_id) == item['ID']) :
                            del items["packaged"][i]
                            cnt += 1
                            with open(path, 'w', encoding='UTF8') as delete_file :
                                json.dump(data, delete_file, indent="\t", ensure_ascii=False)
                            print()
                        else :
                            continue
                    
                    for i, item in enumerate(items["unpackaged"]) :
                        if(int(product_id) == item['ID']) :
                            del items["unpackaged"][i]
                            cnt += 1
                            with open(path, 'w', encoding='UTF8') as delete_file :
                                json.dump(data, delete_file, indent="\t", ensure_ascii=False)
                            print()
                        else :
                            continue
                    
                    if cnt == 0 :
                        print("존재하지 않는 상품 아이디입니다.")
                        continue
                    plus_delete = input("다른 아이디로 삭제하시겠습니까 ? y/n : ")
                    additional_delete(plus_delete)
            cnt=0    
            
            
def additional_delete(request) :


                
    if request == 'y' :
        delete_by_id()
        
    elif request == 'n' :
        print("초기 화면 함수 대기")
        exit()
    else :
        print("y 또는 n을 입력해주세요.")
        plus_delete = input("다른 아이디로 삭제하시겠습니까 ? y/n : ")
        additional_delete(plus_delete)

def consume_by_id() :
    print("asdf")

def all_delete() :
    print("adsf")

def consume_by_id() :
    print("adsf")

if __name__=="__main__":
    while True:
        print("0. 돌아가기")
        print("1. 상품 폐기")
        print("2. 상품 소모")
        user_input = input()
        
        if user_input == '0' :
            print("함수 대기") # 관리화면 함수 기다리는중
            break
        elif user_input == '1' :
            print()
            print("0. 돌아가기")
            print("1. 상품 ID로 삭제")
            print("2. 유통기한 지난 물품 전체 삭제")
            user_input = input()
            if user_input == '0' :
                print("함수 대기") # 돌아가기
                break
            elif user_input == '1' :
                delete_by_id()
            elif user_input == '2' :
                all_delete()

        elif user_input == '2' :
            consume_id = input("소모할 상품 ID : ")
            consume_how = input("소모할 상품 양 : ")

            consume_by_id()



    

    

# 상품 검색 목록 나열할 때 양식 수정
# 상품명 문법 형식에 특수문자 제외 추가
# 상품명 동치 비교 예를 들어 ~~ 없애기