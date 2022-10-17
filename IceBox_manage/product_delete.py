# 상품 삭제 화면

# 상품 검색 화면
import datetime
import json

path = "./data/IceBox_data.json"
# 상품 id로 상품 폐기
def delete_by_id() :
        # special_character = ['~','!','@','#','$','%','^','&','*','(', ')',"'", '-','+','<','>','?']
        cnt = 0
        while True : 
            print()
            product_id = input("폐기할 상품 ID : ")
            if product_id.isdigit() == False:
                print("상품 ID는 숫자만 입력 가능합니다.")
                # if product_id.isalpha() :
                #     print("한글이나, 영어를 사용할 수 없습니다.")
                #     continue
                # else:
                #     for validation in product_id :
                #         if validation in special_character :
                #             print("특수문자를 사용할 수 없습니다.")
                #             break
                
            
            elif product_id.isdigit() == True :
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
                            print("ID '{}'에 해당하는 {} 제품이 폐기되었습니다." .format(int(item["ID"]), item["name"] ))
                        else :
                            continue
                    
                    for i, item in enumerate(items["unpackaged"]) :
                        if(int(product_id) == item['ID']) :
                            del items["unpackaged"][i]
                            cnt += 1
                            with open(path, 'w', encoding='UTF8') as delete_file :
                                json.dump(data, delete_file, indent="\t", ensure_ascii=False)
                            print()
                            print("ID '{}'에 해당하는 {} 제품이 폐기되었습니다." .format(int(item["ID"]), item["name"] ))
                        else :
                            continue
                    
                    if cnt == 0 :
                        print("존재하지 않는 상품 아이디입니다.")
                        continue
                    
                    plus_delete = input("다른 아이디로 삭제하시겠습니까 ? y/n : ")
                    additional_delete(plus_delete)
            cnt=0

# 상품 id로 상품 소모
def consume_by_id() :
    cnt = 0
    while True :
        with open(path, "r", encoding='UTF8') as file :
                
            data = json.load(file)
            items = data['items']
            consume_id = input("소모할 상품 ID : ")
            consume_how = input("소모할 상품 양 : ")
                        
            for item in items["packaged"] :
                if int(consume_id) == item['ID'] :
                    if item['leftover'] < int(consume_how) :
                        cnt+=1
                        print("남은 양이 부족합니다.")
                        print("ID '{}'에 해당하는 제품 '{}'의 남은 양은 '{}'입니다." .format(item['ID'], item['name'], item['leftover']))

                        print()
                        continue
                    else :
                        item['leftover']-=int(consume_how)
                        cnt += 1
                        with open(path, 'w', encoding='UTF8') as consume_file :
                            json.dump(data, consume_file, indent="\t", ensure_ascii=False)
                        print("ID '{}'에 해당하는 제품 '{}'을(를) 소모하고 남은 양은 '{}'입니다." .format(item['ID'], item['name'], item['leftover']))
                        print()
            
            for item in items["unpackaged"] :
                if int(consume_id) == item['ID'] :
                    if item['leftover-number'] < int(consume_how) :
                        cnt+=1
                        print("남은 양이 부족합니다.")
                        print("ID '{}'에 해당하는 제품 '{}'의 남은 양은 '{}'입니다." .format(item['ID'], item['name'], item['leftover-number']))
                        print()
                        continue
                    else :
                        item['leftover-number']-=int(consume_how)
                        cnt += 1
                        with open(path, 'w', encoding='UTF8') as consume_file :
                            json.dump(data, consume_file, indent="\t", ensure_ascii=False)
                        print("ID '{}'에 해당하는 제품 '{}'을(를) 소모하고 남은 양은 '{}'입니다." .format(item['ID'], item['name'], item['leftover-number']))
                        print()
            
                        
        if cnt == 0:
            print("일치하는 상품 ID가 없습니다.")
            print()
            break
            
        
            
# 유통기한 지난 물품 전체 삭제
def all_delete() :
    
    print("유통기한 지난 물품 전체 삭제")
    delete_all = input("삭제하시겠습니까? (y/n) : ")

    if delete_all == 'y' :
        with open(path, "r", encoding='UTF8') as file :
            
            data = json.load(file)
            items = data['items']
            today = int("".join(str(datetime.date.today()).split("-")))

            for item in items["packaged"].copy() :
                expiration = int("".join(item['expiration-date'].split("-")))
                
                if today > expiration :
                    del items['packaged'][items['packaged'].index(item)]
                with open(path, 'w', encoding='UTF8') as delete_all :
                    json.dump(data, delete_all, indent="\t", ensure_ascii=False)


            for item in items["unpackaged"].copy() :
                expiration = int("".join(item['expiration-date'].split("-")))
                
                if today > expiration :
                    del items['unpackaged'][items['unpackaged'].index(item)]
                with open(path, 'w', encoding='UTF8') as delete_all :
                    json.dump(data, delete_all, indent="\t", ensure_ascii=False)
            
        
        print("유통기한 지난 상품이 전체 폐기 되었습니다.")
        print()
                

    elif delete_all == 'n' :
        print("초기 화면 함수 대기")
        exit()
    else :
        print("y 또는 n을 입력해주세요.")
        print()
        all_delete()


# 추가 삭제
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

                        
if __name__=="__main__":
    while True:
        print("0. 돌아가기")
        print("1. 상품 폐기")
        print("2. 상품 소모")
        user_input = input()
        
        if user_input == '0' :
            print("함수 대기") # 돌아가기
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
            elif user_input.isdigit() == False :
                print()
                print("숫자만 입력 해주세요.")
                continue

            else :
                print()
                print("0, 1, 2 중에서 메뉴를 골라주세요.")
                continue

        elif user_input == '2' :
            consume_by_id()
        
        elif user_input.isdigit() == False :
            print()
            print("숫자만 입력 해주세요.")
            continue

        else :
            print()
            print("0, 1, 2 중에서 메뉴를 골라주세요.")
            continue




    

    

# 상품 검색 목록 나열할 때 양식 수정
# 상품명 문법 형식에 특수문자 제외 추가
# 상품명 동치 비교 예를 들어 ~~ 없애기