from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from FoodIndex.models import *
from home_app.models import *
from basic_app.models import *
import requests
import pandas as pd
import csv
from sqlalchemy import create_engine
import mysql.connector as msql
import openpyxl, pymysql
import numpy as np
from basic_app.update import *
from FoodIndex.update import *
# Create your views here.

def upload_csv(request):    
    if request.method == "POST":
        mail = request.POST['mail']  
        pwd = request.POST['pass']
        #engine = create_engine("mysql+pymysql://{user}:{password}@15.207.8.17/{db}".format(user="Food", password="zhTnxpRFiSzpaF2J", db="Food"))
        
        mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
        table =  "SELECT*FROM admin_data"
        df = pd.read_sql(table, mydb)
        mails = list(df['Email_ID'])
        pwds = list(df['Password'])
        admins = dict(zip(mails, pwds))
        if mail not in mails:
            messages.error(request, "Email not registered as ADMIN. Use an Email registered as ADMIN.")
            return redirect("/alreadyuser")
        else:
            if admins[mail] == pwd:
                return render(request, 'upload_file.html')
            else:
                messages.error(request, "Incorrect Password.")
                return redirect("/alreadyuser")
    
def file_to_db(request):
    if request.method == "POST":
        #READING THE INPUT CSV FILE FROM DATABASE
        files = request.FILES["filename"]
        df = pd.read_csv(files, encoding='unicode-escape')

        myconn = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J")
        concursor = myconn.cursor()
        concursor.execute("CREATE DATABASE IF NOT exists Food")
        mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
        cursor = mydb.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS basic_app_food_diary(mfg_code VARCHAR(10), food_id VARCHAR(10), food_name VARCHAR(50), description VARCHAR(200), food_type VARCHAR(200), calories VARCHAR(10),fats VARCHAR(10), protein VARCHAR(10), carbohydrates VARCHAR(10), link_of_image VARCHAR(1000), link_of_recipie VARCHAR(1000), purchasing_link VARCHAR(1000))")
        engine = create_engine("mysql+pymysql://{user}:{password}@15.207.8.17/{db}".format(user="Food", password="zhTnxpRFiSzpaF2J", db="Food"))
        
        df.to_sql("basic_app_food_diary", con = engine, if_exists = 'append', chunksize = 1000, index=False)

        messages.success(request, "File Uploaded Successfully.")
        return redirect("/upload_csv_")
    
    return redirect("/upload_csv_")

def getdata(request):
    if request.method == 'POST':
        mfgcode = request.POST['mfgcode']
        food_id = request.POST['foodid']
        food_name = request.POST['foodname']
        description = request.POST['description']
        food_type = request.POST['foodtype']
        cal = request.POST['cal']
        protein = request.POST['protein']
        fats = request.POST['fats']
        carbs = request.POST['carbs']
        img = request.POST['img']
        link_of_recipie = request.POST['recipe']
        buy = request.POST['buy']

        myconn = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J")
        concursor = myconn.cursor()
        concursor.execute("CREATE DATABASE IF NOT exists Food")
        mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
        cursor = mydb.cursor()
        table = '''SELECT*FROM basic_app_food_diary'''
        df = pd.read_sql(table, mydb)

        unique_ids = list(df['food_id'])
        unique_names = list(df['food_name'])

        if (food_id in unique_ids):
            messages.warning(request, f"Unable to add the food item. Food ID: {food_id} already present.")
            return redirect("/addfood")

        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS basic_app_food_diary(mfg_code VARCHAR(10), food_id VARCHAR(10), food_name VARCHAR(50), description VARCHAR(200), food_type VARCHAR(200), calories VARCHAR(10),fats VARCHAR(10), protein VARCHAR(10), carbohydrates VARCHAR(10), link_of_image VARCHAR(1000), link_of_recipie VARCHAR(1000), purchasing_link VARCHAR(1000))")
            query = "INSERT INTO basic_app_food_diary(mfg_code, food_id, food_name, description, food_type, calories,fats, protein, carbohydrates, link_of_image, link_of_recipie, purchasing_link) VALUES (%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s)"
            vals = (mfgcode, food_id, food_name, description, food_type, cal,fats, protein, carbs, img, link_of_recipie, buy)
            #mydb.close()
            cursor.execute(query, vals)
            mydb.commit()
            messages.success(request, f"New Food '{food_name}' Added To The Table.")    
            return redirect("/addfood")

def addfood(request):
    return render(request, 'add_food.html')

def login(request):
    if request.method == "POST":
        admin_nm = request.POST['admin_nm']
        admin_id = request.POST['admin_id']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        repass = request.POST['repass']
        
        myconn = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J")
        concursor = myconn.cursor()
        concursor.execute("CREATE DATABASE IF NOT exists Food")
        mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
        cursor = mydb.cursor()
        
        #print(admin_nm, admin_id, phone, email, password, repass)

        if password == repass:
            cursor.execute("CREATE TABLE IF NOT EXISTS admin_data(Admin_Name VARCHAR(10), Admin_ID VARCHAR(10), PhoneNo VARCHAR(15), Email_ID VARCHAR(50), Password VARCHAR(20))")
            
            table = ''' SELECT*FROM admin_data'''
            db = pd.read_sql(table, mydb)
            unique_mail = np.array(db['Email_ID'])
            unique_phn = np.array(db['PhoneNo'])
            unique_id = np.array(db['Admin_ID'])
            unique_name = np.array(db['Admin_Name'])

            if (email in unique_mail) or (admin_id in unique_id) or (admin_nm in unique_name) or (phone in unique_phn):
                messages.info(request, "Admin Already Registered.")
                return redirect("/admin_signup")
            else:    
                query = "INSERT INTO admin_data(Admin_Name, Admin_ID, PhoneNo, Email_ID, Password) VALUES (%s, %s, %s, %s, %s)"
                vals = (admin_nm, admin_id, phone, email, password)
                #mydb.close()
                cursor.execute(query, vals)
                mydb.commit()
                return render(request, 'login.html')
        else:
            messages.error(request, "Enter Same Passwords.")
            return redirect("/admin_signup")

def signup(request):
    return render(request, 'signup.html')

def abc(request):
    return render(request, 'login.html')

def base_table(request):
    mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
    cursor = mydb.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS basic_app_food_diary(mfg_code VARCHAR(10), food_id VARCHAR(10), food_name VARCHAR(50), description VARCHAR(200), food_type VARCHAR(200), calories VARCHAR(10),fats VARCHAR(10), protein VARCHAR(10), carbohydrates VARCHAR(10), link_of_image VARCHAR(1000), link_of_recipie VARCHAR(1000), purchasing_link VARCHAR(1000))")
    table = ''' SELECT*FROM basic_app_food_diary'''

    db = pd.read_sql(table, mydb)
    #print(db.columns)
    alldata = []
    for i in range(db.shape[0]):
        temp = db.iloc[i]
        alldata.append(dict(temp))
    context = {"data":alldata}

    return render(request, 'fm_table.html', context)

def xyz(request):
    return render(request, 'upload_file.html')

def user_signup(request):
    return render(request, 'sign-up form.html')

def base_page(request):
    if request.method=="POST":
        email = request.POST['email']
        pwd = request.POST['pwd']
        
        mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
        cursor = mydb.cursor()
        query = "SELECT*FROM FoodIndex_userdata"
        db = pd.read_sql(query, mydb)
        emails = list(db['Email'])
        pwds = list(db['Password'])

        user_dict = dict(zip(emails, pwds))

        if email not in emails:
            messages.error(request, "No User Found!")
            return redirect('/')
        else:
            if user_dict[email] == pwd:
                return render(request, 'home.html')
            else:
                return HttpResponse("Password does not match the email. Enter correct password.")

def user_login(request):
    return render(request, 'user_login.html')

def user_to_database(request):
    if request.method=="POST":
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        pwd = request.POST['pwd']
        repwd = request.POST['repwd']
        weight = request.POST['weight']
        gender=request.POST['gen']
        WorkType=request.POST['level']
        
        if pwd == repwd:
            mydb = msql.connect(host="15.207.8.17", user="Food", password="zhTnxpRFiSzpaF2J", db="Food")
            cursor = mydb.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS FoodIndex_userdata(FirstName VARCHAR(100), LastName VARCHAR(100), Email VARCHAR(100), PhoneNo VARCHAR(20), Age VARCHAR(3), Password VARCHAR(50), Weight VARCHAR(3), Gender VARCHAR(50),WorkType VARCHAR(50))")
            table = ''' SELECT*FROM FoodIndex_userdata'''
            db = pd.read_sql(table, mydb)
            unique_mail = list(db['Email'])
            unique_phn = list(db['PhoneNo'])
            if email in unique_mail or phone in unique_phn:
                messages.info(request, "User Already Registered")
                return redirect("/user_signup")
            else:
                query = "INSERT INTO FoodIndex_userdata(FirstName, LastName, Email, PhoneNo, Age, Password, Weight,Gender,WorkType) VALUES (%s, %s, %s, %s, %s, %s ,%s,%s,%s)"
                vals = (first, last, email, phone, age, pwd, weight,gender,WorkType)
                #mydb.close()
                cursor.execute(query, vals)
                mydb.commit()
                messages.success(request, "User Added Succesfully")
                return redirect("/user_signup")

        else:
            messages.error(request, "Password not same.")
            return redirect("/user_signup")

    return None

def delete_book(request, food_id):
    food_id = str(food_id)
    food = food_diary.objects.get(food_id=food_id)
    food.delete()
    return redirect("/base_table")

def update_food(request, food_id):
    #food_name = str(food_name)
    food = food_diary.objects.get(food_id = food_id)
    updatefood = UpdateFood(request.POST or None, instance = food)
    if updatefood.is_valid():
       updatefood.save()
       return redirect('/base_table')
    return render(request, 'update_form.html', {'update_form':updatefood})

def updata_userdata(request, email):
    email = str(email)
    #s = email[:email.index("@")]
    userdata = UserData.objects.get(Email=email)
    updateuser = UpdateUserData(request.POST or None, instance=userdata)
    if updateuser.is_valid():
        updateuser.save()
        return redirect("/profile_page")
    return render(request, 'update_userdata.html', {'update_userdata':updateuser})

def first_page(request):
    return render(request, 'admin_or_user.html')

def delete_table(request):
    table = food_diary.objects.all()
    table.delete()
    return redirect("/base_table")

