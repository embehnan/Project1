import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	myfile=open(file,'r')
	headers=myfile.readline().strip().split(',')
	final_lst=[]
	for line in myfile.readlines():
		d={}
		index=0
		data_lst=line.strip().split(',')
		for keys in headers:
			d[keys]=data_lst[index]
			index +=1
		final_lst.append(d)
	return final_lst




#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	sorted_data=sorted(data,key=lambda x:x[col])
	firstName=sorted_data[0]["First"]
	lastName=sorted_data[0]["Last"]
	return firstName + " " + lastName

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	class_size= {}
	for student in data:
		if student["Class"] not in class_size:
			class_size[student["Class"]]= 1
		else:
			class_size[student["Class"]] +=1

	class_size_list=class_size.items()
	class_size_list=sorted(class_size_list, key=lambda x:x[1], reverse=True)
	return class_size_list




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	dates_dict = {}
	for x in a:
		date = x['DOB'].split('/')[1]
		if date not in dates_dict.keys():
			dates_dict[date] = 1
		else:
			dates_dict[date] += 1
	sorted_dates = sorted(dates_dict, key = dates_dict.get, reverse = True)
	return int(sorted_dates[0])




# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:

	lst_of_ages=[]
	for dct in a:
		day=int(dct['DOB'].split('/')[0])
		month=int(dct['DOB'].split('/')[1])
		year=int(dct['DOB'].split('/')[2])
		if month <=9:
			age= 2017-year+1
		if month > 9:
			age= 2017-year
		lst_of_ages.append(age)
	years= 0
	for age in lst_of_ages:
		years +=age
	return int(years/len(lst_of_ages))



#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	pass



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
