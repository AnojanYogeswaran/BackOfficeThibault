from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct
from monTiGMagasin.serializers import InfoProductSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Count



#######################
#...TME3 JWT starts...#
from rest_framework.permissions import IsAuthenticated
#...end of TME3 JWT...#
#######################

# Create your views here.
class InfoProductList(APIView):
#######################
#...TME3 JWT starts...#
    permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = InfoProductSerializer(data=request.data)
        if serializer.is_valid():
            # Vérifie si un produit avec le même tig_id existe déjà
            if InfoProduct.objects.filter(tig_id=request.data['tig_id']).exists():
                return Response({'error': 'Un produit avec ce tig_id existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def put(self, request, format=None):
        products = InfoProduct.objects.all()
        for product in products:
            product.tig_id = product.id
            product.save()
        return Response({'success': 'Les tig_id ont été mis à jour avec succès.'})
    
class InfoProductDetail(APIView):
#######################
#...TME3 JWT starts...#
    permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
    
       
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        product.delete()
        return Response(200)

class PutOnSale(APIView):
   permission_classes = (IsAuthenticated,)
   def put(self, request, tig_id, newprice):
    product = InfoProduct.objects.get(id=tig_id)
    serializer = InfoProductSerializer(product)
    if product.sale == False :
        product.sale = True
    product.discount = newprice
    product.save()
    return Response(serializer.data)
   
class RemoveSale(APIView):
   permission_classes = (IsAuthenticated,)
   def put(self, request, tig_id):
    product = InfoProduct.objects.get(id=tig_id)
    serializer = InfoProductSerializer(product)
    if product.sale == True :
        product.sale = False
    product.discount = 0
    product.save()
    return Response(serializer.data)
        
class IncrementStock(APIView):
   permission_classes = (IsAuthenticated,)
   def put(self, request, unites, tig_id):
    product = InfoProduct.objects.get(id=tig_id)
    serializer = InfoProductSerializer(product)
    product.quantityInStock += unites
    product.save()
    return Response(serializer.data)
   
class DecrementStock(APIView):
   permission_classes = (IsAuthenticated,)
   def put(self, request, unites, tig_id):
    product = InfoProduct.objects.get(id=tig_id)
    serializer = InfoProductSerializer(product)
    product.quantityInStock -= unites
    product.save()
    return Response(serializer.data)
   
class update_product_sale(APIView):
   permission_classes = (IsAuthenticated,)
   products = InfoProduct.objects.all()
   for product in products:
        if product.quantityInStock > 16:
           product.sale = True
           if product.quantityInStock <= 64:
              product.discount = 0.8* product.price
           else:
              product.discount = 0.5* product.price
        else:
           product.sale = False 
           product.discount = 0
        product.save()


    
