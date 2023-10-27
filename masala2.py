class MyList:
    def __init__(self, obj_list):
        self.obj_list = obj_list

    def add(self, obj):
        self.obj_list.append(obj)

    def del_obj(self, obj):
        if obj in self.obj_list:
            self.obj_list.remove(obj)

    def clear_objects(self):
        self.obj_list = []


m = MyList(obj_list=[])
print(m.obj_list)  

m.add(34)
m.add(44)
print(m.obj_list) 

m.del_obj(44)
print(m.obj_list)  

m.clear_objects()
print(m.obj_list)  