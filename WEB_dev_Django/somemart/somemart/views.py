import base64
import json

from django.http import JsonResponse, HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views import View

from jsonschema import validate
from jsonschema import ValidationError

from .models import Item, Review
#
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .schemas import ITEMS_SCHEMA, REVIEW_SCHEMA


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        try:
            # BASE, AUTH, USER
            if request.META['HTTP_AUTHORIZATION'].split(' ')[0] == 'Basic':
                auth = base64.b64decode(request.META['HTTP_AUTHORIZATION'].split(' ')[1]).decode("UTF-8").split(':')
                user = authenticate(username=auth[0], password=auth[1])
                # print(type(user))
                if user is None:
                    return HttpResponse(status=401)
                elif user.is_staff != 1:
                    return HttpResponse(status=403)
            else:
                return HttpResponse(status=403)
            # clean = Item.objects.all()
            # clean[0].delete()
            document = json.loads(request.body)
            # if document["description"] == "":
            #     return HttpResponse(status=400)
            validate(document, ITEMS_SCHEMA)
            item = Item(title=document["title"], description=document["description"], price=document["price"])
            # item.id = 1
            item.save()
            return JsonResponse({"id": item.pk}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'error': exc.message}, status=400)
        except KeyError:
            return HttpResponse(status=401)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        # Почему нужно только так, а не как нижеы
        try:
            item = Item.objects.get(pk=item_id)
        except:
            return HttpResponse(status=404)

        try:
            # clean = Review.objects.all()
            # clean[0].delete()
            data = json.loads(request.body)
            validate(data, REVIEW_SCHEMA)
            rewiev = Review(item_id=item_id, grade=data["grade"], text=data["text"])
            print(rewiev)
            # rewiev.id = 1
            rewiev.save()
            return JsonResponse({"id": rewiev.pk}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'error': exc.message}, status=400)
        # except:
        #     return HttpResponse(status=404)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        try:
            need_item = Item.objects.get(pk=item_id)

            need_rewievs_set = list(Review.objects.filter(item=item_id).order_by('-pk')[:5])
            print(need_rewievs_set)
            data = {
                "id": item_id,
                "title": f"{need_item.title}",
                "description": f"{need_item.description}",
                "price": need_item.price,
                "reviews": [
                    {
                        "id": rewiew.pk,
                        "text": rewiew.text,
                        "grade": rewiew.grade

                    } for rewiew in need_rewievs_set
                ]
            }
            return JsonResponse(data, status=200)
        except:
            return HttpResponse(status=404)
