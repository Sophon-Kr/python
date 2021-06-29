try:
    fh= open("myfile.txt","w")
    fh.write("this is my file for exception handling!!")
except IOError:
    print("ERROR: can't find file or read data")
else:
    print("written content in the file successfuly!!!")
    fh.close()
