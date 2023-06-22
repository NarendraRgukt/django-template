from django.shortcuts import render
from .models import Restaurant

from django.db.models import Q



def search_items(dictionary, search_text,restaurant):
    '''Function that returns list of items which matches the query text'''
    matching_items = []                                #all the items which matches the query will be stored in the matching items
    for key, value in dictionary.items():              #comparing the query is in key of dictionary and then append it to the matching_items
        if search_text.lower() in key.lower():
            matching_items.append((key, value,restaurant))
    return matching_items


def search(request):
    query = request.GET.get('query')                    #for getting the text in the searchbar
    if query:
        restaurants = Restaurant.objects.filter(
            Q(items__icontains=query) | Q(name__icontains=query)).order_by('name')#searching the database name and items fields using query
        item_list=[]
        for restaurant in restaurants:
            restaurant_items=restaurant.get_items()       #getting the list of items of particular restaurant in dictionary format
            

            items=search_items(restaurant_items,query,restaurant)    #calling the function for searching the items in the items field which matches the query
            item_list += items                            #concatenating all the restaurant items into item_list
            
            
        

            



    else:
        restaurants = []
        item_list=[]
    context = { 'restaurants': restaurants, 'items': item_list}
    return render(request, 'searchapp/search.html', context)





