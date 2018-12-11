# This is the menu of clgo manager
# also the entrance of the whole procedure
import sub_menu_function

main_ui_dict = {
    "decoration": "*" * 40,
    "system_name": "CLGO 管家 v1.0",
    "empty_line1": "",
    "menu_1_name": "1. 新建名片",
    "menu_2_name": "2. 显示所有名片",
    "menu_3_name": "3. 查找名片",
    "empty_line2": "",
    "menu_0_name": "0. 退出系统"
}
available_menuNum = [1, 2, 3]


while True:
    for key in main_ui_dict:
        print(main_ui_dict[key])

    menuNum = input("请输入菜单号：")

    if menuNum == '0':
        exit(-1)
    elif menuNum == '1':
        sub_menu_function.add_new_student_info()
    elif menuNum == '2':
        sub_menu_function.find_all_student_info()
    elif menuNum == '3':
        sub_menu_function.find_student_info()
    else:
        print("错误的菜单号，请重新输入")
        continue
