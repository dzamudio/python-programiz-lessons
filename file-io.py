import uuid
import time
import os
import constants as DZ
import pprint

try:
    f = open("file-io.txt", mode='w', encoding='utf-8')
    # f = open("C:/Python38/README.txt");
    # w is write as new, a is append (creates if not), x is exclusive creation
    linesLimit = 80
    for limit in range(linesLimit):
        limit += 1
        f.write(str(uuid.uuid4())+"-"+str(uuid.uuid4())+"\n")
        
finally:
    f.close()

# or
# with open("file-io.txt", mode='a', encoding='utf-8') as f:
    # peform io here...
gradualGrow = 0.0001
gradualShrink = 0.3000
try:
    f = open("file-io.txt", mode='r', encoding='utf-8')
    # f.read(4) # reads first 4 data
    # f.tell() # gets the current file position
    # f.seek() # bring file to cursor to initial position
    # print(f.read()) # read the entire file
    for line in f:
        if gradualGrow <= 0.1000:
            gradualGrow += 0.0005
            time.sleep(gradualGrow)
            #print("LOCK (",gradualGrow,")"+line, end='')
        elif gradualGrow == 0.1000:
            gradualGrow = 0.0005
            time.sleep(gradualGrow)
            #print("UN-LOCK (",gradualGrow,")"+line, end='')
        else:
            gradualGrow = 0.0005
            gradualGrow -= 0.0005
            time.sleep(gradualGrow)
            #print("RAD (",gradualGrow,")"+line, end='')
        
        print(line, end='')
        #time.sleep(gradualGrow)
finally:
    print(f.tell())
    print(f.fileno())
    f.close()

pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(project_info)

os_cwd = os.getcwd()
DZ.LINE("os.cwd " + str(os_cwd))

os_cwdb = os.getcwdb()
DZ.LINE("os.cwdb " + str(os_cwdb))

DZ.LINE("os.chdir('[REDACTED]')")
os.chdir('[REDACTED]')
DZ.LINE(str(os.getcwd()))

DZ.LINE(os.listdir())
pp.pprint(os.listdir())

for dir in os.listdir():
    # DZ.LINE(str(dir))
    if dir == 'LYE':
        DZ.LINE("READING INSIDE LYE")
        os.chdir('LYE')
        pp.pprint(os.listdir())
        DZ.LINE("CREATING DIR 'MKSHIFT' in LYE/")
        try:
            # CREATES MKSHIFT ----------------------------------------------- 1/3
            # EXITS()
            os.mkdir('MKSHIFT')
        except:
            DZ.LINE("MKSHIFT dir already exists stupid")
            DZ.LINE("WARNING: renaming an existing folder to a name that already exists will overwrite both.")
            try:
                # RENAMES MKSHIFT TO MKSHIFT_STUIPID ------------------------ 2/4
                # EXITS()
                os.rename('MKSHIFT', 'MKSHIFT_STUPID') # FAILS IS DIRs NON-EMPTY
                DZ.LINE("MKSHIFT renamed to MKSHIFT_STUPID")
            except:
                DZ.LINE("Removing both directories for shits and gigs.")
                # remove(file)rmdir(emptydir)rmtree(non-empty dir)
                import shutil
                # ONLY HAPPENS WHEN both DIRs are NON-EMPTY and CANNOT BE RENAMED
                # ------------------------------------------------------------- 5
                shutil.rmtree('MKSHIFT')
                shutil.rmtree('MKSHIFT_STUPID')
    
print("EOL")
            