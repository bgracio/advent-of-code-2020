def main():
	expense_report = open("day1_expense_report_1.txt", "r")
	list_of_values = expense_report.read().splitlines()

	while len(list_of_values) > 0:
		val1 = list_of_values.pop(0)
		for p2 in range(0, len(list_of_values)):
			for p3 in range(1, len(list_of_values)):
				val1_int = int(val1)
				val2_int = int(list_of_values[p2])
				val3_int = int(list_of_values[p3])
				if val1_int + val2_int + val3_int == 2020:
					print("Result is " + str(val1_int * val2_int * val3_int))
					exit()

	print("No result were found")

if __name__ == "__main__":
	main()