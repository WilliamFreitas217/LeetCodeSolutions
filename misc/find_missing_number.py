def find_missing_number(number_list):
    formula = (len(number_list)*(len(number_list) + 1))/2
    return formula - sum(number_list)