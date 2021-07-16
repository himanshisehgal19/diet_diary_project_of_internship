# Diet_Diary_project_of_internship
### The main idea for this project was that each user can maintain his diet diary so as to analyze his/her diet. On the main page via an API all the food items that are present on the company's website will be displayed as shown below:

![Screenshot (103)](https://user-images.githubusercontent.com/55012463/125988028-ef6cdba4-0b83-4742-a023-b94ec430f55c.png)


 ##  After clicking on Consume items User can select any food item for his consumption or he/she can check the details of the food item
 
 ![Screenshot (106)](https://user-images.githubusercontent.com/55012463/125989022-47dda104-9e7c-44a6-a14c-3f5cfb9ec260.png)



### Here as per the example user selects the shrikhand and consumes 1 unit after clicking on the consume button.An API of getfood is called and it will directly send the details to transaction table
![Screenshot (111)](https://user-images.githubusercontent.com/55012463/125990376-9f0bfd4e-82e2-449f-bf51-a3152904c8d9.png)






## This is the transaction table


![Screenshot (119)](https://user-images.githubusercontent.com/55012463/125994063-6310689a-7b91-48d4-aedf-757a7e200195.png)



## After clicking on detail button it will redirect to the next page where the details of that particular food item is fetched by using an API i.e. getfooddetails
![Screenshot (109)](https://user-images.githubusercontent.com/55012463/125990206-c56f88ed-9731-4d81-9feb-f39b81a1508e.png)




## Example:

![image](https://user-images.githubusercontent.com/55012463/121367109-a73c0b80-c957-11eb-9e90-0dc15b22ca09.png)

## Now after clicking on Purchase Items User can select any shop name from which he/she wants to buy food items

![Screenshot (112)](https://user-images.githubusercontent.com/55012463/125990838-56c03d54-4568-431e-8b7d-28d0068fea73.png)

## After clicking on amazon only those items will be displayed which are filtered as shop_name='amazon'

![Screenshot (114)](https://user-images.githubusercontent.com/55012463/125991958-98e791ee-5916-4155-bb4c-07d69557e4e3.png)

## Here as per the example user selects the noodles and purchases one unit after clicking on the confirm button.
![Screenshot (115)](https://user-images.githubusercontent.com/55012463/125992996-25fa3fda-2165-4603-b6b6-ff2d8c4a99f0.png)

## After clicking on the confirm button it will redirect to the invoice page as shown below:
![Screenshot (116)](https://user-images.githubusercontent.com/55012463/125993151-d9b5f181-1afa-409b-ba33-3c7beaf58e2e.png)

## Now clicking on the 'Click here to Review and confirm all your purchases' button the details will directly send to the purchasing table as shown below:
![Screenshot (117)](https://user-images.githubusercontent.com/55012463/125993796-bd88faeb-653c-4249-bd28-7c67e0e9005a.png)







# ANALYSIS

#### An Api of getuserlogs  will be called here and a dataframe will be formed from this API and later this dataframe is used for the further analysis

![Screenshot (120)](https://user-images.githubusercontent.com/55012463/125994882-83979493-fa0a-40da-babc-4031e6b7cf7b.png)

![Screenshot (121)](https://user-images.githubusercontent.com/55012463/125994728-171f5fbb-9cc3-4e02-bf44-c85d44b5a6bb.png)

![Screenshot (122)](https://user-images.githubusercontent.com/55012463/125994756-e2a8cb1d-68c8-4f31-a65e-9b3603bde56b.png)


![Screenshot (123)](https://user-images.githubusercontent.com/55012463/125994795-f9dbb648-ff62-4271-9424-3e71f4f97d21.png)




![Screenshot (124)](https://user-images.githubusercontent.com/55012463/125995380-c03d184f-744a-4d8a-8841-6b1a3b55b1a3.png)

## He/She can also see his Datewise Calorie Analysis

![Screenshot (125)](https://user-images.githubusercontent.com/55012463/125995369-b1c86c5d-c46b-43f3-b574-857bc800320e.png)


## Nutrition Analysis
![image](https://user-images.githubusercontent.com/55012463/121392313-e32d9b80-c96c-11eb-87a9-771a131541b5.png)
## Graph of carbohydrates consumed in last 5 days from 26-05-2021
![image](https://user-images.githubusercontent.com/55012463/121392272-dc9f2400-c96c-11eb-8a68-1bd0a0ee09df.png)


## An Analysis chart that can compare the purchasing and consumption  analysis
![Screenshot (104)](https://user-images.githubusercontent.com/55012463/125988402-dc600da4-6efd-4724-a22b-16844330bae6.png)


## User can view his/her history for every food item that is purchased


![Screenshot (127)](https://user-images.githubusercontent.com/55012463/125995581-94b4db93-931d-411e-b265-b4d5450b0032.png)

## User can view his/her history for every food item that is consumed

![Screenshot (128)](https://user-images.githubusercontent.com/55012463/125995679-c7bc94a5-c258-45b1-9441-c94b2a231a3f.png)




