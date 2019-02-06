print("Program that opens the file 'CPLX2.txt' and print all the data contained in it.")

CPLX2_file = open("CPLX2.txt", "r")
read_info = CPLX2_file.read()
CPLX2_file.close()
print(read_info)