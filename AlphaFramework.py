
import random
import numpy as np
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
    k = 3
    alphas = random.sample(alpha_list, k)
    weights = list()
    for i in range(k):
        r = np.random.uniform(0, 1)
        weights.append(round(r, 3))

    s = np.sum(weights)
    weights = [round(x/s, 3) for x in weights]

    alpha_weighted = ""
    for i in range(k):
        alpha_weighted += str(weights[i]) + "*" + alphas[i] + "+"

    alpha_weighted = alpha_weighted[:-1]
    #print (alpha_weighted)
    return alpha_weighted

def regression():
    param = ["step(1)", "step(2)", "rank(close)", "rank(volume)", "rank(adv20)", "rank(vwap)", "rank(ts_decay_linear(returns, 20))", "rank(cap)", "rank(close/cap)"]
    rand_param = random.choice(param)
    return ("x = ts_regression(rank(alpha)," + rand_param + ", 252, lag = 0, rettype = 0);\n")

def filters():
    param1 = ["eps", "income", "ebit", "ebitda", "pretax_income", "income_beforeextra", "inventory_turnover", "assets", "assets_curr", "assets_curr_oth", "bookvalue_ps", "cashflow", "cashflow_fin", "cashflow_invst", "cashflow_op", "current_ratio", "inventory", "operating_income", "quick_ratio", "receivable", "retained_earnings", "return_assets", "return_equity", "revenue"]
    param2 = ["accounts_payable", "capex", "cashflow", "cost_of_revenue", "cogs", "debt", "debt_lt", "debt_lt_curr", "debt_st", "enterprise_value", "equity", "income_tax","income_tax_payable", "interest_expense", "invested_capital", "liabilities", "liabilities_cur_oth", "liabilities_curr", "liabilities_oth", "operating_expense", "ppent", "ppent_net", "preferred_dividends", "rd_expense", "sales", "sales_growth", "sales_ps", "SGA_expense", "working_capital"]
    n_days = ["60", "120", "180", "240"]
    r = np.random.uniform(1.5, 3.0)
    r = round(r, 2)

    p1 = random.choice(param1)
    p2 = random.choice(param2)
    n = random.choice(n_days)

    filter_condition1 = "volume > ts_max(volume, 3) - ts_min(volume, 3)"
    filter_condition2 = "rank(ts_delta(" + p1 + "/" + p2 + "," + str(n) + ")) > " + str(r)

    filter_t = "y = " + filter_condition1 + " || " + filter_condition2 + " ? x : -1;\n"
    return filter_t

def neutralize():
    param = ["country", "market", "sector", "industry", "subindustry", "exchange"]
    rand_param = random.sample(param, 2)
    return ("group_neutralize(y," + rand_param[0] + " + " + rand_param[1] + ")\n")

alpha_weighted = alpha_weighing_pipeline()
alpha_weighted = "alpha = " + alpha_weighted + ";\n"
alpha_weighted += regression()
alpha_weighted += filters()
alpha_weighted += neutralize()

print (alpha_weighted)
print ("\n\n")





