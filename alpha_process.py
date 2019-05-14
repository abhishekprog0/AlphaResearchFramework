f1 = open("alphas_nomdf.txt")
f2 = open("alphas_final.txt", "w")

alpha_list = ""
for item in f1:
    alpha_list += item

alpha_list = alpha_list.split("@@")

for alpha in alpha_list:
    alpha = alpha.split(";")
    print (alpha)
    break
