from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Shop
from ..serializers import ShopSerializer

# getshopList/
class ShopList(APIView):

    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self):
        pass