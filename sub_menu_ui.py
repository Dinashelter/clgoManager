import sub_menu_function


def fill_student_info():
    student_info = {
        "name": "",
        "age": "",
        "phone": "",
        "email": ""
    }

    print("请输入以下信息：")
    while True:
        student_name = input("姓名：")
        if student_name == "":
            print("姓名不能为空")
            continue
        # elif sub_menu_function.find_student_info_in_list(student_name) != ("无法找到" + student_name):
        #   print("该姓名已存在")
        #   continue
        else:
            pass

        student_age = input("年龄：")
        student_phone = input("手机：")
        student_email = input("Email： ")

        student_info["name"] = student_name
        student_info["age"] = student_age
        student_info["phone"] = student_phone
        student_info["email"] = student_email

        return student_info


def print_table_head():
    print("姓名\t年龄\t手机\tEmail")


def print_table_line(student_info):
    print("%s\t%s\t%s\t%s" % (
          student_info["name"],
          student_info["age"],
          student_info["phone"],
          student_info["email"]))
