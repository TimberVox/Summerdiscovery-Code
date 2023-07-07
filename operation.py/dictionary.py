weekly_salary={"Li Hua":500,"Xiao Ming":300,"Xiao Hong":450}
week_done={"Li Hua":2,"Xiao Ming":4,"Xiao Hong":3}
employee=weekly_salary.keys()
for employee in weekly_salary.keys():
    total=weekly_salary[employee]*week_done[employee]  
    print(total)