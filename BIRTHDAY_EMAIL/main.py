import random
import pandas as pd
import smtplib
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
date = now.day

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("birthdays.csv")
dict_data = data.to_dict(orient='records')
name = ''
email = ""
for data in dict_data:
    if data['day'] == date and data['month'] == month:
        name = data['name']
        email = data['email']
        select_letter = random.randint(1,3)
        with open(f"letter_templates/letter_{select_letter}.txt",'r') as letter:
            content = letter.read()
            content = content.replace("[NAME]",name)

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = "ssanyukta16@gmail.com"
        password = "jmivpefvcsyjlksf"

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()

            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Birthday Wish\n\n{content}")




