# 상품 수정 화면
#냉장고 관리 화면에서 사용자가 ‘5’를 입력하면 나오는 화면입니다.
from itertools import product
import json
from unicodedata import category
# import IceBox
path = "./data/IceBox_data.json"
packaged_updatable_cate = {"파티션": "partition",'상품명': 'name', '총량':'total-bulk', '현재량':'leftover', '카테고리':'category', '보관권장온도':'recommended-temp', '유통기한':'expiration-date'}
unpackaged_updatable_cate = {"파티션": "partition",'상품명': 'name', '총량' : 'total-number', '현재량' : 'leftover-number', "개당 부피": "bulk-for-unit",'카테고리':'category', '보관권장온도':'recommended-temp', '유통기한':'expiration-date'}
special_character = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
category_data_type={
    'name': "string",
    'total-bulk': "int",
    'leftover': "int",
    'total-number': "int",
    'leftover-number': "int",
    'category': "select",
    'recommended-temp': "int",
    'expiration-date': "string"
}
category_object = {
    '1' : '야채', '2':'과일', '3':'유제품', '4':'냉동식품', '5':'육류', '6':'어류', '7':'과자', '8':'음료', '9':'주류', '10':'빙과류', '11':'신선제품', '12':'소스', '13':'곡식류', '14':'가루류', '15':'기타'
}

partition_object = {
    '1': "냉장",
    '2': "냉동"
}

file_path = './data/IceBox_data.json'

def load_json ():
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json (current_json):
    with open(file_path, 'w') as f:
        json.dump(current_json, f, ensure_ascii=False, indent=2)

def save_product (is_packaged,input_data):
    loaded_json = load_json()
    input_data["ID"]=loaded_json["current_item_sequence"]
    loaded_json["current_item_sequence"]+=1
    if is_packaged:
        loaded_json["items"]["packaged"].append(input_data)
    else:
        loaded_json["items"]["unpackaged"].append(input_data)
    save_json(loaded_json)




def set_input_process_tmp_data(input_data,key,input_process_tmp_data,exit_object):
    if(input_data=="0"):
        exit_object["is_exit"]=True
        return False
    if validate_input_data(input_data,key,input_process_tmp_data) == True:
        save_data(input_data,key,input_process_tmp_data)
        return True
    else :
        return False

def validate_int (input_data):
    try:
        if input_data.isdigit()==True:
            return True
        else:
            return False
    except:
        return False


def save_data(input_data,key,input_process_tmp_data) :
    parsed_input_data=input_data

    if key == 'bulk-for-unit':
        parsed_input_data = int(input_data)

    if key == 'partition':
        parsed_input_data = partition_object[input_data]

    if key == 'product-type':
        parsed_input_data = input_data

    if key == 'name':
        parsed_input_data = input_data

    elif key == 'total-bulk':
        parsed_input_data = int(input_data)

    elif key == 'leftover':
        parsed_input_data = int(input_data)

    elif key == 'total-number':
        parsed_input_data = int(input_data)

    elif key == 'leftover-number':
        parsed_input_data = int(input_data)

    elif key == 'category':
        parsed_input_data = category_object[input_data]

    elif key == 'recommended-temp':
        parsed_input_data = int(input_data)

    elif key == 'expiration-date':
        parsed_input_data = input_data
        #date check
    input_process_tmp_data[key]=parsed_input_data

def validate_input_data(input_data,key,input_process_tmp_data) :


    if key == 'product-type':
        if(validate_int(input_data)==False):
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        if (int(input_data) >= 0) & (int(input_data)<=2):
            return True
        else:
            print("카테고리 범주 내에서 선택해주세요.")
            print("다시 입력해주세요.")
            return False


    if key == 'name':
        return True

    elif key == 'total-bulk':
        if(validate_int(input_data)==False):
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        if (int(input_data) >= 0):
            return True
        else:
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False


    elif key == 'leftover':
        if(validate_int(input_data)==False):
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        if input_process_tmp_data["total-bulk"]<int(input_data):
            print("총량보다 작은 값만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        else :
            if int(input_data) >= 0:
                return True
            else:
                print("자연수만 입력 가능합니다.")
                print("다시 입력해주세요.")
                return False


    elif key == 'total-number':
        if(validate_int(input_data)==False):
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False

        if int(input_data) >= 0:
            return True
        else:
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False

    elif key == 'leftover-number':
        if(validate_int(input_data)==False):
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        if input_process_tmp_data["total-number"]<int(input_data):
            print("총량보다 작은 값만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        else :
            if int(input_data) >= 0:
                return True
            else:
                print("자연수만 입력 가능합니다.")
                print("다시 입력해주세요.")
                return False

    elif key == 'bulk-for-unit':
            if(validate_int(input_data)==False):
                print("자연수만 입력 가능합니다.")
                print("다시 입력해주세요.")
                return False
            if int(input_data) >= 0:
                return True
            else:
                print("자연수만 입력 가능합니다.")
                print("다시 입력해주세요.")
                return False

    elif key == 'partition':
        if(validate_int(input_data)==False):
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False

        if (int(input_data) >= 0) & (int(input_data) <= 2):
            return True
        else:
            print("카테고리 범주 내에서 선택해주세요.")
            print("다시 입력해주세요.")
            return False


    elif key == 'category':
        if(validate_int(input_data)==False):
            print("자연수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        if int(input_data)<=len(list(category_object.keys())):
            return True
        else:
            print("카테고리 범주 내에서 선택해주세요.")
            print("다시 입력해주세요.")
            return False


    elif key == 'recommended-temp':
        if(validate_int(input_data)==False):
            print("정수만 입력 가능합니다.")
            print("다시 입력해주세요.")
            return False
        return True

    elif key == 'expiration-date':
        return True
        #date check
        #미개발
    return False


def register_product():
    #수정할 상품 ID 입력하여 해당 ID의 예외 처리 후 적법할 경우 상품을 찾는 함수
    exit_object={
        "is_exit": False
    }
    while exit_object["is_exit"]==False:
        print("(1) 보관함으로 저장")
        print("(2) 개별 저장")
        product_register_type =  input("상품의 저장 환경을 선택하세요: ")

        #입력값 검증
        if set_input_process_tmp_data(product_register_type,"product-type",{},exit_object) == False :
            continue

        if(exit_object["is_exit"]==True):
            break

        #입력 단계 counter
        process_step=0
        #입력할 데이터 Form 선택
        input_process_category = packaged_updatable_cate if product_register_type == "1" else unpackaged_updatable_cate

        #입력 단계 수
        max_process_step=len(list(input_process_category.keys()))-1
        #입력할 데이터 display string list
        input_process_category_display_list = list(input_process_category.keys())
        #입력할 데이터 key string list
        input_process_category_key_list = list(input_process_category.values())
        #저장할 데이터
        input_process_tmp_data = {input_process_category_key_list[i]: None for i in range(0, len(input_process_category_key_list))}
        #페키지 언페키지
        is_input_process_tmp_data_packaged= True if product_register_type == "1" else False


        #상품 데이터 입력 cycle
        while exit_object["is_exit"]==False & process_step<max_process_step:

            print(" ")
            print("==========================================")
            print(" ")

            if len(input_process_category_display_list)<=process_step:
                break

            if input_process_category_display_list[process_step]=="카테고리":
                for idx,i in enumerate(list(category_object.values())):
                    print(f"({idx+1}) {i}")
            if input_process_category_display_list[process_step]=="파티션":
                for idx,i in enumerate(list(partition_object.values())):
                    print(f"({idx+1}) {i}")
            input_data =  input(f"{input_process_category_display_list[process_step]} 입력:")
            # print(input_data)

            #입력값 검증
            if set_input_process_tmp_data(input_data,input_process_category_key_list[process_step],input_process_tmp_data,exit_object) == False :
                if exit_object["is_exit"]==True:
                    break
                else:
                    continue
            else :
                process_step+=1

            if(exit_object["is_exit"]==True):
                break

        if(exit_object["is_exit"]==False):
            save_product(is_input_process_tmp_data_packaged,input_process_tmp_data)




# register_product()
