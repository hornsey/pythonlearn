"""
    hornsey
    version:1.0
    data：2018-10-17
"""
import turtle

def draw_pentagram(size):
    """
    绘制五角星
    :return:
    """
    i = 0
    while i < 5:
        turtle.forward(size)
        turtle.right(144)
        i = i + 1

def main():
    """
    主函数
    :return:
    """
    turtle.penup()
    turtle.backward(300)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('red')

    j=5
    while j > 0:
        draw_pentagram(100-j*10)
        j -= 1


    turtle.exitonclick()


if __name__ == '__main__':
    main()

