from django.shortcuts import render
# from .csv_data_save import csv_data_to_sqlite
from .models import Restaurant
# Create your views here.


def dish_lists():
    all_data = Restaurant.objects.all()
    dish_set = set()
    for data in all_data:
        for item in data.items:
            dish_set.add(item)
    dish_list=list(dish_set)
    return dish_list

def matched_dishes(dish):
    matched_list=[]
    dish_list=dish_lists()
    for item in dish_list:
        if dish.lower() in item.lower():
            matched_list.append(item)
    return matched_list

def restaurant_id_dish_matched(dish):
    matched_list=matched_dishes(dish)
    all_data = Restaurant.objects.all()
    matched_restaurants=[]
    for item in matched_list:
        for data in all_data:
            if item in data.items:
                matched_restaurants.append([data,item])
    return matched_restaurants

def get_restaurant_data(dish):
    details=restaurant_id_dish_matched(dish)
    context = []
    for data in details:
        data_dict = {
            'item': data[1],
            'price': data[0].items[data[1]],
            'id': data[0].id,
            'name': data[0].name,
            'location': data[0].location,
            'address': data[0].address,
                }
        context.append(data_dict)
    return context
        
def home(request):
    # csv_data_to_sqlite()
    if request.method == 'POST':
        dish = request.POST['dish']
        data = get_restaurant_data(dish)
        dish_list = matched_dishes(dish)
        context={'all_data':data,'dish_list':dish_list ,'user_input' : dish}
        return render(request, 'home.html', context)
    # data=get_restaurant_data('idli')
    return render(request, 'home.html')

def filter_dish(request):
    if request.method == 'POST':
        dish = request.POST['filter_dish']
        data = get_restaurant_data(dish)
        dish_list = matched_dishes(dish)
        context={'all_data':data,'dish_list':dish_list ,'user_input' : dish}
        return render(request, 'home.html', context)
    return render(request, 'home.html')