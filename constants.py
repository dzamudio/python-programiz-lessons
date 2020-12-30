"""constants docstring to describe this stuff"""
CONST_VAL = 3.14159265
CONST_NAME = 'PI'

def LINE(*msgs):
    if len(msgs) == 0:
        print("Press enter to continue...")
    else:
        finalMsg = "";
        for msg in msgs:
            finalMsg += ' ' + str(msg)
        input(finalMsg.strip())


class Core():
    def __init__(self):
        pass
    
    def line(self,*msgs):
        if len(msgs) == 0:
            print("Press enter to continue...")
        else:
            finalMsg = "";
            for msg in msgs:
                finalMsg += ' ' + str(msg)
            input(finalMsg.strip())