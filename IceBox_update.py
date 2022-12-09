#냉장고 수정 화면
import json
import os
import IceBox_menu
import time
import platform

def icebox_updater(UserID):
    # 냉장고 정보 배열 중 현재 냉장고 index
    icebox_num = int(UserID)-1

    # 현재 정보 출력
    def current_info_printer(current_icebox):
        print("현재 냉장고: \n")
        print(f'냉장 - 크기 {current_icebox["refrigerator-size"]["total"]}L, 온도 {current_icebox["refrigerator-temp"]}°C')
        print(f'냉동 - 크기 {current_icebox["freezer-size"]["total"]}L, 온도 {current_icebox["freezer-temp"]}°C\n')
    
    # 메뉴 출력
    def menu_printer():
        print("0. 돌아가기")
        print("1. 냉장 온도")
        print("2. 냉동 온도")
        print("3. 냉장고 비밀번호")

    # 냉장고 온도 수정 함수
    def refrigerator_temp_handler(current_icebox):
        current_temp = current_icebox["refrigerator-temp"] 
        print("수정할 냉장고 설정:\n")
        print(f'냉장 온도 – 현재: {current_temp}°C\n')
        while(True):
            temp_str = input("정수를 입력해주세요 >> ").strip()
            # 정수 확인
            try:
                temp = int(temp_str)
                if temp >= 0:
                # 숫자로만 이루어져 있어야 함. (+ 등 문자 포함 안됨)
                    if not temp_str.isdigit():
                        print("양의 정수 값은 기호를 포함하지 말고 입력해주세요.\n")
                        continue
                    # 선행 0이 있는 경우
                    if len(temp_str) >=2 and temp_str[0] == '0':
                        print("온도 값은 앞자리가 0으로 시작할 수 없습니다.\n")
                        continue
                else:
                    # 선행 0이 있는 경우 (-0 포함)
                    if temp_str.startswith('-') and temp_str[1] == '0':
                        print("온도 값은 앞자리가 0으로 시작할 수 없습니다.\n")
                        continue
                current_icebox["refrigerator-temp"] = temp
                return
            except ValueError:
                print("입력한 값이 정수가 아닙니다.\n")

    # 냉동고 온도 수정 함수
    def freezer_temp_handler(current_icebox):
        current_temp = current_icebox["freezer-temp"] 
        print("수정할 냉동고 설정:\n")
        print(f'냉동 온도 – 현재: {current_temp}°C\n')
        while(True):
            temp_str = input("정수를 입력해주세요 >> ").strip()
            # 정수 확인
            try:
                temp = int(temp_str)
                if temp >= 0:
                # 숫자로만 이루어져 있어야 함. (+ 등 문자 포함 안됨)
                    if not temp_str.isdigit():
                        print("양의 정수 값은 기호를 포함하지 말고 입력해주세요.\n")
                        continue
                    # 선행 0이 있는 경우
                    if len(temp_str) >=2 and temp_str[0] == '0':
                        print("온도 값은 앞자리가 0으로 시작할 수 없습니다.\n")
                        continue
                else:
                    # 선행 0이 있는 경우 (-0 포함)
                    if temp_str.startswith('-') and temp_str[1] == '0':
                        print("온도 값은 앞자리가 0으로 시작할 수 없습니다.\n")
                        continue
                current_icebox["freezer-temp"] = temp
                return
            except ValueError:
                print("입력한 값이 정수가 아닙니다.\n")

    # 냉장고 비밀번호 수정
    def password_reset(current_icebox):
        print("냉장고 비밀번호 수정:")
        while(True):
            password = input("6자리 숫자를 입력해주세요 >> ").strip()
            if not password.isdigit():
                print("숫자로만 입력해주세요.")
            elif len(password) != 6:
                print("비밀번호는 6자리 숫자여야 합니다. 다시 입력해주세요.")
            else:
                current_icebox["password"] = password
                return

    handlers = {'1': refrigerator_temp_handler, '2': freezer_temp_handler, '3': password_reset }

    def updater(current_icebox, menu):
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
        menu_printer()

    # json 파일 열기
    file_path = './data/IceBox_data.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 현재 냉장고가 있는 경우
        if data['iceboxes']: 
            current_icebox = data['iceboxes'][icebox_num] # 현재 냉장고의 정보만 가져오기
            # 현재 냉장고 정보 및 수정 안내 메시지 출력
            current_info_printer(current_icebox)
            print("어떤 설정 정보를 수정하시겠습니까?")
            menu_printer()

            while(True):
                # 메뉴 출력 및 입력 받기
                menu = input("0 이상 3이하의 숫자로 입력해주세요. ").strip()

                if menu == "":
                    print("입력된 값이 없습니다.")
                elif menu == '0':
                    # 메인 메뉴로 돌아가기
                    IceBox_menu.MainMenu(data["today"], UserID)
                    return
                elif menu == '1' or menu == '2':
                    updater(current_icebox, menu)
                elif menu == '3':
                    current_password = input("현재 비밀번호를 입력해주세요 >> ").strip()
                    if current_password != current_icebox["password"]:
                        print("비밀번호가 올바르지 않습니다.")
                        time.sleep(0.7)
                        if platform.system() == "Windows":
                            os.system("cls")
                        elif platform.system() == "Darwin":
                            os.system("clear")
                        current_info_printer(current_icebox)
                        print("어떤 설정 정보를 수정하시겠습니까?")
                        menu_printer()
                        continue
                    else:
                        updater(current_icebox, menu)
                else:
                    print("올바른 입력값이 아닙니다.\n")
        else:
            # 냉장고 정보가 없는 경우
            return
    except FileNotFoundError:
        # json 파일이 존재하지 않는 경우 
        return
