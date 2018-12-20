import turtle

def draw_branch(branch_length):
    """
    绘制分析树
    :param length:
    :return:
    """
    if branch_length > 5:
        if branch_length < 30:
            turtle.pencolor('green')
        else:
            turtle.pencolor('gold')

        #绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        #绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 15)

        if branch_length < 30:
            turtle.pencolor('green')
        else:
            turtle.pencolor('gold')

        #返回之前的树枝
        turtle.right(20)
        turtle.backward(branch_length)

def main():
    """
    主函数
    :return:
    """
    turtle.speed(40)
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    draw_branch(120)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
