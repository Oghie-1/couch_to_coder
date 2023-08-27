#!/usr/bin/python3

employees = [
    {
        "first_name": "Jose",
        "last_name": "Lopez",
        "email": "joselopez0944@example.com",
        "age": 25,
        "job_title": "Project Manager",
        "years_of_experience": 1,
        "salary": 8500,
        "department": "Product"
    },
    {
        "first_name": "Diane",
        "last_name": "Carter",
        "email": "dianecarter1228@example.com",
        "age": 26,
        "job_title": "Machine Learning Engineer",
        "years_of_experience": 2,
        "salary": 7000,
        "department": "Product"
    },
    {
        "first_name": "Shawn",
        "last_name": "Foster",
        "email": None,
        "age": 37,
        "job_title": "Customer Service Rep",
        "years_of_experience": 14,
        "salary": 17000,
        "department": "Business"
    },
    {
        "first_name": "Brenda",
        "last_name": "Fisher",
        "email": "brendafisher3185@example.com",
        "age": 31,
        "job_title": "Web Developer",
        "years_of_experience": 8,
        "salary": 10000,
        "department": "Product"
    },
    {
        "first_name": "Sean",
        "last_name": "Hunter",
        "email": None,
        "age": 35,
        "job_title": "Project Manager",
        "years_of_experience": 11,
        "salary": 14500,
        "department": "Product"
    },
    {
        "first_name": "Joshua",
        "last_name": "Jacobs",
        "email": "joshuajacobs5904@example.com",
        "age": 28,
        "job_title": "Project Manager",
        "years_of_experience": 3,
        "salary": 10500,
        "department": "Business"
    },
    {
        "first_name": "Brianna",
        "last_name": "Marshall",
        "email": None,
        "age": 33,
        "job_title": "Machine Learning Engineer",
        "years_of_experience": 10,
        "salary": 11000,
        "department": "Product"
    },
    {
        "first_name": "John",
        "last_name": "Tate",
        "email": "johntate7881@example.com",
        "age": 33,
        "job_title": "Mobile Developer",
        "years_of_experience": 10,
        "salary": 11000,
        "department": "Product"
    },
    {
        "first_name": "Jillian",
        "last_name": "Byrd",
        "email": None,
        "age": 34,
        "job_title": "Business Analyst",
        "years_of_experience": 10,
        "salary": 11000,
        "department": "Business"
    },
    {
        "first_name": "Melanie",
        "last_name": "Sharp",
        "email": "melaniesharp9256@example.com",
        "age": 41,
        "job_title": "Web Developer",
        "years_of_experience": 15,
        "salary": 14500,
        "department": "Product"
    },
    {
        "first_name": "Brandy",
        "last_name": "Mckee",
        "email": None,
        "age": 37,
        "job_title": "Marketing Manager",
        "years_of_experience": 14,
        "salary": 14000,
        "department": "Business"
    },
    {
        "first_name": "Robert",
        "last_name": "Simpson",
        "email": "robertsimpson11778@example.com",
        "age": 36,
        "job_title": "Marketing Manager",
        "years_of_experience": 12,
        "salary": 15000,
        "department": "Business"
    },
    {
        "first_name": "George",
        "last_name": "Mckenzie",
        "email": "georgemckenzie12384@example.com",
        "age": 28,
        "job_title": "Machine Learning Engineer",
        "years_of_experience": 4,
        "salary": 10000,
        "department": "Product"
    },
    {
        "first_name": "Joseph",
        "last_name": "Smith",
        "email": None,
        "age": 40,
        "job_title": "Machine Learning Engineer",
        "years_of_experience": 14,
        "salary": 14000,
        "department": "Product"
    },
    {
        "first_name": "Dana",
        "last_name": "Crawford",
        "email": "danacrawford14310@example.com",
        "age": 32,
        "job_title": "Project Manager",
        "years_of_experience": 8,
        "salary": 12000,
        "department": "Product"
    },
    {
        "first_name": "Christopher",
        "last_name": "Benson",
        "email": None,
        "age": 29,
        "job_title": "Web Developer",
        "years_of_experience": 5,
        "salary": 7500,
        "department": "Product"
    },
    {
        "first_name": "Nicole",
        "last_name": "Smith",
        "email": "nicolesmith16360@example.com",
        "age": 26,
        "job_title": "Designer",
        "years_of_experience": 4,
        "salary": 10000,
        "department": "Product"
    },
    {
        "first_name": "Peter",
        "last_name": "Jimenez",
        "email": "peterjimenez17791@example.com",
        "age": 28,
        "job_title": "UX Designer",
        "years_of_experience": 3,
        "salary": 6500,
        "department": "Business"
    },
    {
        "first_name": "Sergio",
        "last_name": "Boyle",
        "email": "sergioboyle18425@example.com",
        "age": 31,
        "job_title": "Tester",
        "years_of_experience": 6,
        "salary": 9000,
        "department": "Product"
    },
    {
        "first_name": "Brianna",
        "last_name": "Moss",
        "email": None,
        "age": 31,
        "job_title": "Designer",
        "years_of_experience": 5,
        "salary": 10500,
        "department": "Product"
    },
    {
        "first_name": "Taylor",
        "last_name": "Garner",
        "email": "taylorgarner20196@example.com",
        "age": 32,
        "job_title": "Machine Learning Engineer",
        "years_of_experience": 6,
        "salary": 11000,
        "department": "Product"
    },
    {
        "first_name": "Michael",
        "last_name": "Padilla",
        "email": "michaelpadilla21381@example.com",
        "age": 29,
        "job_title": "Customer Service Rep",
        "years_of_experience": 5,
        "salary": 9500,
        "department": "Business"
    },
    {
        "first_name": "Yvette",
        "last_name": "Walker",
        "email": None,
        "age": 26,
        "job_title": "Designer",
        "years_of_experience": 2,
        "salary": 7000,
        "department": "Product"
    },
    {
        "first_name": "Kristina",
        "last_name": "Pena",
        "email": "kristinapena23750@example.com",
        "age": 34,
        "job_title": "Business Analyst",
        "years_of_experience": 11,
        "salary": 12500,
        "department": "Business"
    }
]

# Print the name of the person who has the highest salary at the company.

def highest_salary(employees):
    highest_salary = None
    for item in employees:
        if highest_salary is None or item["salary"] > highest_salary["salary"]:
            highest_salary = item
    return highest_salary["first_name"]



result = highest_salary(employees)


# Print the combined years of experience of all employees at the company.

def combined_years_of_experience(employees):
    combined_years_of_experience = 0
    for item in employees:
        if item['years_of_experience'] > 0:
            combined_years_of_experience += item["years_of_experience"]
    return combined_years_of_experience


result = combined_years_of_experience(employees)

#print(result)


# Some people don't have an email address - collect their details into a new list!

def no_emails(employees):
    no_email_list = []
    for item in employees:
        if item["email"] is None:
            no_email_list.append(item)
    return no_email_list

result = no_emails(employees)

#print(result)

# Which one costs more for the company - Product department salaries or Business department salaries?

def cost_comparism(employees):
    total_biz_dept_salary = 0
    total_prd_dept_salary = 0
    for item in employees:
        if item["department"] == "Product":
            total_prd_dept_salary += item["salary"]
        elif item["department"] == "Business":
            total_biz_dept_salary += item["salary"]
        
    if total_biz_dept_salary > total_prd_dept_salary:
        print("\nBusiness Department is Bigger with: {}".format(total_biz_dept_salary))
    else:
        print("\nProduct department is Bigger with: {}".format(total_prd_dept_salary))


#cost_comparism(employees)

# What is the average salary for people over 30 years of age?

def avrage_salary_of_people_over_30(employees):
    av_salary = 0
    nos_of_employees_over_30 = 0
    for item in employees:
        if item["age"] >= 30:
            av_salary += item["salary"]
            nos_of_employees_over_30 += 1
            result = av_salary / nos_of_employees_over_30

    return result

print(avrage_salary_of_people_over_30(employees))

#Create a new dict and calculate how many people are in the company with the same job title

def similar_job_title(employees):
    similar_job_title = {}
    for item in employees:
        if item["job_title"] in similar_job_title:
            similar_job_title[item["job_title"]] += 1
        else:
            similar_job_title[item["job_title"]] = 1
    return similar_job_title
            


print(similar_job_title(employees))