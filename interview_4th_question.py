#URL: https://blog.svpino.com/2015/05/08/solution-to-problem-4
import string

def comparator(x_str, y_str):
    max_len = max(len(x_str), len(y_str))
    format_str = "{:0<" + str(max_len) + "s}"
    new_x_str = format_str.format(x_str)
    new_y_str = format_str.format(y_str)
#    print new_x_str, " ", new_y_str

    return cmp(new_x_str, new_y_str)




input = [50, 5, 56]
#input = [321, 4, 56,124,567,744,2565]
print input
new_input = sorted(input, cmp=comparator, key=lambda x: str(x), reverse=True)
print new_input
