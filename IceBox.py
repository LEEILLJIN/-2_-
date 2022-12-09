#main (초기 화면)
#기획서에는 json 파일을 냉장고 생성할 때 같이 만드는거로 되었지만 일단 예시 파일로 구현 진행
import json

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
            # IceBox_menu.MainMenu(today)
            LogInorJoin(today)
            #냉장고 생성 후 json파일이 만들어질떄 today data를 넣기위해 인자로 전달
        else:
            print("유효하지 않은 날짜입니다. 다시 입력해주세요.")
            continue

def validate_date(today):
    try:
        if today.isspace() or today == "":
            today = "whiteSpace"
            return today
        temp = today.split("-")         
        if str(len(temp)) != "3":
            return False
        else:
            year = int(temp[0])
            # month = int(temp[1])
            # day = int(temp[2])

            if 2000 > year or 2999 < year:
                return False
            # for i in range(len(temp)):
            #     temp[i] = str(int(temp[i]))
            # today='-'.join(temp)
            datetime.datetime.strptime(today,"%Y-%m-%d")
            return today
    except ValueError:
        # print("Incorrect data format({0}), should be YYYY-MM-DD".format(today))
        return False

def LogInorJoin(today):
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")
    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    print(f"오늘 날짜 : <{today}>")
    print("1. 로그인")
    print("2. 회원가입")

    while True:
        menuInput = input()
        if menuInput.isspace() or menuInput == "":
            print("입력된 값이 없습니다.")
            continue
        elif menuInput == "1":
            if json_data["iceboxes"]:
                LogIn(today)
                # 로그인 화면으로
            else :
                # iceboxes에 아무것도 없을 경우 -> 2차 기획서 수정해야함
                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                print("등록된 회원이 없습니다. 먼저 회원가입을 해주세요.")
                continue
           
        elif menuInput == "2":
            Join(today)
            # 회원가입 화면으로
        else:
            print("1 또는 2만 입력할 수 있습니다.")

def LogIn(today):
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")

    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    if json_data["iceboxes"]:
        iceBox = json_data['iceboxes']
        MaxId = len(iceBox)
    else :
        MaxId = 1
    while True :
        IdInput = input("아이디 : ")
        if Validate_ID(IdInput, MaxId) :
            RightPassword = iceBox[int(IdInput)-1]["password"]
            while True:
                PasswordInput = input("비밀번호 : ")
                if Validate_Password(PasswordInput, RightPassword) :
                    IceBox_menu.MainMenu(today, IdInput)
                else :
                    continue
        else:
            continue

def Validate_Password(PasswordInput, RightPassword) :
    if PasswordInput == RightPassword:
        return True
    elif PasswordInput.isspace() or PasswordInput == "":
        print("입력된 값이 없습니다.")
        return False
    elif (PasswordInput.isdigit()) and (len(PasswordInput)) == 6:
        print("비밀번호가 틀렸습니다. 다시 입력해주세요.")
        return False
    else :
        print("비밀번호는 6자리 숫자로 입력해주세요.")
        return False

def Validate_ID(IdInput, MaxId):
    if IdInput.isspace() or IdInput == "":
        print("입력된 값이 없습니다.")
        return False
    elif IdInput.isdigit() == False:
        print("존재하지 않는 ID입니다.")
        return False
    elif len(str(int(IdInput))) != len(IdInput):
        print("존재하지 않는 ID입니다.")
        return False
    elif int(IdInput) <= 0:
        print("존재하지 않는 ID입니다.")
        return False
    elif (IdInput.isdigit() == True) & (int(IdInput) <= MaxId):
        return True
    else :
        print("존재하지 않는 ID입니다.")
        return False

def Join(today):
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")

    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    iceBox = json_data['iceboxes']
    # today를 업데이트 하는건 IceBox_menu에서
    inputData = {"id" : "", "password" : ""}
    if json_data["iceboxes"]:
        #현재 회원이 있을 경우 
        UserId = len(iceBox)+1
    else:
        #현재 회원이 없는 경우
        UserId = 1
    
    print(f"귀하의 ID는 {UserId}입니다.")
    print("비밀번호를 설정해주세요.")
    while True:
        UserPassword = input()
        if UserPassword.isspace() or UserPassword == "":
            print("입력된 값이 없습니다.")
            continue
        elif (UserPassword.isdigit() == False) or (len(UserPassword) != 6):
            print("비밀번호는 6자리 숫자로 입력해주세요.")
            continue
        else:
            break
    inputData["id"] = str(UserId)
    inputData["password"] = str(UserPassword)
    iceBox.append(inputData)
    #JSON 파일 업데이트
    with open("./data/IceBox_data.json", 'w', encoding='UTF8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2)

    LogInorJoin(today) 

def main():
    DateInput()

if __name__ == "__main__":
	main()
