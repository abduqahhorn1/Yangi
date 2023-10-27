class ListSort:
    def __init__(self, obj_list):
        self.obj_list = obj_list

    def even_numbers(self):
        even_nums = [num for num in self.obj_list if num % 2 == 0]
        return even_nums

list_obj = ListSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

even_nums_list = list_obj.even_numbers()
print(even_nums_list) 