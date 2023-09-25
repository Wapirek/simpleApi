from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['Get'])
def getDate(request):
    fajne_dane = {'lucz':'wartosc','liczba':48}
    return Response(fajne_dane)