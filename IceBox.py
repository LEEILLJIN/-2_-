#main (초기 화면)
#기획서에는 json 파일을 냉장고 생성할 때 같이 만드는거로 되었지만 일단 예시 파일로 구현 진행
import datetime
import IceBox_menu
def DateInput():
    while True:
        today = str(input("오늘 날짜를 입력해주세요 : "))
        today = validate_date(today)
        if(type(today) == str):
            # print(today,"날짜 적합")
            IceBox_menu.MainMenu(today)
            #냉장고 생성 후 json파일이 만들어질떄 today data를 넣기위해 인자로 전달
        else:
            # print(today,"날짜 부적합")
            continue

def validate_date(today):
    try:
        temp = today.split("-")
        for i in range(len(temp)):
            temp[i] = str(int(temp[i]))
        today='-'.join(temp)
        datetime.datetime.strptime(today,"%Y-%m-%d")
        return today
    except ValueError:
        # print("Incorrect data format({0}), should be YYYY-MM-DD".format(today))
        return False

def main():
    DateInput()

if __name__ == "__main__":
	main()