from django.shortcuts import render

# Create your views here.
def home(requests):
    context = {
        'cart_entries': [
            {
                'title': 'GOOD BOOKS!',
                'body': 'I have created my first template in Django!',


            },
            {
                'title': 'ITEMS',
                'body': 'LalalaLand',

            },
            {
                'title': 'ANOTHER ONE!!',
                'body': 'MAYBE?',

            },  {
                'title': 'SOMETHING !!',
                'body': 'Am i doing it right?',

            }, {
                'title': 'ELSE!!',
                'body': 'Am i doing it right?',

            }
        ]
    }

    return render(requests, 'home.html', context)



def products(requests):
    return render(requests, "products.html")