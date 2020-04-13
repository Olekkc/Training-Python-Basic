#Test Def. Function
def hello(name):
    print("Hello %s"% name)


#test call function
hello("ole")


# Def. function return
def Sumdata(d1, d2):
    sumbuff = d1 + d2
    return sumbuff

#test call function return
print(Sumdata(2, 5))


#Test function default value parameter
def show_Info(name,salary=0.00,lang="not define"):
    print("Name: %s"% name)
    print("Salary: %s" % salary)
    print("Language: %s" % lang)
    print("\r")


show_Info("ole")
show_Info("ole",10,"Java")

