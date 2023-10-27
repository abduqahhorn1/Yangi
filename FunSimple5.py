def RectPS(x1,y1,x2,y2):
    A = abs(x1-x2)
    B = abs(y1-y2)
    s = A * B
    p = 2 * (A + B)
    print("S =",s,"  P =",p)
    
RectPS(int(input('x1 = ')),int(input('y1 = ')),
       int(input('x2 = ')),int(input('y2 = ')))

RectPS(int(input('x1 = ')),int(input('y1 = ')),
       int(input('x2 = ')),int(input('y2 = ')))