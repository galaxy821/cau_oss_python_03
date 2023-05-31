"""
figure.py
그림과 관련된 함수들을 모아놓은 모듈입니다.

line class는 선들의 길이를 저장하는 변수 width, height를 가지고 있으며, 
line class의 get_length, set_length 함수를 통해 width, height 값을 불러오거나 설정할 수 있습니다.

area_rectangle, area_ellipse, area_right_triangle 함수는 각각 직사각형, 타원, 직각 삼각형의 넓이를 구하는 함수입니다.
"""

import math

class line :
    """line class
    선들의 길이를 저장하는 클래스입니다.
    
    Attributes:
        __width (int or float): 선의 가로 길이
        __height (int or float): 선의 세로 길이
    
    Methods:
        get_length: 선들의 길이를 반환합니다.
        set_length: 선들의 길이를 설정합니다.
    """ 
    __width = 0
    __height = 0
    
    def __init__(self, width, height) :
        """__init__
        생성자를 통해 선들의 초기 길이를 설정합니다.

        Args:
            width (int or float): 선의 가로 길이
            height (int or float): 선의 세로 길이
        """
        self.__width = width
        self.__height = height
        
    def get_length(self) :
        """get_length
        선들의 길이를 반환합니다.

        Returns:
            tuple(int or float, int or float) : 선들의 길이
        """
        return self.__width, self.__height
    
    def set_length(self, width, height) :
        """set_length
        선들의 길이를 설정합니다.

        Args:
            width (int or float): 선의 가로 길이
            height (int or float): 선의 세로 길이
        """
        self.__width = width
        self.__height = height
        
def area_rectangle(width, height) :
    """area_rectangle
    선의 길이를 통해 직사각형의 넓이를 반환합니다.

    Args:
        width (int or float): 직사각형의 가로 길이
        height (int or float) : 직사각형의 세로 길이
    Returns:
        int or float : 직사각형의 넓이
    """
    if width <= 0 or height <= 0 : raise ValueError
    return width * height

def area_ellipse(width, height) :
    """area_ellipse
    선의 길이를 통해 타원의 넓이를 반환합니다.

    Args:
        width (int or float): 타원의 가로 반지름 길이
        height (int or float): 타원의 세로 반지름 길이
    Returns:
        int or float : 타원의 넓이
    """
    if width <= 0 or height <= 0 : raise ValueError
    return math.pi * width * height

def area_right_triangle(width, height) :
    """area_right_triangle
    선의 길이를 통해 직각 삼각형의 넓이를 반환합니다.

    Args:
        width (int or float): 직각 삼각형의 밑변의 길이
        heigth (int or float): 직각 삼각형의 높이
    Returns:
        int or float : 직각 삼각형의 넓이
    """
    if width <= 0 or height <= 0 : raise ValueError
    return width * height / 2