from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Notebook
from .serializers import NotebookSerializer
# Create your views here.


# @api_view(["GET"])
# def notebook_list(request):
#     notebooks = Notebook.objects.all()
#     serializer = NotebookSerializer(notebooks, many = True)
#     return Response(serializer.data)

# @api_view(["POST"])
# def notebook_create(request):
#     serializer = NotebookSerializer(data = request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)

# @api_view(["GET"])
# def notebook_detail(request, pk):
#     notebook = get_object_or_404(Notebook, pk = pk)
#     serializer = NotebookSerializer(notebook)
#     return Response(serializer.data)

# @api_view(["PATCH"])
# def notebook_partial_update(request, pk):
#     notebook = get_object_or_404(Notebook, pk = pk)
#     serializer = NotebookSerializer(data = request.data, instance = notebook, partial = True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)

# @api_view(["PUT"])
# def notebook_update(request, pk):
#     notebook = get_object_or_404(Notebook, pk = pk)
#     serializer = NotebookSerializer(data = request.data, instance = notebook)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)

# @api_view(["DELETE"])
# def notebook_detail(request, pk):
#     notebook = get_object_or_404(Notebook, pk = pk)
#     notebook.delete()
#     return Response({"message": "O'chirildi"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def notebook_list(request):
    notebooks = Notebook.objects.all()
    data = []
    for notebook in notebooks:
        data.append({
            "id":notebook.id, 
            "brand":notebook.brand,
            "model":notebook.model,
            "year": notebook.year,
            "price":notebook.price,
            "color": notebook.color
        })
    return Response({
        "status":status.HTTP_200_OK,
        "message": "Barcha notebooklar",
        "data":data
        })

@api_view(["POST"])
def notebook_create(request):
    brand = request.data.get("brand")
    model = request.data.get("model")
    year = request.data.get("year")
    price = request.data.get("price")
    color = request.data.get("color")
    created_notebook = Notebook.objects.create(brand=brand, model=model, year=year, price=price, color=color)

    # notebook = Notebook(brand=brand, model=model, year=year, price=price, color=color)
    # notebook.save()
    
    data = {
            "id":created_notebook.id, 
            "brand":created_notebook.brand,
            "model":created_notebook.model,
            "year": created_notebook.year,
            "price":created_notebook.price,
            "color": created_notebook.color
    }
    return Response({
        "status":status.HTTP_201_CREATED,
        "message": "Yaratildi",
        "data":data
        })
    
@api_view(["GET"])
def notebook_detail(request, pk):
    notebook = get_object_or_404(Notebook, pk = pk)
    data = {
            "id":notebook.id, 
            "brand":notebook.brand,
            "model":notebook.model,
            "year": notebook.year,
            "price":notebook.price,
            "color": notebook.color
            }
    return Response({
        "status":status.HTTP_200_OK,
        "message":f"{notebook.id}-IDli notebookning barcha ma'lumotlari",
        "data":data
        })

@api_view(["PUT"])
def notebook_update(request, pk):
    notebook = get_object_or_404(Notebook, pk = pk)
    notebook.brand = request.data.get("brand")
    notebook.model = request.data.get("model")
    notebook.year = request.data.get("year")
    notebook.price = request.data.get("price")
    notebook.color = request.data.get("color")
    notebook.save()
    data = {
            "id":notebook.id, 
            "brand":notebook.brand,
            "model":notebook.model,
            "year": notebook.year,
            "price":notebook.price,
            "color": notebook.color
            }
    return Response({
        "status":status.HTTP_202_ACCEPTED,
        "message":f"{notebook.id}-IDli notebookning ma'lumotlari uzgardi",
        "data":data
        })

@api_view(["PATCH"])
def notebook_partial_update(request, pk):
    notebook = get_object_or_404(Notebook, pk = pk)
    if "brand" in request.data:
        notebook.brand = request.data.get("brand")
    if "model" in request.data:
        notebook.model = request.data.get("model")
    if "year" in request.data:
        notebook.year = request.data.get("year")
    if "price" in request.data:
        notebook.price = request.data.get("price")
    if "color" in request.data:
        notebook.color = request.data.get("color")

    notebook.save()
    data = {
            "id":notebook.id, 
            "brand":notebook.brand,
            "model":notebook.model,
            "year": notebook.year,
            "price":notebook.price,
            "color": notebook.color
            }
    return Response({
        "status":status.HTTP_202_ACCEPTED,
        "message":f"{notebook.id}-IDli notebookning ma'lumotlari uzgardi",
        "data":data
        })
    
@api_view(["DELETE"])
def notebook_delete(request, pk):
    notebook = get_object_or_404(Notebook, pk = pk)
    data = {
            "id":notebook.id, 
            "brand":notebook.brand,
            "model":notebook.model,
            "year": notebook.year,
            "price":notebook.price,
            "color": notebook.color
            }
    notebook.delete()
    return Response({
        "status":status.HTTP_204_NO_CONTENT,
        "message":f"{data['id']}-IDli notebook o'chirildi",
        "data":data
        })


@api_view(["GET", "POST"])
def notebook_list_create_view(request):
    if request.method == "GET":
        notebooks = Notebook.objects.all()
        data = []
        for notebook in notebooks:
            data.append({
                "id":notebook.id, 
                "brand":notebook.brand,
                "model":notebook.model,
                "year": notebook.year,
                "price":notebook.price,
                "color": notebook.color
            })
        return Response({
            "status":status.HTTP_200_OK,
            "message": "Barcha notebooklar",
            "data":data
            })
    if request.method == "POST":
        brand = request.data.get("brand")
        model = request.data.get("model")
        year = request.data.get("year")
        price = request.data.get("price")
        color = request.data.get("color")
        created_notebook = Notebook.objects.create(brand=brand, model=model, year=year, price=price, color=color)

        # notebook = Notebook(brand=brand, model=model, year=year, price=price, color=color)
        # notebook.save()
        
        data = {
                "id":created_notebook.id, 
                "brand":created_notebook.brand,
                "model":created_notebook.model,
                "year": created_notebook.year,
                "price":created_notebook.price,
                "color": created_notebook.color
        }
        return Response({
            "status":status.HTTP_201_CREATED,
            "message": "Yaratildi",
            "data":data
            })



@api_view(["GET", "PUT", "PATCH", "DELETE"])
def notebook_detail_update_delete_view(request, pk):
    
    if request.method == "GET":
        notebook = get_object_or_404(Notebook, pk = pk)
        data = {
            "id":notebook.id, 
            "brand":notebook.brand,
            "model":notebook.model,
            "year": notebook.year,
            "price":notebook.price,
            "color": notebook.color
            }
        return Response({
            "status":status.HTTP_200_OK,
            "message":f"{notebook.id}-IDli notebookning barcha ma'lumotlari",
            "data":data
            })
    
    if request.method == "PUT":
        notebook = get_object_or_404(Notebook, pk = pk)
        notebook.brand = request.data.get("brand")
        notebook.model = request.data.get("model")
        notebook.year = request.data.get("year")
        notebook.price = request.data.get("price")
        notebook.color = request.data.get("color")
        notebook.save()
        data = {
                "id":notebook.id, 
                "brand":notebook.brand,
                "model":notebook.model,
                "year": notebook.year,
                "price":notebook.price,
                "color": notebook.color
                }
        return Response({
            "status":status.HTTP_202_ACCEPTED,
            "message":f"{notebook.id}-IDli notebookning ma'lumotlari uzgardi",
            "data":data
            })

    if request.method == "PATCH":
        notebook = get_object_or_404(Notebook, pk = pk)
        if "brand" in request.data:
            notebook.brand = request.data.get("brand")
        if "model" in request.data:
            notebook.model = request.data.get("model")
        if "year" in request.data:
            notebook.year = request.data.get("year")
        if "price" in request.data:
            notebook.price = request.data.get("price")
        if "color" in request.data:
            notebook.color = request.data.get("color")

        notebook.save()
        data = {
                "id":notebook.id, 
                "brand":notebook.brand,
                "model":notebook.model,
                "year": notebook.year,
                "price":notebook.price,
                "color": notebook.color
                }
        return Response({
            "status":status.HTTP_202_ACCEPTED,
            "message":f"{notebook.id}-IDli notebookning ma'lumotlari uzgardi",
            "data":data
            })

    if request.method == "DELETE":
        notebook = get_object_or_404(Notebook, pk = pk)
        data = {
                "id":notebook.id, 
                "brand":notebook.brand,
                "model":notebook.model,
                "year": notebook.year,
                "price":notebook.price,
                "color": notebook.color
                }
        notebook.delete()
        return Response({
            "status":status.HTTP_204_NO_CONTENT,
            "message":f"{data['id']}-IDli notebook o'chirildi",
            "data":data
            })




