
import random
import numpy as np

np.random.seed(30)
def data_preprocessing_pipeline():

    f = open("101alphas.txt")
    print("\n\n\t\t\t\t\t\tAsia Alpha Research and Development Framework")
    print ("\n\n")
    alpha = ""
    alpha_list = list()
    start_flag = 1
    for line in f:

        line = line.rstrip()
        line = line.replace("sum", "ts_sum")
        line = line.replace("correlation", "ts_corr")
        line = line.replace("IndClass.", "")
        line = line.replace("IndNeutralize", "group_neutralize")
        line = line.replace("decay_linear", "ts_decay_linear")
        line = line.replace("adv40", "ts_decay_linear(volume, 40)")
        line = line.replace("adv60", "ts_decay_linear(volume, 60)")
        line = line.replace("adv120", "ts_decay_linear(volume, 120)")
        line = line.replace("adv180", "ts_decay_linear(volume, 180)")
        line = line.replace("stddev", "ts_stddev")
        line = line.replace("Ts_ArgMax", "ts_arg_max")
        line = line.replace("SignedPower","signed_power")
        temp_line = line
        for i in range(len(line)):
            if line[i] == '.':
                j = i - 1
                k = i + 1

                while j >= 0:
                    if (line[j].isdigit()):
                        j -= 1
                    else:
                        break

                while k < len(line):
                    if line[k].isdigit():
                        k += 1
                    else:
                        break
                
                floatingNum = line[j + 1 : k]
                t1 = (floatingNum)
                t2 = int(float(floatingNum))
                if t2 == 0:
                    t2 = 1
                #print(floatingNum)
                temp_line = temp_line.replace(t1, str(t2))
                #print (temp_line)
        
        line = temp_line
        if line.startswith("Alpha") and start_flag:
            alpha += line
            start_flag = 0

        if line.startswith("Alpha") and not start_flag:
            i = 0
            for ch in alpha:
                if ch == '(':
                    break
                i += 1
            
            alpha = alpha[i:len(alpha)]
            '''
            if alpha[-1] != ')':
                if alpha[-2] != ')':
                    alpha = alpha[:-2]
                else:
                    alpha = alpha[:-1]
            '''
            alpha_list.append(alpha)
            alpha = line
        else:
            alpha += line
    '''
    for alpha in alpha_list:
        temp = alpha.split()
        for element in temp:
            try:
                float(element)
                element = str(int(round(element, 0)))
            except ValueError:
                pass
    '''
         
    return alpha_list

def alpha_weighing_pipeline():

    alpha_list = data_preprocessing_pipeline()
    k = 2
    alphas = random.sample(alpha_list, k)

    alpha_weighted = "x1 = " + alphas[0] + ";\n"
    alpha_weighted += "x2 = " + alphas[1] + ";\n"

    alpha_weighted += "n1 = max(0.5,group_rank(volume/adv20, exchange));\n"
    alpha_weighted += "n2 = max(0.5,group_rank(volume/adv20, industry));\n"
    alpha_weighted += "norm = n1 + n2;\n" 
    alpha_weighted += "alpha = (n1 * x1 + n2 * x2)/ norm;\n"

    return alpha_weighted




def regression():
    param = ["step(1)", "step(2)", "rank(close)", "rank(volume)", "rank(adv20)", "rank(vwap)", "rank(ts_decay_linear(returns, 20))", "rank(cap)", "rank(close/cap)"]
    rand_param = random.sample(param, 2)
    return ("x = ts_regression(rank(alpha)," + rand_param[1] + "+" + rand_param[0] + ", 252, lag = 0, rettype = 0);\n")

def filters():

    param1 = ["cashflow_op", "eps", "income", "ebit", "ebitda", "pretax_income", "income_beforeextra", "inventory_turnover", "assets", "assets_curr", "assets_curr_oth", "bookvalue_ps", "cashflow_fin", "cashflow_invst", "current_ratio", "inventory", "inventory_turnover", "operating_income", "quick_ratio", "receivable", "retained_earnings", "return_assets", "return_equity", "revenue"]
    param2 = ["accounts_payable", "capex", "cost_of_revenue", "cogs", "debt", "debt_lt", "debt_lt_curr", "debt_st", "enterprise_value", "equity", "income_tax","income_tax_payable", "interest_expense", "liabilities", "liabilities_cur_oth", "liabilities_curr", "liabilities_oth", "operating_expense", "ppent", "ppent_net", "preferred_dividends", "rd_expense", "sales", "SGA_expense"]
    n_days = ["63", "122", "181", "244"]

    #Thresholds
    r1 = np.random.normal(3, 1)
    r1 = round(r1, 2)
    r2 = np.random.normal(3, 1)
    r2 = round(r2, 2)
    r3 = np.random.uniform(0, 1)
    r3 = round(r3, 2)

    #Random sampling of parameters
    p1 = random.sample(param1, 2)
    p2 = random.sample(param2, 2)
    n = random.sample(n_days, 2)

    #Filters Definition
    
    #Technical Filters
    #Volumetric Spread
    technical_filter_condition1 = "volume >= ts_max(volume, 3) - ts_min(volume, 3)"
    #High Supply Less demand
    technical_filter_condition2 = "ts_delta(volume, 2) >= 0 && ts_delta(close, 2) <= 0"

    
    #Fundamental Filters
    #Cross Sectional Rank of momemntum in Decay Linear Moving Average of financial ratios
    options = [1, 2, 3, 4]
    ch = np.random.choice(options, 1)[0]
    fundamental_filter_condition1 = ""
    if ch == 1:
        fundamental_filter_condition1 = "rank(ts_decay_linear(" + p1[0] + "/" + p2[0] + "," + "60" + ")) > " + "rank(ts_decay_linear(" + p1[0] + "/" + p2[0] + "," + "120" + "))"
    elif ch == 2:
        fundamental_filter_condition1 = "rank(ts_zscore(" + p1[0] + "/" + p2[0] + "," + "120" + ")) > " + "rank(ts_zscore(" + p1[0] + "/" + p2[0] + "," + "240" + "))"
    elif ch == 3:
        fundamental_filter_condition1 = "rank(ts_decay_linear(" + p1[0] + "/" + p2[0] + "," + "120" + ")) > " + "rank(ts_decay_linear(" + p1[0] + "/" + p2[0] + "," + "240" + "))"
    elif ch == 4:
        fundamental_filter_condition1 = "rank(ts_sum(" + p1[0] + "/" + p2[0] + "," + "120" + ")) > " + "rank(ts_decay_linear(" + p1[0] + "/" + p2[0] + "," + "240" + ")/2)"
    
    #filter_condition3 = "rank(ts_delta(" + p1[1] + "/" + p2[1] + "," + str(n[1]) + ")) > " + str(r2)
    fundamental_filter_condition2 = "rank(ts_zscore(" + p1[1] + "/" + p2[1] + "," + str(n[1]) + ")) > " + str(round(r3, 2))
    
    #Filters Combination
    filter_t = "y = " + technical_filter_condition1 + " || " + technical_filter_condition2 + " || " + fundamental_filter_condition1 +" || " + fundamental_filter_condition2 + " ? x : -1;\n"
    return filter_t

def neutralize():
    param = ["country", "market", "sector", "industry", "subindustry", "exchange"]
    rand_param = random.sample(param, 2)
    return ("group_neutralize(y," + rand_param[0] + " + " + rand_param[1] + ")\n")

alpha_weighted = alpha_weighing_pipeline()
alpha_weighted += regression()
alpha_weighted += filters()
alpha_weighted += neutralize()

print (alpha_weighted)
print ("\n\n")





