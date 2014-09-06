import sys

#prints out results of the comparison
def reportStats(error,line_counter,report):
	report.write("#####################################\n")
	line_info = "Lines Compared: " + str(line_counter) + "\n"
	error_info = "Errors Found: " + str(error) + "\n"
	report.write(line_info)
	report.write(error_info)

#compares the files line by line
def compare(file1,file2, report):
	line_counter = 1
	errors = 0

	line1 = file1.readline()
	line2 = file2.readline()

	#read and compare lines until one or both of the files finish
	while(line1 != "" and line2 != ""):
		#if the are not equal write them to a file
		if(line1 != line2):
			reason = "Line " + str(line_counter) + " does not match: \n" + line1[0:-1] + " | " + line2 + "\n"
			report.write(reason)
			errors += 1
		line_counter += 1
		line1 = file1.readline()
		line2 = file2.readline()

	#make sure one of the files doesn't have more lines
	if(line1 != ""):
		while(line1 != ""):
			reason = "Line " + str(line_counter) + " does not match: \n" + line1[0:-1] + " | " + line2 + "\n"
			report.write(reason)
			errors += 1
			line_counter += 1
			line1 = file1.readline()
	elif(line2 != ""):
		while(line1 != ""):
			reason = "Line " + str(line_counter) + " does not match: \n" + line1[0:-1] + " | " + line2 + "\n"
			report.write(reason)
			errors += 1
			line_counter += 1
			line2 = file2.readline()

	return (errors,line_counter)



#takes in two files one of known answers and other of produced output
#answers and output are both one per line
def main():
	if(len(sys.argv) != 3):
		print("The program requires two input files")
		print(sys.argv)
		return False

	#open the two files
	file1 = open(sys.argv[1],'r')
	file2 = open(sys.argv[2],'r')

	#open a new file to write the differences to
	report = open("report.txt", 'w')

	results = compare(file1,file2,report)
	reportStats(results[0],results[1],report)
	print("The Program has finsished")


main()