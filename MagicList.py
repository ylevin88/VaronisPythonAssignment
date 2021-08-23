from typing import List


class MagicList:
    def __init__(self, cls_type=None):
        if cls_type:
            self.__internal_list = List[cls_type]
        else:
            self.__internal_list = []

    def __setitem__(self, key, value):
        if key < len(self.__internal_list):
            self.__internal_list[key] = value
        elif key == len(self.__internal_list):
            self.__internal_list.append(value)
        else:  # if it is invalid index - insert to get the error
            self.__internal_list[key] = value

    def __getitem__(self, item):
        return self.__internal_list[item]

    def __str__(self):
        return self.__internal_list.__str__()
