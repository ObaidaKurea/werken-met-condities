kaas = input("is de  kaas geel?")
if  kaas == "yes":
    wat = input("zitten er gaten in?")
    if  wat == "yes":
        wat = input("is de kaas belachelijk duur?")
        if wat == "yes":
            print("emmenthaler")
        elif wat == "no ":
            print("leerdammer")
    elif wat == "no":
        wat = input(" is de kaas hard als steen?")
        if wat == "yes":
            print("pamnigiano reggiano")
        elif wat == "no":
            print ("goudse kaas")
elif kaas == "no":
    kaas = input("heeft fr kaas blaouwe shimmels?")
    if kaas == "yes":
        kaas = input("heeft de kaas een korst?")
        if kaas == "yes":
            print("bleu de rochbaron")
    elif kaas == "no":
        kaas = input("heeft de kaas een korst")
        if kaas == "yes":
            print(" camembert")
        elif kaas == "no":
            print("Mozzarella")
else:
    print("u have to (say yes or no) ")
            
          







            
    


