   
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