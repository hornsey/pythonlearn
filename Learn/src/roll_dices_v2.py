"""
    作者：hornsey
    说明：掷骰子，统计各种情况
"""


import random
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

def roll_dice():
    """
    得到一个骰子的点数
    :return:
    """
    roll = random.randint(1,6)
    return roll

def main():
    total_times = 1000

    roll_time = [0]*11
    roll_results = list(range(2,13))
    roll_list = []

    roll_dict = dict(zip(roll_results,roll_time))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_dict[roll1 + roll2] += 1
        roll_list.append(roll1+roll2)

    for result,time in roll_dict.items():
        print("点数{} 的次数是{}, 概率是{}.".format(result,time,time/total_times))

#    plt.plot(roll_dict.keys(),roll_dict.values())
    plt.hist(roll_list,bins=range(2,14),normed=1,edgecolor='black',linewidth=2)
    plt.title("骰子点数统计")
    plt.xlabel('点数')
    plt.ylabel('概率')
    plt.show()

if __name__ == '__main__':
    main()