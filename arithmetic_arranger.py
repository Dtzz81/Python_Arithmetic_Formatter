def arithmetic_arranger(problems, result = False):
    output = ""
    n1f = ""
    n2f = ""
    op = ""
    
    for i in problems:    
        if len(problems) > 5:
            return "Error: Too many problems." 
        
    for i in problems:  
        n1s = (i.split(" ")[0])
        op = i.split(" ")[1]
        n2s = (i.split(" ")[2])
        if (op != '+') and (op != '-'):
            return "Error: Operator must be '+' or '-'."    
        
    for i in problems:
        n1s = (i.split(" ")[0])
        n2s = (i.split(" ")[2])
        try:
            n1 = int(n1s)
        except ValueError:
            return "Error: Numbers must only contain digits."
        try:
            n2 = int(n2s)
        except ValueError:
            return "Error: Numbers must only contain digits."
         
    for i in problems:
        
        n1s = (i.split(" ")[0])
        n2s = (i.split(" ")[2])
        op = i.split(" ")[1]
        if len(n1s) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif len(n2s) > 4:
            return"Error: Numbers cannot be more than four digits."
        else: 
            pass
     
    n1f = []
    n2f = []
    opf = []     
     
    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""
    
    for i in problems:  
        
        n1f.append(i.split(" ")[0])
        opf.append(i.split(" ")[1])
        n2f.append(i.split(" ")[2])
        
    for i in range(len(problems)):
        n1 = n1f[i]
        n2 = n2f[i]
        op = opf[i]
        
        space = max(len(n1),len(n2))
        n1x = f"{n1:>{space}}"
        if i != 0:
            first_line += "    "
        first_line += "  " + n1x
        
        n2x = f"{n2:>{space}}"
        if i != 0:
            second_line += "    "
        second_line += op + " " + n2x 
        

        dashes_len = space + 2
        if i != 0:
            dash_line += "    "
        for d in range(dashes_len):
            dash_line += "-" 
    
        if op == "+":
            total = int(n1) + int(n2)
        else:
            total = int(n1) - int(n2)
       
        extra_space = 2
        if i != 0:
            extra_space  += 4
        result_string = f"{total:>{space + extra_space}}"
        
        result_line += result_string
        
    if result:  
        output = first_line + "\n" + second_line + "\n" + dash_line + "\n" + result_line
    
    else:
        output = first_line + "\n" + second_line + "\n" + dash_line 
      
    return output
