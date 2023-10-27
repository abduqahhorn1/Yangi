# class News:
#     title = "New title"

#     def news_info(self):
#         print("  news_info is working ")


# s = News()   
# print(s.title) 
# print(s.news_info() )

# 
class Writer:
    def __init__(self,filename) -> None:
        assert filename.endswith() (".txt"), "Fayl formati xato"
        self.file = filename

    def write(self, text):
        print( self.file)
        with open(self.file , "w") as f:
            f.write(text)

file = Writer(filename="data.txt")
file.write("Assalom")