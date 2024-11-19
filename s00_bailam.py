#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/uYheiLdfy6K8LVQj6

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333, and 4444!
"""
#endregion debai

#region bailam
def hi(*args, **key):
   if 'name' in key:
      if key['name'] in (None, ''):
         return "Hi!"
      return f"Hi {key['name']}!"
   valid_args = []
   for arg in args:
      if arg not in (None, ''):
         valid_args.append(arg)
   if len(valid_args) == 0:
      return "Hi!"
   if len(valid_args) == 1:
      return f"Hi {valid_args[0]}!"
   return f"Hi {', '.join(valid_args[:-1])}, and {valid_args[-1]}!"
#endregion bailam
