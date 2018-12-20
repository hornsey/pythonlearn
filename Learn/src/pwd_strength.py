"""
    功能：检查密码强度
"""

def check_str_num(str):
    """
    检查字符串是否含有数字
    :param str:
    :return:
    """
    flag = False
    for x in str:
        if x.isnumeric():
            flag = True
            break

    return flag


def check_str_alpha(str):
    """
    检查字符串是否含有字母
    :param str:
    :return:
    """
    flag = False
    for x in str:
        if x.isalpha():
            flag = True
            break

    return flag

def main():
    num = 0
    while num < 5:
        num += 1
        pwd_str = input("请输入密码：")

        strength_level = 0
        if len(pwd_str) < 8:
            print("密码长度太短！")
            continue
        else:
            strength_level += 1

        if check_str_num(pwd_str):
            strength_level += 1
        else:
            print("密码应包含数字！")
            continue

        if check_str_alpha(pwd_str):
            strength_level += 1
        else:
            print("密码应包含字母")
            continue

        if strength_level == 3:
            print("你的密码强度满足要求！")
            break


if __name__ == '__main__':
    main()