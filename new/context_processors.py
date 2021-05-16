from basic_app.models import Temporary,Temporary_purchase,Unsaved_purchase,Unsaved


def notify(request):
    items_left = Temporary.objects.all().count()  
    purchase_left = Temporary_purchase.objects.all().count()          
    return {'items_left': items_left,'purchase_left':purchase_left}