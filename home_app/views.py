from django.shortcuts import render,redirect
from django.contrib import messages
from home_app.models import Main_page
from basic_app.models import food_diary,Temporary,Transaction_det,Unsaved,Temporary_purchase, Unsaved_purchase, Purchase_det
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import messages
from datetime import datetime,date
import datetime as dt
from django.urls import reverse
import mysql.connector as msql
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import seaborn as sns
from django.db.models import Sum
import matplotlib.pyplot as plt1
from FoodIndex.models import *
from FoodIndex.update import *



# Create your views here.
email_id=''
quant = {}
items = food_diary.objects.all()
z=0
x=0
y=0
w=0
for i in items:
    quant[i.food_name]=0


def home(request):
    global email_id
    if request.method=="POST":
        email = request.POST['email']
        pwd = request.POST['pwd']
        email_id=email
        mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
        cursor = mydb.cursor()
        query = "SELECT*FROM FoodIndex_userdata"
        db = pd.read_sql(query, mydb)
        emails = list(db['Email'])
        pwds = list(db['Password'])

        user_dict = dict(zip(emails, pwds))

        global w
        w=w+1
        if w==1:
            try:
                unsav = Unsaved.objects.all()
                tod = datetime.date(datetime.now())
                for i in unsav:
                    if(i.email_id==email):
                        entry = Temporary(
                            food_name = i.food_name,
                            calories = i.calories,
                            quantity = i.quantity,
                            meal_type = i.meal_type)
                        entry.save()
                        i.delete() 
                uns = Unsaved_purchase.objects.all()
                for j in uns:
                    if(j.email_id == email):    
                        ent = Temporary_purchase(
                            mfg_code=j.mfg_code,
                            food_id=j.food_id,
                            food_name = j.food_name,
                            calories = j.calories,
                            quantity = j.quantity,
                            protein=j.protein,
                            carbohydrates=j.carbohydrates,
                            fats=j.fats)
                        ent.save()
                           
                    else:
                        continue  
            except Unsaved.DoesNotExist:
                item = none

        if email not in emails:
            messages.error(request, "No User Found!")
            return redirect('/')
        else:
            if user_dict[email] == pwd:
                allTypes=Main_page.objects.all()
                con={'allTypes':allTypes}
                return render(request,'home.html',con)
            else:
                messages.error(request, "Incorrect Password")
                return redirect('/')
    else:

        return render(request,'home.html')
'''def renderhome(request):
    return render(request,'home.html')'''

def details(request,f_name):
    item = food_diary.objects.all()
    return render(request,'details.html',{'info': item,'food_name': f_name })

def add_item1(request):
    if request.method=="POST":
        meal = request.POST["meal_type"]
        f_name = request.POST["selectedItem"]
        qnt = request.POST["selectedQuant"]
        item = food_diary.objects.get(food_name = f_name) 
        cal = item.calories
        cal=int(cal)
        num = int(qnt)
        new_entry = Temporary(
                food_name = f_name,
                calories = cal*num,
                quantity = qnt,
                meal_type = meal
            )
        new_entry.save()
        return redirect('/table')

    
        
      



def table(request):
    try:
        item = Temporary.objects.all()
    except Temporary.DoesNotExist:
        item = none

    return render(request,'table.html',{'info':item})

def purchase(request):
    try:
        item = Temporary_purchase.objects.all()
    except Temporary_purchase.DoesNotExist:
        item = none

    return render(request,'purchase.html',{'info':item})


def confirm_purchase(request):
    if request.method == "POST":
        f_name = request.POST["selectedItem2"]
        qnt = request.POST["selectedQuant"]
        item = food_diary.objects.get(food_name = f_name) 
        cal = item.calories
        protin = item.protein
        carbs = item.carbohydrates
        f = item.fats
        num = int(qnt)
        new_entry = Temporary_purchase(
                mfg_code=item.mfg_code,
                food_name = f_name,
                food_id=item.food_id,
                calories = cal*num,
                quantity = qnt,
                protein=num*protin,
                carbohydrates=num*carbs,
                fats=num*f)
                
        new_entry.save()   
        try:
            item = Temporary_purchase.objects.all()
        except Temporary_purchase.DoesNotExist:
            item = none

        return render(request,'purchase.html',{'info':item})

def confirm_purchase2(request):
        if request.method == "POST":
            f_name = request.POST["selectedItem"]
            m = request.POST["mfg"]
            f_id = request.POST["fd_id"]
            calo = request.POST["cal"]
            f = request.POST["fat"]
            p = request.POST["protin"]
            c = request.POST["carbs"]
            qnt = request.POST["quantity"]
            calo=int(calo)
            f=int(f)
            c=int(c)
            p=int(p)
            qnt=int(qnt)
            new_entry = Temporary_purchase(
                    mfg_code=m,
                    food_name = f_name,
                    food_id=f_id,
                    calories = calo*qnt,
                    quantity = qnt,
                    protein=p*qnt,
                    carbohydrates=c*qnt,
                    fats=f*qnt)
                    
            new_entry.save()   
            try:
                item = Temporary_purchase.objects.all()
            except Temporary_purchase.DoesNotExist:
                item = none

            return redirect('/purchase')



def delete(request,f_name):
    email = email_id
    instance = Temporary.objects.get(food_name = f_name)
    instance.delete()
    unsav = Unsaved.objects.all()
    tod = datetime.date(datetime.now())
    for i in unsav:
        if(i.email_id==email and i.date==tod and i.food_name == f_name):
            i.delete()
    quant[f_name] = 0
    try:
        item = Temporary.objects.all()
        return redirect('/table')
    except Temporary.DoesNotExist:
         return redirect('/home')

def delete_purchase(request,f_id):
    email = email_id
    f_id=int(f_id)
    instance = Temporary_purchase.objects.get(food_id = f_id)
    instance.delete()
    unsav = Unsaved_purchase.objects.all()
    tod = datetime.date(datetime.now())
    
    for i in unsav:
        if(i.email_id==email and i.food_id == f_id):
            i.delete()
   
    try:
        item = Temporary_purchase.objects.all()
        return redirect('/purchase')
    except Temporary_purchase.DoesNotExist:
         return redirect('/home')
    


def save_table(request):
    email = email_id
    try:
        item = Temporary.objects.all()
   
        for i in item:
            #nutrition = food_diary.objects.get(food_name = i.food_name)

            entry = Transaction_det(
                email_id = email,
                date = datetime.date(datetime.now()),
                food_name = i.food_name,
                calories = i.calories,
                quantity = i.quantity,
                meal_type = i.meal_type,
                #protein=nutrition.protein,
                #carbohydrates=nutrition.carbohydrates,
                #fats=nutrition.fats
            )
            entry.save()
            Temporary.objects.all().delete()
            unsav = Unsaved.objects.all()
            tod = datetime.date(datetime.now())
            for i in unsav:
                if(i.email_id==email and i.date==tod):
                    i.delete()
        return redirect('/home')

    except Transaction_det.DoesNotExist:
        return redirect('/home')

def save_purchase(request):
    email = email_id
    try:
        item = Temporary_purchase.objects.all()
   
        for i in item:

            entry = Purchase_det(
                mfg_code=i.mfg_code,
                food_id=i.food_id,
                email_id = email,
                date = datetime.date(datetime.now()),
                food_name = i.food_name,
                calories = i.calories,
                quantity = i.quantity,
                protein=i.protein,
                carbohydrates=i.carbohydrates,
                fats=i.fats
            )
            entry.save()
            Temporary_purchase.objects.all().delete()
            unsav = Unsaved_purchase.objects.all()
            tod = datetime.date(datetime.now())
            for i in unsav:
                if(i.email_id==email and i.date==tod):
                    i.delete()
        return redirect('/home')

    except Transaction_det.DoesNotExist:
        return redirect('/home')

def deletetemp(request):
    global w
    try:
        email = email_id
        items = Temporary.objects.all()
        for i in items:
            quant[i.food_name]=0
            entry = Unsaved(
                email_id = email,
                date = datetime.date(datetime.now()),
                food_name = i.food_name,
                calories = i.calories,
                quantity = i.quantity,
                meal_type = i.meal_type)
                
            entry.save()

        it = Temporary_purchase.objects.all()
      
        for j in it:
            entry = Unsaved_purchase(
                mfg_code=j.mfg_code,
                food_id=j.food_id,
                email_id = email,
                date = datetime.date(datetime.now()),
                food_name = j.food_name,
                calories = j.calories,
                quantity = j.quantity,
                protein=j.protein,
                carbohydrates=j.carbohydrates,
                fats=j.fats)
                
            entry.save()
        w=0   
        Temporary.objects.all().delete()
        Temporary_purchase.objects.all().delete()
        return HttpResponseRedirect('/')
    except Temporary.DoesNotExist:
        w=0
        return HttpResponseRedirect('/')

def calories(request):
    if request.method == 'POST':
        var1=float(request.POST['weigh'])
        var2=float(request.POST['gen'])
        var3=float(request.POST['level'])
        mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
        cur = mydb.cursor()
        cur.execute("SELECT * FROM basic_app_transaction_det")
        sql_data = pd.DataFrame(cur.fetchall())
        sql_data.columns=['id','email_id','date','food_name','calories','quantity','meal_type']
        df=pd.DataFrame()
        df=sql_data
        df.to_csv("foodcaloriesflask.csv")
        dfn=pd.read_csv('foodcaloriesflask.csv')
        dfn.drop('Unnamed: 0',axis=1,inplace=True)

        todays='2021-04-09'
        dfx=dfn[dfn['date']==todays]
       
        sumx=np.sum(dfx['calories'])
        x=''
        dataa=''
        
        calculated=var1*24*var2*0.93*var3
        global val
        def val():
            return calculated
        
        bic={'calculated':calculated,'consumed':sumx}
        return render(request,"calories.html",bic)
    return render(request,"calories.html")

def chart(request):
    mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
    cur = mydb.cursor()
    cur.execute("SELECT * FROM basic_app_transaction_det")
    filedata = pd.DataFrame(cur.fetchall())
    
    filedata.columns=['id','email_id','date','food_name','calories','quantity','meal_type']
    dfn=filedata
    if request.method == 'POST':
        meal=str(request.POST['gens'])
        charts=str(request.POST['charts'])
        today = date.today()
        email = email_id
        dfn=dfn[dfn['email_id']==email]
        dfn=dfn[dfn['date']==today]
        if charts == 'calories':
            if meal=='all':
                dfx=dfn
            else:
                dfx=dfn[dfn['meal_type']==meal]
            
            x='food_name'
            dfx.plot(x, y="calories", kind="bar",figsize=(100,30) ,fontsize=80)
            #plotss = sns.barplot(x,y,data=dfx)
            plt.legend(prop={'size': 80},loc='center left', bbox_to_anchor=(1, 0.5))
            plt.xticks(rotation ='horizontal',fontsize=80)
            plt.savefig('media/graph/brxxxy.png')
        else:
            if meal=='all':
                dfx=dfn
            else:
                dfx=dfn[dfn['meal_type']==meal]
            protein=[]
            carbs=[]
            fats=[]
            for i in dfx['food_name']:
                nutrition = food_diary.objects.get(food_name = i)
                protein.append(nutrition.protein)
                fats.append(nutrition.fats)
                carbs.append(nutrition.carbohydrates)
            dfx['protein']=protein
            dfx['fats']=fats
            dfx['carbs']=carbs
            x='food_name'
            dfx.plot(x, y=["protein","carbs", "fats"], kind="bar",figsize=(100,20) ,fontsize=70)
            
            plt.legend(prop={'size': 80},loc='center left', bbox_to_anchor=(1, 0.5))
            plt.xticks(rotation ='horizontal',fontsize=80)
            plt.savefig('media/graph/brxxxy.png')
        
        return render(request,'chart.html')
    else:
        return render(request,'chart.html')





def calchartthree(request):
    mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
    cur = mydb.cursor()
    cur.execute("SELECT * FROM basic_app_transaction_det")
    filedata = pd.DataFrame(cur.fetchall())
    filedata.columns=['id','email_id','date','food_name','calories','quantity','meal_type']
    dfn=filedata
    if request.method == 'POST':
        numbr=int(request.POST['genx'])
        listdate=[]
        calx=[]
        today=date.today()
        for i in range(numbr):
            e = dt.timedelta(days = i)
            e=today-e
            listdate.append(e)
        
        for i in listdate:
            dfxx=dfn[dfn['date']==i]
            cal=np.sum(dfxx['calories'])
            calx.append(cal)
        
        width_in_inches = 10
        height_in_inches = 8

        plt.figure(figsize=(width_in_inches, height_in_inches))
        plt.plot(listdate,calx, linestyle="--")
        plt.scatter(listdate,calx)
        plt.xticks(rotation ='vertical',fontsize= 18)
        plt.yticks(label ='calories',fontsize= 18)
        plt.ylabel('calories', fontsize=30)
        plt.savefig('media/barchartcalthreee.png')
    
    return render(request,'calchartthreey.html')
    


def homex(request):
    
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render('homex.html', data)

    
def profile_page(request):
    email_id = request.session['email']
    instance = UserData.objects.get(Email = email_id)
    f_name = instance.FirstName
    l_name = instance.LastName
    name = f_name + ' ' + l_name
    phno = instance.PhoneNo
    age = instance.Age
    weight = instance.Weight
    gender=instance.Gender
    return render(request,'profile_page.html',{'name':name,'email':email_id,'phno':phno,'age':age,'weight':weight,'gender':gender})
    

    
