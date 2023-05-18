"""
figure.py
그림과 관련된 함수들을 모아놓은 모듈입니다.

line class는 길이를 저장하는 변수 length를 가지고 있으며, 
line class의 get_length, set_length 함수를 통해 length 값을 불러오거나 설정할 수 있습니다.

area_square, area_circle, area_regular_triangle 함수는 각각 정사각형, 원, 정삼각형의 넓이를 구하는 함수입니다.
"""

import math

class line :
    """line class
    선의 길이를 저장하는 클래스입니다.
    
    Attributes:
        __length (int or float): 선의 길이 입니다.
    
    Methods:
        get_length: 선의 길이를 반환합니다.
        set_length: 선의 길이를 설정합니다.
    """ 
    __length = 0
    
    def __init__(self, length) :
        """__init__
        생성자를 통해 선의 초기 길이를 설정합니다.

        Args:
            length (int or float): 선의 길이
        """
        self.__length = length
        
    def get_length(self) :
        """get_length
        선의 길이를 반환합니다.

        Returns:
            int or float: 선의 길이
        """
        return self.__length
    
    def set_length(self, length) :
        """set_length
        선의 길이를 설정합니다.

        Args:
            length (int or float): 선의 길이
        """
        self.__length = length
        
def area_square(length) :
    """area_square
    선의 길이를 통해 정사각형의 넓이를 반환합니다.

    Args:
        length (int or float): 정사각형의 한 변의 길이
    Returns:
        int or float : 정사각형의 넓이
    """
    return length * length

def area_circle(length) :
    """area_circle
    선의 길이를 통해 원의 넓이를 반환합니다.

    Args:
        length (int or float): 반지름의 길이
    Returns:
        int or float : 원의 넓이
    """
    return math.pi * length * length

def area_regular_triangle(length) :
    """area_regular_triangle
    선의 길이를 통해 정삼각형의 넓이를 반환합니다.

    Args:
        length (int or float): 정삼각형의 한 변의 길이
    Returns:
        int or float : 정삼각형의 넓이
    """
    return math.sqrt(3) / 4 * length * length