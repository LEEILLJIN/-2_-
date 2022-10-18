# 상품 조회 화면

import json

file_path = "./data/IceBox_data.json"

def sort_display(direction,reverse):
    if direction=="up":
        if reverse==False:
            return "오름차순"
        else:
            return "내림차순"
    if direction=="down":
        if reverse==False:
            return "내림차순"
        else:
            return "오름차순"


def load_json ():
    with open(file_path, 'r', encoding="utf-8") as f:
        return json.load(f)

def show_item(item):
    # print('bulk-for-unit' in item)
    if 'bulk-for-unit' in item:
        #unpackaged
        print("<상품 ID: {}, 상품명: {}, 총량: {}, 단위 수량: {}, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-number"], item["bulk-for-unit"],item["leftover-number"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
    else:
        #packaged
        print("<상품 ID: {}, 상품명: {}, 총량: {}, 현재량: {}, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-number"], item["leftover-number"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))  
        
def dic_key_change(dic,prevKey,nextkey) :
    new_items=[]
    for item in dic:
        newDic={}
        values=list(item.values())
        for idx,key in enumerate(list(item.keys())):
            if key==prevKey:
                newDic[nextkey]=values[idx]
            else:
                newDic[key]=values[idx]
        new_items.append(newDic)
    return new_items
    

def show_items(sort_filter) :        
    data=load_json()
    unpackedged_itmes=data["iceboxes"][0]["items"]["unpackaged"]
    #normalize
    normarlized_packaged_items = dic_key_change(data["iceboxes"][0]["items"]["packaged"],"total-bulk","total-number")
    normarlized_packaged_items = dic_key_change(normarlized_packaged_items,"leftover","leftover-number")
    items=unpackedged_itmes+normarlized_packaged_items

    #filter
    items=sorted(items, key=lambda item: item[sort_filter[0]] ,reverse=(( not sort_filter[1]) if sort_filter[2]==True else  sort_filter[1]))
    print("==========================================")
    print(sort_filter[3]+" "+sort_display(sort_filter[4],sort_filter[2]))
    # ( "역순" if  sort_filter[2]==True else "")
    print("----냉동----")
    for item in list(filter((lambda x: x["partition"]=="냉동"),items)):
        show_item(item)
    print("----냉장----")
    for item in list(filter((lambda x: x["partition"]=="냉장"),items)):
        show_item(item)
    
                     
            

def product_show():
    #unpackeged defaultReverseFlag defaultReverseFlagOfreverse Display defaultSortDisplay
    sort_filter=["expiration-date",True,False,"유통기한 기준","up"]
    while True:
        show_items(sort_filter)
        print("==========================================")
        print("(0) 돌아가기")
        print("(1) 유통기한 기준 조회")
        print("(2) 상품명 사전식 조회")
        print("(3) 총량 기준 조회")
        print("(4) 현재량 기준 조회")
        print("(5) 보관권장온도 기준 조회")
        print("(6) 역순 조회")
        user_input = input("선택 항목 입력:")
        
        if user_input == '0' :
            break; 
        elif user_input == '1' :
            sort_filter=["expiration-date",True,False,"유통기한 기준","up"]
        elif user_input == '2' :
            sort_filter=["name",False,False,"상품명 사전식","up"]
        elif user_input == '3' :
            sort_filter=["total-number",True,False,"총량 기준","down"]
        elif user_input == '4' :
            sort_filter=["leftover-number",True,False,"현재량 기준","down"]
        elif user_input == '5' :
            sort_filter=["recommended-temp",False,False,"보관권장온도 기준","up"]
        elif user_input == '6' :
            sort_filter[2]= False if sort_filter[2]==True else True
        else :
            print("==========================================")
            print("선택지 내에서 선택해주세요.")
    
# print(dic_key_change([{"test":1,"test2":2}],"test2","nextkey"))

# product_show()
