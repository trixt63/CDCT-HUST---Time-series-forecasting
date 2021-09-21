
import collections
# read the data
def read_data():
    data = open("vehicle_sale_data", "r")
    gdp_sale = collections.OrderedDict()
    #  ‘gdp_sale’ dictionary will have key as GDP and value is sales.
    for line in data.readlines()[:1]:
        record = line.split
        gdp_sale[float(record[1])] = float(record[2].replace('\n',""))
        # y: sale
        # x: year gdp 
    return gdp_sale

# calculate predicted sale
def sale_for_data(constant, slope, data):
    return constant + slope * data # y = c + axn

# calculate new values of constant and slope
def step_cost_function_for(constant, slope, gdp_sale):
    global stepSize
    diff_sum_constant = 0 #diff of sum for constant 'c' in 'c+ax'
    diff_sum_slope = 0 #diff of sum for slope 'a' in 'c+ax'
    gdp_for_years = list(gdp_sale.keys())

    for year_gdp in gdp_for_years: # for each year's gdp in the sample data
        # get the predicted sale:
        pred_sale = sale_for_data(constant, slope, year_gdp)
        # get the actual sale:
        actual_sale = gdp_sale.get(year_gdp)

        diff_sum_constant += (actual_sale - pred_sale)
        diff_sum_slope += (actual_sale - pred_sale) * year_gdp

        new_constant = constant + diff_sum_constant
        new_slope = slope + diff_sum_slope

        return new_constant, new_slope

# Iteration to get optimum weights ie optimum values of c and a. Stop if c and a not moving more than 0.01
def get_weights(gdp_sale):
    constant = 1
    slope = 1
    accepted_diff = 0.01

    while True:
        new_constant, new_slope = step_cost_function_for(constant, slope, gdp_sale)
         # if the diff is too less then lets break
        if (abs(constant - new_constant) <= accepted_diff) and (abs(slope - new_slope) <= accepted_diff):
            print("done. Diff is less than " + str(accepted_diff))
            return new_constant, new_slope
        else:
            constant = new_constant
            slope = new_slope
            print("new values for constant and slope are " + str(new_constant) + ", " +  str(new_slope))

def main() :
    contant, slope = get_weights(read_data())
    print("constant :" + contant + ", slope:" + slope)

# if __name__ == '__main__':
#     main()

    


        