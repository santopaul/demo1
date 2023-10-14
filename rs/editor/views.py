from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import people_about,home_portfolio_status,home_portfolio_work,portfolio_status,portfolio_work
# Create your views here.
def home(request):
    status=home_portfolio_status.objects.all()
    status=home_portfolio_work.objects.all()
    """
    { 
        'home_portfolio_status':[
    {
        'det_date':'July 25, 2023.',
        'anytext': '',
        'category':'House For Sale!',
        'place':'Near Thirumala', 
        'img_vid': True, #Img or video selector true if it's video
        'img':'',
        'vid': 'a.mp4',
    },
    {
        'det_date':'July 25, 2023.',
        'anytext': '',
        'category':'House For Sale!',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video 
        'img':'blog6.jpg',       
        'vid': '',
    },     
    {
        'det_date':'July 25, 2023.',
        'anytext': '',
        'category':'House For Sale!',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video 
        'img':'blog3.jpg',       
        'vid': '',
    },     
    {
        'det_date':'July 25, 2023.',
        'anytext': '',
        'category':'House For Sale!',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video 
        'img':'blog3.jpg',       
        'vid': '',
    },     
    {
        'det_date':'July 25, 2023.',
        'anytext': '',
        'category':'House For Sale!',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video 
        'img':'blog6.jpg',       
        'vid': '',
    },     
    {
        'det_date':'July 25, 2023.',
        'anytext': '',
        'category':'House For Sale!',
        'place':'Near Thirumala',  
        'img_vid': True, #Img or video selector true if it's video
        'img':'',       
        'vid': 'a.mp4',
    },     
    ],
       'home_portfolio_work':[
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p1.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p2.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p3.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p4.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p2.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p1.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p4.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p3.jpg',
            'vid': '',
        },
        ], }
        """
    return render(request,'index.html',{'home_portfolio_status':status},{'home_portfolio_work':status})

def portfolio(request):
    status=status=portfolio_status.objects.all()
    status=status=portfolio_work.objects.all()
    """
    { 
        'portfolio_status':[
    {
        'title':'Project1',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available':True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b1.jpg',
        'vid': '',
    },     
    {
            'title':'Project2',
        'status':'notCompleted',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available':True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b9.jpg',
        'vid': '', 
   },
    {
            'title':'Project3',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available':True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b10.jpg',
        'vid': '',
   },
    {
            'title':'Project4',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available':True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b11.jpg',
        'vid': '',
   },
    {
            'title':'Project5',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available':True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b4.jpg',
        'vid': '',
   },
    {
            'title':'Project6',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b3.jpg',
        'vid': '',
   },
    {
            'title':'Project7',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': False,
        'category':'Sold !',
        'portfolio_id':'portfolio0',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b2.jpg',
        'vid': '', 
   },
    {
            'title':'Project8',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': False,
        'category':'Sold !',
        'portfolio_id':'portfolio0',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b5.jpg',
        'vid': '', 
   },
    {
            'title':'Project9',
        'status':'heheCompleted',
        'price':'60 Lakeds',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': False,
        'category':'Sold !',
        'portfolio_id':'portfolio0',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b7.jpg',
        'vid': '',   
   },
    {
            'title':'Project10',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': False,
        'category':'Sold !',
        'portfolio_id':'portfolio0',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b2.jpg',
        'vid': '', 
   },
    {
            'title':'Project11',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': False,
        'category':'Not For Sale',
        'portfolio_id':'portfolio0',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b5.jpg',
        'vid': '', 
   },
    {
            'title':'Project13',
        'status':'heheCompleted',
        'price':'60 Lakeds',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': False,
        'category':'Not For Sale',
        'portfolio_id':'portfolio0',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b7.jpg',
        'vid': '',  
   },
    {
            'title':'Project4',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available':True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b11.jpg',
        'vid': '',
   },
    {
            'title':'Project5',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available':True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b4.jpg',
        'vid': '',
   },
    {
            'title':'Project6',
        'status':'Completed',
        'price':'60 Lakhs',
        'date':'July 25.',
        'det_date':'July 25, 2023.',
        'available': True,
        'category':'House For Sale!',
        'portfolio_id':'portfolio1',
        'place':'Near Thirumala', 
        'img_vid': False, #Img or video selector true if it's video
        'img':'b3.jpg',
        'vid': 'a.mp4',
   },
    ],
        'portfolio_work':[
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p1.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p2.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p3.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p4.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p2.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p1.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p4.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p3.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p1.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p2.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p3.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p4.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p2.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p1.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p4.jpg',
            'vid': '',
        },
        {   'title': 'Campus project.',
            'status': 'Ongoing.',
            'amount': '70 Lakhs Estd.',
            'time': '6 Months.', 
            'img_vid': False, #Img or video selector true if it's video
            'img':'p1.jpg',
            'vid': 'a.mp4',
        },
        ]}
        """
    return render(request,'portfolio.html',{'portfolio_status':status},{'portfolio_work':status})

def about(request):
    about=people_about.objects.all()
    return render(request,'about.html',{'people_about':about})

def services(request):
    return render(request,'services.html')

def license(request):
    return render(request,'license.html')

def contact(request):
    return render(request,'contact.html')

def error(request):
    return render(request,'404.html')

