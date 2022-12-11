#냉장고 삭제 화면

import json
import os
import time
import IceBox_menu

def icebox_remover(UserID):
    # 냉장고 정보 배열 중 현재 냉장고 index
    icebox_num = int(UserID)-1

    # json 파일 열기
    file_path = './data/IceBox_data.json'
    try:
        with open(file_path, 'r',encoding="utf-8") as f:
            data = json.load(f)
        # 현재 냉장고가 있는 경우
        if data['iceboxes']:
            current_icebox = data['iceboxes'][icebox_num] # 현재 냉장고의 정보만 가져오기
            # 현재 냉장고 정보 및 삭제 경고 메시지 출력
            print("현재 냉장고 삭제...\n")
            print(f'냉장 - 크기 {current_icebox["refrigerator-size"]["total"]}L, 온도 {current_icebox["refrigerator-temp"]}°C')
            print(f'냉동 - 크기 {current_icebox["freezer-size"]["total"]}L, 온도 {current_icebox["freezer-temp"]}°C\n')
            print("이 작업을 처리되면 되돌릴 수 없습니다.")

            # 냉장고 삭제 확인
            while(True):
                # 입력 시 좌우 공백 허용을 위한 strip()
                delete_confirm = input("정말로 생성된 냉장고를 삭제하시겠습니까? (Y/N) ").strip()
                if delete_confirm == "":
                    print("입력된 값이 없습니다.")
                elif delete_confirm == 'Y' or  delete_confirm == 'y':
                    while(True):
                        password = input("비밀번호를 입력해주세요 >> ").strip()
                        if password != "":
                            break
                        print("입력된 값이 없습니다.\n")
                    if password != current_icebox["password"]:
                        print("비밀번호가 일치하지 않습니다.")
                        time.sleep(0.7)
                        IceBox_menu.MainMenu(data["today"], UserID)
                    else:
                        # 냉장고 삭제 (현재 냉장고 정보 삭제 -> json 파일 덮어쓰기)
                        del data['iceboxes'][icebox_num]["refrigerator-size"]
                        del data['iceboxes'][icebox_num]["refrigerator-temp"]
                        del data['iceboxes'][icebox_num]["freezer-size"]
                        del data['iceboxes'][icebox_num]["freezer-temp"]
                        del data['iceboxes'][icebox_num]["items"]
                        with open(file_path, 'w',encoding="utf-8") as f:
                            json.dump(data, f, ensure_ascii=False, indent=2)
                        print("냉장고가 정상적으로 삭제되었습니다.")
                        time.sleep(0.7)
                        IceBox_menu.MainMenu(data["today"], UserID)

                elif delete_confirm == 'N' or delete_confirm == 'n':
                    print("냉장고 삭제가 취소되었습니다.")
                    time.sleep(0.7)
                    IceBox_menu.MainMenu(data["today"], UserID)
                else:
                    print("Y(y), N(n)으로 다시 입력해주세요.")
        else:
            # 냉장고 정보가 없는 경우
            return
    except FileNotFoundError:
        # json 파일이 존재하지 않는 경우 
        return