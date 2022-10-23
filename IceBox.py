#main (초기 화면)
#기획서에는 json 파일을 냉장고 생성할 때 같이 만드는거로 되었지만 일단 예시 파일로 구현 진행

import datetime
import os
import platform

import IceBox_menu


def DateInput():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")
    while True:
        today = str(input("오늘 날짜를 입력해주세요. >> "))
        today = validate_date(today)
        if today == "whiteSpace":
            print("입력된 값이 없습니다.")
            continue
        elif(type(today) == str):
            # print(today,"날짜 적합\n")
            IceBox_menu.MainMenu(today)
            #냉장고 생성 후 json파일이 만들어질떄 today data를 넣기위해 인자로 전달
        else:
            print("유효하지 않은 날짜 입니다. 다시 입력해주세요.")
            continue

def validate_date(today):
    try:
        temp = today.split("-")
        year = int(temp[0])
        month = int(temp[1])
        day = int(temp[2])

        if 2000 > year or 2999 < year:
            return False
        for i in range(len(temp)):
            temp[i] = str(int(temp[i]))
        today='-'.join(temp)
        datetime.datetime.strptime(today,"%Y-%m-%d")
        return today
    except ValueError:
        # print("Incorrect data format({0}), should be YYYY-MM-DD".format(today))
        if today.isspace() or today == "":
            today = "whiteSpace"
            return today
        return False

def main():
    DateInput()

if __name__ == "__main__":
	main()
