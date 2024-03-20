from non_lineare_quation import *
from non_lineare_system import *
import sys

def main():
    type = (sys.argv[1])
    
    if str(type) == "true":
        input_variant = int(1)
    else:
        input_variant = int(2)
    
    
    

    switch_command = {
        1: non_lineare_quation,
        # 2: system_of_non_linear_equations,
        2: non_lineare_system,
        3: exit,
    }
    switch_command.get(input_variant, exit)()


if __name__ == "__main__":
    main()
