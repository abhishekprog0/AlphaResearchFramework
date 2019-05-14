f = open("alphas.txt")
fout1 = open("alphas_mdf.txt", "w")
fout2 = open("alphas_nomdf.txt", "w")
l = ""

for line in f:
    l += line

s = l.split("@@")

for item in s:
    if "mdf" in item:
        fout1.write(item + "@@")
    else:
        fout2.write(item + "@@")