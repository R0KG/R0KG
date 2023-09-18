##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib 
import datetime as dt
import random

# Updating ma csv
# Read the CSV file into a DataFrame
df = pd.read_csv("birthdays.csv")

# New data for the row you want to add
mama_birth = {"name": "Mom", "email": "approm12@yahoo.com", "year": 1976, "month": "12", "day": 11}

# Convert the new data into a DataFrame
new_row_df = pd.DataFrame([mama_birth])

# Concatenate the original DataFrame and the new row DataFrame
# df = pd.concat([df, new_row_df], ignore_index=True)

# Save the updated DataFrame back to the CSV file
df.to_csv("birthdays.csv", index=False)

## 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
now_month = now.month
for index,row in df.iterrows():
    if now_month == row.month and now.day == row.day:
        my_email = "int1994019@gmail.com"
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt",'r') as write_file:
            content = write_file.read()
            new_content = content.replace("[NAME]",row["name"])
            new_content = new_content.replace("Angela","Roman")
        with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
            connection.starttls()
            connection.login(my_email, password="jqpeqxxpzszoqwal")
            connection.sendmail(from_addr=my_email,to_addrs="approm12@yahoo.com",msg=f"Subject:Mom Happy Birthday\n\n{new_content}")
 


