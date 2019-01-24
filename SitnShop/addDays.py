from market.models import Day

f = open('C:/Hiruna/sem6/co328/punk/Days.csv', 'r')

for line in f:  
   line =  line.split(',')  
   # print(line[2])
   z = Day.objects.create(day_name=line[0])
   # product = Product()  
   # product.name = line[2] + '(' + line[1] + ')'  
   # product.description = line[4]  
   # product.price = '' #data is missing from file  
   # product.save()  

f.close()  



# >>> from market.models import *
# >>> user = User.objects.get(id=3)
# >>> fls = user.follows.all()
# >>> fls
# <QuerySet [<Follow: Follow object (6)>]>
# >>> flwd = user.is_followed_by.all()
# >>> flwd
# <QuerySet [<Follow: Follow object (8)>]>
# >>> user = User.objects.get(id=2)
# >>> flwd = user.is_followed_by.all()
# >>> fls = user.follows.all()
# >>> fls
# <QuerySet [<Follow: Follow object (8)>]>
# >>> flwd = user.is_followed_by.all()
# >>> flwd
# <QuerySet [<Follow: Follow object (4)>, <Follow: Follow object (6)>, <Follow: Follow object (7)>]>