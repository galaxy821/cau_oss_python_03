# %%
"""
figure_main.py
try-except문을 사용하여
line class의 area_rectangle, area_ellipse, area_right_triangle 함수를 실행했을 때
예외처리를 하는 코드입니다.
"""
import figure

myline = figure.line(10, 20)
width, height = myline.get_length()
# area_rectangle의 예외처리를 위해 try-except문을 사용합니다.
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError :
    print("please input positive number for width and height")

myline.set_length(20, 30)
width, height = myline.get_length()
# area_right_triangle의 예외처리를 위해 try-except문을 사용합니다.
try :
    rigth_triangle = figure.area_right_triangle(width, height)
    print(rigth_triangle)
except ValueError :
    print("please input positive number for width and height")

myline.set_length(30, 40)
width, height = myline.get_length()
# area_ellipse의 예외처리를 위해 try-except문을 사용합니다.
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError :
    print("please input positive number for width and height")