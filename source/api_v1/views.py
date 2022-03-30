from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import ProductSerializer, OrderSerializer
from webapp.models import Product, Order


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=204)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(remainder__gte=1)
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny]
        return [IsAdminUser]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)



