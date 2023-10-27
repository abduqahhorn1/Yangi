# class Iron:
#     def turn_on(self):
#         print("Yondi")

#     def indicator(self):
#         print("Indikator ishladi Tok taqsimlandi")

#     def work(self):
#         print(" Ishladi ")

#     def turn_off(self):
#         print("O'chirildi")

# dazmol = Iron()
# dazmol.indicator()

import random
class Worker:
    def request_salary(self):
        salary = random.randint(70000 , 100000)
        self.salary = salary
        return self.__get_salary()

    def get_salary(self):
        return f"{self.salary} sum pul berildi"
    
w = Worker()
w.salary = 100000000
print( w.request_salary())
 