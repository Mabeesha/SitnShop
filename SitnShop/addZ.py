from market.models import ZIPCode

f = open('C:/Hiruna/sem6/co328/punk/Kandy.csv', 'r')

for line in f:  
   line =  line.split(',')  
   # print(line[2])
   z = ZIPCode.objects.create(District=line[0], City=line[1], Code=line[2])

f.close()  

# >>> user = User.objects.get(id=2)
# >>> user
# <User: shop1>
# >>> r = user.is_reported_by.all()
# >>> r
# <QuerySet [<Report: Report object (4)>]>
# >>> r[0].reported
# <User: shop1>
# >>> r[0].reporting
# <User: hiruna72>
# >>> user = User.objects.get(id=3)
# >>> user
# <User: shop2>
# >>> user = User.objects.get(id=4)
# >>> user
# <User: hiruna72>
# >>> r = user.has_reported.all()
# >>> r
# <QuerySet [<Report: Report object (4)>]>
# >>> r[0].reported
# <User: shop1>

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

# -----------------------------------------------------------------------------------------------------------------------------------

# from scipy.spatial import cKDTree
# import numpy as np
# # A = np.random.random((10,2))*100
# A = np.array([[7.2642107,80.5930652],[7.2574688,80.607362]])
# print(A)
# pt = [6.9016085999999,80.0087746]  # <-- the point to find
# A[cKDTree(A).query(pt)[1]]
# [[ 7.2642107 80.5930652]
#  [ 7.2574688 80.607362 ]]
# array([ 7.2642107, 80.5930652])

# from geopy import Nominatim
# ​
# geolocator =  Nominatim(user_agent="sitnshop")
# ​
# with open("cities.txt",'r') as fp:
#     for line in fp:
#         location = geolocator.geocode(line)
#         print (location.latitude, location.longitude)
# fp.close()
# 7.2642107 80.5930652
# 7.2574688 80.607362