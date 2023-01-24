import os
import shutil
import filecmp
import difflib
from ex5 import processDirectory
#to keep the output files comment the last block of code in the file

#Change it for the number of test you want. (up to 1001)
NUM_OF_TESTS = 10

testCounter = 0
for num in range(NUM_OF_TESTS):
    passed = True
    dirpath1 = os.path.join('tests', "test{}e".format(num))
    dirpath2 = os.path.join('tests', "test{}d".format(num))
    
    print("____________________________________")
    print("test no.{}:".format(num),end=" ")

    processDirectory(dirpath1)
    
    if num in [0,1,2,3] :
        out_file = os.path.join(dirpath1, "test{}.enc".format(num))
        exp_file = os.path.join(dirpath1, "{}.out".format(num))
        
        try:
            result = filecmp.cmp(out_file, exp_file)
        except: 
            passed = False
            print("FAILED :( -> File Not Found!")
            print("in comparing: {} - {}".format(out_file,exp_file))
        if not result:
            passed = False
            print("FAILED :(")
            with open(out_file, "r") as f1:
                text1 = f1.readlines()
            with open(exp_file, "r") as f2:
                text2 = f2.readlines()
            diff = difflib.unified_diff(text1, text2)
            print("\n".join(diff))

        src_file = os.path.join(dirpath1, "test{}.enc".format(num))
        dst_file = os.path.join(dirpath2, "test{}.enc".format(num))
        shutil.copy(src_file, dst_file)
        
        processDirectory(dirpath2)

        
        file1 = os.path.join(dirpath1, "test{}.txt".format(num))
        file2 = os.path.join(dirpath2, "test{}.txt".format(num))
        try:
            result = filecmp.cmp(file1, file2)
        except: 
            passed = False
            print("FAILED :( -> File Not Found!")
            print("in comparing: {} - {}".format(file1,file2))
        
        if not result:
            passed = False
            print("FAILED :(")
            with open(file1, "r") as f1:
                text1 = f1.readlines()
            with open(file2, "r") as f2:
                text2 = f2.readlines()
            diff = difflib.unified_diff(text1, text2)
            print("\n".join(diff))
    
    else:
        for elem in os.listdir(dirpath1) :
            if elem.endswith(".enc") :
                src_file = os.path.join(dirpath1, elem)
                dst_file = os.path.join(dirpath2, elem)
                shutil.copy(src_file, dst_file)
        
        processDirectory(dirpath2)
        for elem in os.listdir(dirpath1) :
            if elem.endswith(".txt") :
                file1 = os.path.join(dirpath1, elem)
                file2 = os.path.join(dirpath2, elem)
                try:
                    result = filecmp.cmp(file1, file2)
                except: 
                    passed = False
                    print("FAILED :( -> File Not Found!")
                    print("in comparing: {} - {}".format(file1,file2))
                    break
                if not result:
                    passed = False
                    print("FAILED :(")
                    with open(file1, "r") as f1:
                        text1 = f1.readlines()
                    with open(file2, "r") as f2:
                        text2 = f2.readlines()
                    diff = difflib.unified_diff(text1, text2)
                    print("\n".join(diff))
                    break
    
    if passed :
        testCounter += 1
        print("PASSED :)")



if testCounter == NUM_OF_TESTS :
    print("\n\nGood Job! You've PASSED all the tests ")
else:
    print("\n\nYou've FAILED in {} tests... Keep going".format(NUM_OF_TESTS-testCounter))



#__________________________________________________________________________
#comment next lines to keep the output files

for num in range(NUM_OF_TESTS) :
    dirpath1 = os.path.join('tests', "test{}e".format(num))
    dirpath2 = os.path.join('tests', "test{}d".format(num))

    for file in os.listdir(dirpath1) :
        path = os.path.join(dirpath1, file)
        if file.endswith(".enc"):
            os.remove(path)
    for file in os.listdir(dirpath2) :
        path = os.path.join(dirpath2, file)
        if file.endswith(".json"):
            continue
        os.remove(path)
print("deleting files succeeded")