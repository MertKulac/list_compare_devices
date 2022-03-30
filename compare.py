ARBOR = []
with open('MO_ARBOR.txt') as f:
    lines = f.readlines()
    lines2 = "".join(lines)
    lines3 = lines2.split("/32")
    lines4 = "".join(lines3)
    lines5 = lines4.strip()
    lines6 = lines5.split()
    #print(lines6)

with open('UPE_PUBLIC.txt') as f:
    lines10 = f.readlines()
    lines20 = "".join(lines10)
    lines30 = lines20.replace("\n",",")
    lines30 = lines30.split(",")

while '' in lines30:  # A method that removes specific characters. (for example "" > empty)
    lines30.remove('')

for i in lines30:
    if i in lines6:
        print(i + ":Tanım Var")
        with open('var.txt', 'a') as f:
            f.write(i +" "+"Tanım Var"+"\n")
    else:
        print(i + ":Tanım Yok")
        with open('yok.txt', 'a') as f:
            f.write(i +" "+"Tanım Yok"+"\n")








