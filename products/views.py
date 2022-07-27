import json

from django.http           import JsonResponse
from django.views          import View
from django.core.paginator import Paginator
from django.db.models      import Q
from django.db.models import F, Sum, Count, Case, When

from products.models import *
from orders.models   import *
from core.utils      import *


# class ListView_draft(View):

#     '''
#     페이지 상단의 (main) category를 클릭하면 
#     (main) category 전체와 선택된 (main) category의 sub categoies list를 보여주는 동시에
#     해당 (main) category에 속하는 모든 제품의 리스트(이미지, 브랜드, 제품명, 가격 포함)를 보여준다.
#     여기에서, sub category(또는 (main) category)를 클릭하면 해당 sub category(또는 (main) category)에 속하는 제품들의 리스트만를 반환한다.

#     목적: 사용자가 (main) categories 중 하나를 선택했을 때는 해당하는 sub categories 리스트와 (main) category에 속하는 제품 리스트를 반환하고
#         sub categories 중 하나를 선택했을 때는 그 sub category에 속하는 제품 리스트를 반환한다.

#     1. client가 보내온 데이터에서 요청하는 category를 받아온다.
#     2. 요청받은 category가 (main)인지 sub인지 확인 후 
#     3-1. 요청받은 (main) category에 속하는 sub categories를 DB에서 찾는다.
#             요청받은 (main) category에 속해있는 제품 전부를 DB에서 찾는다.
#             찾은 데이터를 리스트로 만들어서 json파일로 변환하여 반환한다.
#     3-2. 요청받은 sub category에 속하는 제품들을 DB에서 찾는다.
#             찾은 데이터를 리스트로 반환한다.
#     '''

#     def get(self, request):
#         try:
#             data = json.loads(request.body)
#             selected_category = data['category']

#             main_categories = Category.objects.all()
#             # QuerySet: [ <'id':1, 'name':'소파'>,
#             #             <'id':2, 'name':'체어'>,
#             #             ... ]
#             sub_categories = SubCategory.objects.all()
#             # QuerySet: [ <'id':1, 'name':'라운지 체어'>,
#             #             <'id':2, 'name':'바 체어'>,
#             #             <'id':3, 'name':'키즈 체어'>,
#             #             ... ]

#             if selected_category in [category.name for category in main_categories]:
#                 subs = SubCategory.objects.filter(
#                     category__name=selected_category)
#                 sub_list = []
#                 for sub in subs:
#                     sub_list.append(sub.name)
#                 products = Product.objects.filter(
#                     sub_category__category__name=selected_category)

#                 product_list = []
#                 for product in products:
#                     product_list.append({
#                         'id': product.id,
#                         'image': product.thumbnail_image_url,
#                         'brandName': product.furniture.brand.name,
#                         'productName': product.furniture.name + '_' + product.color.name,  # 가능? 오 된다
#                         'price': product.price
#                     })
#                 return JsonResponse({'message': 'SUCCESS', 'sub_list': sub_list, 'product_list': product_list}, status=200)
#             elif selected_category in [category.name for category in sub_categories]:
#                 products = Product.objects.filter(
#                     sub_category__name=selected_category)
#                 product_list = []
#                 for product in products:
#                     product_list.append({
#                         'id': product.id,
#                         'image': product.thumbnail_image_url,
#                         'brandName': product.furniture.brand.name,
#                         'productName': product.furniture.name + '_' + product.color.name,
#                         'price': product.price
#                     })
#                 return JsonResponse({'message': 'SUCCESS', 'product_list': product_list}, status=200)
#                 '''
#                 product_list = [{
#                     'id'         : 5,
#                     'image'      : 'https://www.abcd',
#                     'brandName'  : 'HAY',
#                     'productName': '팔리사이드 쉐이즈 롱_올리브',
#                     'price'      : 100000
#                 }]
#                 '''
#             else:
#                 return JsonResponse({'message': 'INVALID_CATEGORY'}, status=400)
#         except KeyError:
#             return JsonResponse({'message': 'KEY_ERROR'}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({'message': 'JSON_ERROR'}, status=400)




# class CategoryView(View):

#     def get(self, request, category_id):
#         try:            
#             category = Category.objects.get(id = category_id)
#             products = Product.objects.filter(sub_category__category__id = category_id)
#             product_list = []
#             for product in products:
#                 product_list.append({
#                         'id': product.id,
#                         'image': product.thumbnail_image_url,
#                         'brandName': product.furniture.brand.name,
#                         'productName': product.furniture.korean_name + '_' + product.color.korean_name,
#                         'price': product.price
#                     }                    
#                 )
#             return JsonResponse({'message': 'SUCCESS', 'product_list': product_list}, status=200)
#             '''
#             product_list = [{
#                 'id'         : 5,
#                 'image'      : 'https://www.abcd',
#                 'brandName'  : 'HAY',
#                 'productName': '팔리사이드 쉐이즈 롱_올리브',
#                 'price'      : 100000
#             }]
#             '''
#         except Category.DoesNotExist:
#             return JsonResponse({'message': 'INVALID_CATEGORY'}, status=400)
        
#         except json.JSONDecodeError:
#             return JsonResponse({'message': 'JSON_ERROR'}, status=400)


# class SubCategoryView(View):

#     def get(self, request, sub_category_id):
#         try:            
#             sub_category = SubCategory.objects.get(id = sub_category_id)
#             products = Product.objects.filter(sub_category = sub_category)
#             product_list = []
#             for product in products:
#                 product_list.append({
#                         'id': product.id,
#                         'image': product.thumbnail_image_url,
#                         'brandName': product.furniture.brand.name,
#                         'productName': product.furniture.korean_name + '_' + product.color.korean_name,
#                         'price': product.price
#                     }                   
#                 )
#             return JsonResponse({'message': 'SUCCESS', 'product_list': product_list}, status=200)
#             '''
#             product_list = [{
#                 'id'         : 5,
#                 'image'      : 'https://www.abcd',
#                 'brandName'  : 'HAY',
#                 'productName': '팔리사이드 쉐이즈 롱_올리브',
#                 'price'      : 100000
#             }]
#             '''
#         except SubCategory.DoesNotExist:
#             return JsonResponse({'message': 'INVALID_SUB_CATEGORY'}, status=400)
        
#         except json.JSONDecodeError:
#             return JsonResponse({'message': 'JSON_ERROR'}, status=400)

######## 판매량순으로 order_by 실패... ↓포기한다#########
# class ProductListView(View):
#     def get(self, request):
#         '''
#         필요한 예외처리
#       (x)  1. DB에 없는 value이 들어온 경우 404 + 첫 페이지???
#       (x)  2. 올바르지 않은 parameter가 들어온 경우 400 + 첫 페이지이이이???? >> 400이 아니구 셋 다 없는 경우로 취급되겠구만
#       ()  3. category_id와 sub_category_id가 맞지 않는 경우 400 + sub_category에 맞는 페이지?
#         '''
#         try:
#             DEFAULT_LIMIT = 4
#             DEFAULT_OFFSET = 0

#             category_id     = request.GET.get('category_id', None)
#             sub_category_id = request.GET.get('sub_category_id', None)
#             # page_number       = request.GET.get('page', 1)
#             # pagesize          = request.GET.get('pagesize', 8)
#             limit           = int(request.GET.get('limit', DEFAULT_LIMIT))
#             offset          = int(request.GET.get('offset', DEFAULT_OFFSET))
#             sort_type       = int(request.GET.get('sort_type', 1))   # id순(1 = default), 신상품순(2), 높은가격순(3), 낮은가격순(4), 판매순(5)
           
#             # if category_id:
#             #     Category.objectes.get(id = category_id)
#             # if sub_category_id:
#             #     SubCategory.objects.get(id = sub_category_id)
            
#             sub_category_q = Q()

#             product_q = Q()

#             if category_id:
#                 category        = Category.objects.get(id = category_id)
#                 sub_category_q &= Q(category=category)
#                 product_q      &= Q(sub_category__category = category)

#             if sub_category_id:
#                 sub_category    = SubCategory.objects.get(id = sub_category_id)
#                 sub_category_q &= Q(category=sub_category.category)
#                 product_q      &= Q(sub_category = sub_category)

#             count = len(Product.objects.filter(product_q))
            
#             if offset > count: 
#                 return JsonResponse({'message': 'INVALID_OFFSET'}, status=404)

#             sub_category_list = [ sub_category.name for sub_category in SubCategory.objects.filter(sub_category_q) ]

#             # id순(1 = default), 신상품순(2), 높은가격순(3), 낮은가격순(4), 판매순(5)
#             # Product.annotate(updated_at=Product.furniture.updated_at)
#             # Product.annotate(total_quantity=OrderItme.)
#             sort_set = { 
#                 1: 'id',
#                 2: 'furniture__updated_at',
#                 3: '-price',
#                 4: 'price',
#                 5: 'total_quantity',
#             }

#             TotalPrice = OrderItem.objects.values('product').annotate(total_price=Sum('product__price'))
#             Product2 = OrderItem.objects.values('product__id','product__thumbnail_image_url','product__furniture','product__price','product__color','product__sub_category').annotate(total_quantity=Sum('quantity'))

#             sort_field = sort_set.get(sort_type, 'id')
#             products = Product2.filter(product_q).order_by(sort_field)[offset:offset+limit]
            
#             product_list = [{
#                 'id'         : product.product__id,
#                 'image'      : product.product__thumbnail_image_url,
#                 'brandName'  : product.product__furniture.brand.name,  
#                 'productName': product.product__furniture.korean_name + '_' + product.product__color.korean_name,
#                 'price'      : product.product__price
#             } for product in products]    
            
#             # paginator    = Paginator(product_list, pagesize)
#             # product_list = paginator.page(page_number).object_list
#             # page_list    = list(paginator.page_range)

#             return JsonResponse({'message': 'SUCCESS', 'count': count, 'sub_category_list': sub_category_list, 'product_list': product_list}, status=200)
#         except Category.DoesNotExist:
#             return JsonResponse({'message': 'INVALID_CATEGORY'}, status=404)
#         except SubCategory.DoesNotExist:   
#             return JsonResponse({'message': 'INVALID_SUBCATEGORY'}, status=404)        
#         # except Paginator.EmptyPage:
#         #     return JsonResponse({'message': 'INVALID_PAGE'}, status=404)    

    # def get(self, request):
    #     category_id     = request.GET.get('category_id', None)
    #     sub_category_id = request.GET.get('sub_category_id', None)
    #     page_number     = request.GET.get('page', None)

    #     if int(category_id) in [c.id for c in Category.objects.all()] and int(sub_category_id) in [c.id for c in SubCategory.objects.all()]:
    #         if SubCategory.objects.get(id=sub_category_id).category == Category.objects.get(id=category_id):
    #             products = Product.objects.filter(Q(sub_category_id = sub_category_id) & Q(sub_category__category_id = category_id)) 
    #             product_list = [{
    #                 'id'         : product.id,
    #                 'image'      : product.thumbnail_image_url,
    #                 'brandName'  : product.furniture.brand.name,
    #                 'productName': product.furniture.korean_name + '_' + product.color.korean_name,
    #                 'price'      : product.price
    #             } for product in products]    

    #             try: 
    #                 paginator    = Paginator(product_list, 4)
    #                 product_list = paginator.page(page_number).object_list
    #                 page_list    = list(paginator.page_range)
    #                 return JsonResponse({'message': 'SUCCESS', 'product_list': product_list, 'page_list': page_list}, status=200)
    #             except :
    #                 return JsonResponse({'message': 'INVALID_PAGE'}, status=404)
    #         else:
    #             return JsonResponse({'message': 'DO_NOT_MATCH_CATEGORY'}, status=400)
    #     else:
    #         return JsonResponse({'message': 'INVALID_CATEGORY'}, status=404)

class ProductListView(View):
    def get(self, request):
        try:
            DEFAULT_LIMIT = 4
            DEFAULT_OFFSET = 0

            category_id     = request.GET.get('category_id', None)
            sub_category_id = request.GET.get('sub_category_id', None)
            limit           = int(request.GET.get('limit', DEFAULT_LIMIT))
            offset          = int(request.GET.get('offset', DEFAULT_OFFSET))
            sort_type       = int(request.GET.get('sort_type', 1))  
            
            sub_category_q = Q()

            product_q = Q()

            if category_id:
                category        = Category.objects.get(id = category_id)
                sub_category_q &= Q(category=category)
                product_q      &= Q(sub_category__category = category)

            if sub_category_id:
                sub_category    = SubCategory.objects.get(id = sub_category_id)
                sub_category_q &= Q(category=sub_category.category)
                product_q      &= Q(sub_category = sub_category)
            
            count = len(Product.objects.filter(product_q))

            #### count 값 줬으니까 예외처리는 하지말고 그냥 빈 리스트 반환할까... ###
            # if offset > count: 
            #     return JsonResponse({'message': 'INVALID_OFFSET'}, status=404)

            sub_category_list = [ sub_category.name for sub_category in SubCategory.objects.filter(sub_category_q) ]

            sort_set = { 
                1: 'id',
                2: 'furniture__updated_at',
                3: '-price',
                4: 'price',
            }

            sort_field = sort_set.get(sort_type, 'id')            
            products   = Product.objects.filter(product_q).order_by(sort_field)[offset:offset+limit]
            
            product_list = [{
                'id'         : product.id,
                'image'      : product.thumbnail_image_url,
                'brandName'  : product.furniture.brand.name,  
                'productName': product.furniture.korean_name + '_' + product.color.korean_name,
                'price'      : product.price
            } for product in products]                

            return JsonResponse({'message': 'SUCCESS', 'count': count, 'sub_category_list': sub_category_list, 'product_list': product_list}, status=200)
        except Category.DoesNotExist:
            return JsonResponse({'message': 'INVALID_CATEGORY'}, status=404)
        except SubCategory.DoesNotExist:   
            return JsonResponse({'message': 'INVALID_SUBCATEGORY'}, status=404)    

            
class ProductDetailView(View):
    '''
    목적: 사용자가 선택한 제품(product)의 상세정보를 보내준다.
    1. client가 보내온 데이터에서 제품아이디를 받아온다.
    2. 요청받은 product_id에 해당하는 상제 정보를 DB에서 찾는다.
    3. 찾은 데이터를 반환한다.
    '''

    def get(self, request, product_id):
        try:
            # data = json.loads(request.body)

            # product_id = data['product_id']
            product = Product.objects.get(id=product_id)
            
            # detail_images    = ProductImage.objects.filter(product_id = product_id)
            related_products = Product.objects.filter(furniture_id=product.furniture_id)
            # detail_image_list = []
            # for detail_image in detail_images:
            #     detail_image_list.append(detail_image.image_url)

            # description = [
            #     {
            #         "english_name": product.furniture.english_name + '_' + product.color.english_name,
            #         'name': product.furniture.korean_name + '_' + product.color.korean_name,
            #         'main_image': product.main_image_url,
            #         # 'detail_image': product.detail_image.all() # 쿼리셋으로 받아오고 for문 돌려서 각 이미지 받아오는 방식으로 해야한다
            #         'detail_image': [image.image_url for image in product.detail_image.all()],
            #         # 'detail_image': detail_image_list,
            #         'related_color_price': [related_product.color.english_name+'_'+str(int(related_product.price))+'원' for related_product in related_products]
            #     }]
            result = {
                    'english_name'         : product.furniture.english_name + '_' + product.color.english_name,
                    'korean_name'          : product.furniture.korean_name + '_' + product.color.korean_name,
                    'main_image'           : product.main_image_url,
                    'detail_image'         : [image.image_url for image in product.detail_image.all()],
                    'price'                : product.price,
                    'brand'                : product.furniture.brand.name,
                    'related_products_list': [{
                        'id'   : related_product.id,
                        'color': related_product.color.english_name,
                        'price': related_product.price
                    } for related_product in related_products]
                }

            # related_products = Product.objects.filter(furniture_id=product.furniture_id)

            # related_product_list = []
            # for related_product in related_products:
            #     related_product_list.append({
            #         'color': related_product.color.engilsh_name,
            #         'price': related_product.price
            #     })

            return JsonResponse({'result': result}, status=200)

            '''
            'description' : [
                {
                    "english_name": 'Puff Puff Sofa' + '_' + 'Red',
                    'name'        : '퍼프 퍼프 소파' + '_' + '레드',
                    'main_image'  : 'https://aaaaaa',
                    'detail_image': 'https://bbbbb',
                }],
            'related_products' : [
                {
                    'color' : '레드',
                    'price' : 1000000
                },
                {
                    'color' : '화이트',
                    'price' : 1100000
                },
                {
                    'color' : '블랙',
                    'price' : 1500000
                }
            ]
            '''

        # except KeyError:
        #     return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'INVALID_PRODUCT_ID'}, status=400)
        # except json.JSONDecodeError:
        #     return JsonResponse({'message': 'JSON_ERROR'}, status=400)




class ReviewView(View):
    
    def get(self, request, product_id):
    
        result = [{
            'review_id' : review.id,
            'user_first_name' : review.user.first_name,
            'user_last_name' : review.user.last_name,
            'content'   : review.content,
            'created_at': review.created_at,
            'updated_at': review.updated_at
        } for review in Review.objects.filter(product_id=product_id)]
    
        return JsonResponse({'result':result}, status=200)

    @login_confirm
    def post(self, request, product_id):
        try:
            data    = json.loads(request.body)

            Review.objects.create(
                user    = request.user,
                product = Product.objects.get(id=product_id),
                content = data["content"])

            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        
        except Product.DoesNotExist:
            return JsonResponse({"MESSAGE":"PRODUCT_DOES_NOT_EXIST"}, status=400)