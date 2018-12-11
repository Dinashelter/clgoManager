import sub_menu_ui
student_info_list = []


# Add student info to the list
def add_new_student_info():
    student_info = sub_menu_ui.fill_student_info()
    student_info_list.append(student_info)


# Change student info in the list
def change_student_info(student_info):
    student_info_updated = sub_menu_ui.fill_student_info()
    student_info.update(student_info_updated)
    update_student_info_in_list(student_info)


# Delete student info
def delete_student_info(student_name):
    for student_info in student_info_list:
        if student_info["name"] == student_name:
            student_info_list.remove(student_info)
            break
        else:
            pass
    else:
        print("无法找到" + student_name)


# Find all student info
def find_all_student_info():
    if len(student_info_list) == 0:
        print("暂无学生数据")
    else:
        sub_menu_ui.print_table_head()
        for student_info in student_info_list:
            sub_menu_ui.print_table_line(student_info)


# Find student info
def find_student_info():
    student_name = input("请输入想要查找的名字：")
    if find_student_info_in_list(student_name) == ("无法找到" + student_name):
        print("无法找到" + student_name)
        return
    else:
        sub_menu_ui.print_table_head()
        student_info = find_student_info_in_list(student_name)
        sub_menu_ui.print_table_line(student_info)

    while True:
        print("1. 修改")
        print("2. 删除")
        print("")
        print("0. 返回上级菜单")
        sub_menu_num = input("请输入想要进行的操作：")
        if sub_menu_num == '0':
            return
        elif sub_menu_num == '1':
            change_student_info(student_info)
            return
        elif sub_menu_num == '2':
            delete_student_info(student_name)
            return
        else:
            print("错误的菜单号，请重新输入")
            continue


# Update the student info record
def update_student_info_in_list(student_info_updated):
    for student_info in student_info_list:
        if student_info["name"] == student_info_updated["name"]:
            student_info.update(student_info_updated)
            break
        else:
            pass
    else:
        pass


# Change student info in the list
def find_student_info_in_list(student_name):
    for student_info in student_info_list:
        if student_info["name"] == student_name:
            return student_info
        else:
            pass
    else:
        return "无法找到" + student_name
