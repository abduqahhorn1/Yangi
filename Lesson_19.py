class Line:

    def __init__(self,Length:int) -> None:
        self.length = Length

    def __str__(self) -> str:
        return f"{self.__class__.__name__} object . Length: {self.length}mm"
    
    def __repr__(self) -> str:
        return str( self.__dict__)
    
    def __add__(self,__value):
        if isinstance(__value , (int,float)):
            self.length -= __value
            return self.length
        raise ValueError(" 'Line' class objectiga int yoki float qo'shing ")
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value,self.__class__):
            return self.length == __value 
        raise ValueError("Invalid data")
    def __lt__(self,__value: object):
        if isinstance(__value,self,__class__):
            return self.length <= __value.length
        if isinstance(__value,{int,float}):
            return self.length <= __value
        raise ValueError("Invalid")






l = Line(Length=78)
l2 = Line(Length=78)

print(l < 176)
