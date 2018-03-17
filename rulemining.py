# Find all association rules in QLD crash data

from apyori import apriori
import csv
import sys

def floatToStr(num):
	return "{0:.2f}".format(num)

# Input: rules = order_statistic of RelationRecord
# Output: Prints all rules
def printRules(rules):
	for rule in rules:
		antecedent = list(rule.items_base)
		consequent = list(rule.items_add)

		if len(antecedent) > 0:
			print "Confidence " + floatToStr(rule.confidence) + ":" + \
				str(antecedent) + " => " + str(consequent)

def printAllRules(results):
	for result in results:
		rules = result.ordered_statistics
		printRules(rules)

def printFrequentItems(results):
	for result in results:
		print "Support " + floatToStr(result.support) + ":" + str(list(result.items))

def printAll(results):
	for result in results:
		print result

def parseFactorsCSV(csvFile):
	factorsColumns = ["Drinking", "Speeding", "Fatigue", "Defective"]
	crashes = []
	for row in csvFile:
		crash = [row[2]] #row[2] = severity
		drinking = row[3]
		speed = row[4]
		fatigue = row[5]
		defective = row[6]

		if drinking == "Yes":
			crash.append("Drinking")
		if speed == "Yes":
			crash.append("Speeding")
		if fatigue == "Yes":
			crash.append("Fatigue")
		if defective == "Yes":
			crash.append("Defective")

		crashes.append(crash)
	return crashes

def parseDemographicsCSV(csvFile):
	demographicsCol = ["Male", "Female", "Young", "Senior", 
		"Provisional", "Overseas", "Unlicensed"]
	crashes = []
	for row in csvFile:
		crash = [row[2]] #row[2] = severity
		for i in range(3, 10):
			if row[i] == "Yes":
				crash.append(demographicsCol[i - 3])

		crashes.append(crash)

	return crashes


##----------------------------------------------------------##


if __name__ == "__main__":
	fileName = sys.argv[1]
	min_sup = float(sys.argv[2])
	min_conf= float(sys.argv[3])

	crashes = []
	file = ""
	if fileName == "factors":
		file = "factorsinroadcrashes.csv"
	if fileName == "demographics":
		file = "driverdemographics.csv"

	csvFile = csv.reader(open(file, "rU"), delimiter=",")

	if fileName == "factors":
		crashes = parseFactorsCSV(csvFile)
	if fileName == "demographics":
		crashes = parseDemographicsCSV(csvFile)

	results = list(apriori(crashes, min_support=min_sup, min_confidence=min_conf))
	
	#printAll(results)

	print "Frequent Items:-------------"
	printFrequentItems(results)
	print " "

	print "Association Rules:------------"
	printAllRules(results)

