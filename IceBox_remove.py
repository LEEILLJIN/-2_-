#냉장고 삭제 화면

import json
import os

import IceBox_menu

# 현재 냉장고는 하나 밖에 없으므로, iceboxes 배열의 0번째 정보를 바로 넣었습니다.
icebox_num = 0 # 냉장고가 여러 개가 되면, 바꿔줘야 한다.
def icebox_remover():
    # json 파일 열기
    file_path = './data/IceBox_data.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r',encoding="utf-8") as f:
            data = json.load(f)
        # 현재 냉장고가 있는 경우
        if data['iceboxes']: 
            current_icebox = data['iceboxes'][icebox_num] # 현재 냉장고의 정보만 가져오기
            # 현재 냉장고 정보 및 삭제 경고 메시지 출력
            print("현재 냉장고 삭제...\n")
            print(f'냉장 - 크기 {current_icebox["refrigerator-size"]}L, 온도 {current_icebox["refrigerator-temp"]}°C')
            print(f'냉동 - 크기 {current_icebox["freezer-size"]}L, 온도 {current_icebox["freezer-temp"]}°C\n')
            print("이 작업을 처리되면 되돌릴 수 없습니다.")

            # 냉장고 삭제 확인
            while(True):
                # 입력 시 좌우 공백 허용을 위한 strip()
                delete_confirm = input("정말로 생성된 냉장고를 삭제하시겠습니까? (Y/N) ").strip()
                if delete_confirm == 'Y' or  delete_confirm == 'y':
                    # 냉장고 삭제 (현재 냉장고 정보 삭제 -> json 파일 덮어쓰기)
                    del data['iceboxes'][icebox_num]
                    with open(file_path, 'w',encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print("냉장고가 정상적으로 삭제되었습니다.")
                    IceBox_menu.MainMenu(data["today"])
                    return
                elif delete_confirm == 'N' or delete_confirm == 'n':
                    print("냉장고 삭제가 취소되었습니다.")
                    IceBox_menu.MainMenu(data["today"])
                    return
                else:
                    print("다시 입력해주세요.")
        else:
            print("삭제할 냉장고가 없습니다 ")
            IceBox_menu.MainMenu(data["today"])
            return
    else:
        print("냉장고 정보 파일이 존재하지 않습니다.")
        IceBox_menu.MainMenu(data["today"])
        return
