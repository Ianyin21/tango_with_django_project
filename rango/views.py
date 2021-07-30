from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page, UserProfile
# Create your views here.
def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)
# return HttpResponse("Rango says hey there partner! <a href='/rango/about>About</a>")


def about(request):
    context = RequestContext(request)
    if 'visits' in request.session:
        visits = request.session['visits']
    else:
        visits = 0
    return render_to_response('rango/about.html', {'visits': visits}, context)
    # return HttpResponse("Rango says here is the about page. <a href='/rango/>Index</a>")

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() returns a list of page objects or an empty list
        pages = Page.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.        
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None


    # create a default query based on the category name
    # to be shown in the search box
    context_dict['query'] = category.name

    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Webhose function to get the results list!
            result_list = run_query(query)
            context_dict['query'] = query
    context_dict['result_list'] = result_list


    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)