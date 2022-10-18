#냉장고 수정 화면

import json
import os
import IceBox_menu

# 현재 냉장고는 하나 밖에 없으므로, iceboxes 배열의 0번째 정보를 바로 넣었습니다.
icebox_num = 0 # 냉장고가 여러 개가 되면, 바꿔줘야 한다.
def icebox_updater():
    # 현재 정보 출력
    def current_info_printer(current_icebox):
        print("현재 냉장고: \n")
        print(f'냉장 - 크기 {current_icebox["refrigerator-size"]}L, 온도 {current_icebox["refrigerator-temp"]}°C')
        print(f'냉동 - 크기 {current_icebox["freezer-size"]}L, 온도 {current_icebox["freezer-temp"]}°C\n')

    # 냉장고 크기 수정 함수
    def refrigerator_size_handler(current_icebox):
        current_size = current_icebox["refrigerator-size"] 
        print("수정할 냉장고 설정:\n")
        print(f'냉장 크기 – 현재: {current_size}L\n')
        while(True):
            # 정수 확인
            try:
                size = int(input("정수를 입력해주세요 >> ").strip())
                current_icebox["refrigerator-size"] = size
                return
            except ValueError:
                print("올바른 입력값이 아닙니다.\n")

    # 냉장고 온도 수정 함수
    def refrigerator_temp_handler(current_icebox):
        current_temp = current_icebox["refrigerator-temp"] 
        print("수정할 냉장고 설정:\n")
        print(f'냉장 온도 – 현재: {current_temp}°C\n')
        while(True):
            # 정수 확인
            try:
                temp = int(input("정수를 입력해주세요 >> ").strip())
                current_icebox["refrigerator-temp"] = temp
                return
            except ValueError:
                print("올바른 입력값이 아닙니다.\n")

    # 냉동고 크기 수정 함수
    def freezer_size_handler(current_icebox):
        current_size = current_icebox["freezer-size"] 
        print("수정할 냉동고 설정:\n")
        print(f'냉동 크기 – 현재: {current_size}L\n')
        while(True):
            # 정수 확인
            try:
                size = int(input("정수를 입력해주세요 >> ").strip())
                current_icebox["freezer-size"] = size
                return
            except ValueError:
                print("올바른 입력값이 아닙니다.\n")

    # 냉동고 온도 수정 함수
    def freezer_temp_handler(current_icebox):
        current_temp = current_icebox["freezer-temp"] 
        print("수정할 냉동고 설정:\n")
        print(f'냉동 온도 – 현재: {current_temp}°C\n')
        while(True):
            # 정수 확인
            try:
                temp = int(input("정수를 입력해주세요 >> ").strip())
                current_icebox["freezer-temp"] = temp
                return
            except ValueError:
                print("올바른 입력값이 아닙니다.\n")

    handlers = {'1': refrigerator_size_handler, '2': refrigerator_temp_handler, '3': freezer_size_handler, '4': freezer_temp_handler}

    # json 파일 열기
    file_path = './data/IceBox_data.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 현재 냉장고가 있는 경우
        if data['iceboxes']: 
            current_icebox = data['iceboxes'][icebox_num] # 현재 냉장고의 정보만 가져오기
            # 현재 냉장고 정보 및 삭제 경고 메시지 출력
            current_info_printer(current_icebox)
            print("어떤 설정 정보를 수정하시겠습니까?")
            # 냉장고 삭제 확인
            while(True):
                # 메뉴 출력 및 입력 받기
                print("0. 돌아가기")
                print("1. 냉장 크기")
                print("2. 냉장 온도")
                print("3. 냉동 크기")
                print("4. 냉동 온도")
                menu = input("0이상 4이하의 숫자로 입력해주세요. ").strip()

                if menu == '0':
                    # 메인 메뉴로 돌아가기
                    IceBox_menu.MainMenu(data["today"])
                    return
                elif menu == '1' or menu == '2' or menu == '3'  or menu == '4' :
                    # 정보 수정 handler 호출
                    info_updater = handlers[menu]
                    info_updater(current_icebox)
                    
                    # 수정 정보 저장
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print("해당 냉장고 설정 정보를 변경되었습니다.\n")

                    # 수정이 반영된 현재 상태 출력
                    current_info_printer(current_icebox)
                    print("또 다른 설정을 수정하시겠습니까?")
                else:
                    print("올바른 입력값이 아닙니다.\n")
        else:
            print("삭제할 냉장고가 없습니다 ")
            IceBox_menu.MainMenu(data["today"])
            return
    else:
        print("냉장고 정보 파일이 존재하지 않습니다.")
        IceBox_menu.MainMenu(data["today"])
        return
