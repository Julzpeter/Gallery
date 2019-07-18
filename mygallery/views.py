from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
# Create your views here.
def welcome(request):
        html = f'''
        <html>
            <body>
                <h1>Welcome to My Gallery</h1>
            </body>
        </html>
            '''
        return render('html')

       



    
    
