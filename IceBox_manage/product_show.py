# 상품 조회 화면

import json
import IceBox_menu
file_path = "./data/IceBox_data.json"

def main_screen2(UserID) :
    with open(file_path, "r", encoding='UTF8') as file :
          
            data = json.load(file)
            today = data['today']
            IceBox_menu.MainMenu(today,UserID)


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
        
        print("<상품 ID: {}, 상품명: {}, 총량: {}개, 단위 수량: {}개, 현재량: {}개, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-number"]*item["bulk-for-unit"], item["bulk-for-unit"],item["leftover-number"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))
    else:
        #packaged
        print("<상품 ID: {}, 상품명: {}, 총량: {}L, 현재량: {}L, 카테고리: {}, 분류: {}, 보관권장온도: {}, 유통기한: {}>" .format(item["ID"], item["name"], item["total-bulk"], item["leftover-bulk"], item["category"], item["partition"], item["recommended-temp"], item["expiration-date"]))  
        
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
    

def show_items(sort_filter,UserID) :        
    def isMatch(iceBox):
        if iceBox["id"]==UserID :
            return True
        else :
            return False

    loaded_json = load_json()
    selectedIceBox=list(filter(isMatch,loaded_json["iceboxes"]))[0]
    unpackedged_itmes=selectedIceBox["items"]["unpackaged"]
    normarlized_packaged_items = selectedIceBox["items"]["packaged"]
    items=unpackedged_itmes+normarlized_packaged_items
    #items

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
    
                     
            

def product_show(UserID):
    #unpackeged defaultReverseFlag defaultReverseFlagOfreverse Display defaultSortDisplay
    sort_filter=["expiration-date",False,False,"유통기한 기준","up"]
    while True:
        show_items(sort_filter,UserID)
        print("==========================================")
        print("0. 돌아가기")
        print("1. 유통기한 기준 조회")
        print("2. 카테고리 기준 조회")
        print("3. 역순 조회")
        # print("(3) 상품명 사전식 조회")
        # print("(4) 총량 기준 조회")
        # print("(5) 현재량 기준 조회")
        # print("(6) 보관권장온도 기준 조회")
        # print("(7) 역순 조회")
        user_input = input("조회할 기준을 선택해주세요.:")
        
        if user_input == '0' :
            main_screen2(UserID)
            break; 
        elif user_input == '1' :
            sort_filter=["expiration-date",False,False,"유통기한 기준","up"]
        elif user_input == '2' :
            sort_filter=["category",False,False,"카테고리 기준","up"]
        # elif user_input == '3' :
        #     sort_filter=["name",False,False,"상품명 사전식","up"]
        # elif user_input == '4' :
        #     sort_filter=["total-number",True,False,"총량 기준","down"]
        # elif user_input == '5' :
        #     sort_filter=["leftover-number",True,False,"현재량 기준","down"]
        # elif user_input == '6' :
        #     sort_filter=["recommended-temp",False,False,"보관권장온도 기준","up"]
        elif user_input == '3' :
            sort_filter[2]= False if sort_filter[2]==True else True
        else :
            print("==========================================")
            print("선택지 내에서 선택해주세요.")
    
# print(dic_key_change([{"test":1,"test2":2}],"test2","nextkey"))

# product_show()
