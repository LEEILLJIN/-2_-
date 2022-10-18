# 상품 조회 화면

import json

file_path = "./data/IceBox_data.json"

def load_json ():
    with open(file_path, 'r') as f:
        return json.load(f)

def show_item(item):
    # print('bulk-for-unit' in item)
    if 'bulk-for-unit' in item:
        #unpackaged
        print("<상품 ID: {}, 상품명: {}, 총량: {}, 단위 수량: {}, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-number"], item["bulk-for-unit"],item["leftover-number"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
    else:
        #packaged
        print("<상품 ID: {}, 상품명: {}, 총량: {}, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-bulk"], item["leftover"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))



def show_items() :
    data=load_json()
    items=data["iceboxes"][0]["items"]["unpackaged"]+data["iceboxes"][0]["items"]["packaged"]
    print("----냉동----")
    for item in list(filter((lambda x: x["partition"]=="냉동"),items)):
        show_item(item)
<<<<<<< HEAD
    print("----냉장----")
    for item in list(filter((lambda x: x["partition"]=="냉장"),items)):
        show_item(item)
    
                     
            
=======



>>>>>>> d21841d17085443993107f35155cab2d19c319ff

def product_show():
    while True:
        show_items()
        print(" ")
        print("==========================================")
        print(" ")
        print("0. 돌아가기")
        user_input = input("선택 항목을 입력해주세요.")

        if user_input == '0' :
            break;
        else :
            print(" ")
            print("==========================================")
            print(" ")
<<<<<<< HEAD
            print("선택지 내에서 선택해주세요.")
    
product_show()
=======
            print("카테고리 범주 내에서 선택해주세요.")

# product_show()
>>>>>>> d21841d17085443993107f35155cab2d19c319ff
