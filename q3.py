n=int(input("enter rows"))
def pascal_triangle(n):
   l1 = [1]
   trow = l1
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(n)
