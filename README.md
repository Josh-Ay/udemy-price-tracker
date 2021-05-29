# udemy-price-tracker
Scrapes the udemy website for a particular course and sends an email if the price falls below a set price.

# Overview
Udemy is a top online learning platform that helps people looking to learn a new skill or upskill themselves reach their goals by connecting them to the best instructors. 

# Objective/Motivation
On udemy, there is a machine learning course by one of the most top-rated instructors on udemy that some of my friends recommended but, I could not afford it at its base price so I was always looking out for the promotions that udemy does every year so I could afford to buy it. So, instead of opening up the website manually to be checking if there was a promomtion, I came up with a script that does just that for me and automated it using [PythonAnywhere](https://www.pythonanywhere.com/). 

# How it works
- It fills in the name of the course using Selenium and then scrapes the udemy site for the price.
- It sends me a mail if the price is lower than a particular price that I set.

