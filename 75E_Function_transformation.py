import sys
import re


func_name = "(?:" + "|".join(['sqrt', 'abs', 'sin', 'cos', 'tan', 'exp', 'log']) + ")"
args      = "\([\w,+\-*/]+\)"
func      = func_name + args
operand   = "(" + func + "|" + "[\w]+" + ")"
binop     = "([" + "".join(['+', '\-', '*', '/']) + "])"
pattern   = '([\w]+)\(([\w,]*)\)=' + operand + binop + operand
# pattern = '([\w]+)\(([\w,]*)\)=' +  '([^+\-*/]+)' + binop + '([^+\-*/]+)'


# pattern =  "([\w]+)\(([\w,])*\)=" + "((?:sqrt|abs)\([\w,+\-*/]+\)|[\w]+)" + "([+\-*/])" + \
# "((?:sqrt|abs)\([\w,]*\)|[\w]+)"


def process_result(res):
    func_name, pars, op1, binop, op2 = res
    pars = pars.split(",")
    ret  =  "float " + func_name + "("
    ret += ", ".join("float " + par for par in pars) + ")\n{\n"


    op_l  = ['abs', 'sin', 'cos', 'tan', 'sqrt', 'exp', 'log']
    op_rl = ['fabs', 'fsin', 'fcos', 'ftan', 'fsqrt', 'fexp', 'flog']
    for op, op_r in zip(op_l, op_rl):
        op1 = op1.replace(op, op_r)
        op2 = op2.replace(op, op_r)

    ret += "\treturn " + op1 + " " + binop + " " + op2 + ";\n}\n"
    return ret

file = open(sys.argv[1])
for line in file.readlines():
    result = re.match(pattern, line.strip())
    if result :
        print(line)
        print(result.groups())
        print(process_result(result.groups()))


