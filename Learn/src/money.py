input_str = input('请输入货币金额（USD/CNY),退出请输入Q:')

USD_VS_CNY = 7
while input_str != 'Q':
    unit = input_str[-3:]
    if unit == 'USD':
        usd_str_value = input_str[:-3]
        usd_value = eval(usd_str_value)
        print('你的货币为：%d' % usd_value)
        cny_value = usd_value * USD_VS_CNY
        print("您的货币可兑换%d元 人民币" % cny_value)
    elif unit == 'CNY':
        cny_value = input_str[:-3]
        cny_str_value = input_str[:-3]
        cny_value = eval(cny_str_value)
        print('你的货币为：%d' % cny_value)
        usd_value = cny_value / USD_VS_CNY
        print("您的货币可兑换%d美元" % usd_value)
    else:
        print("您的货币不支持兑换！")

    input_str = input('请输入货币金额（USD/CNY),退出请输入Q:')

print("程序已退出！")