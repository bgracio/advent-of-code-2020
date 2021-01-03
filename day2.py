def main():
	passwords = open("day2_passwords_1.txt", "r")
	num_valid_passwords = 0

	password = passwords.readline() # 3-7 r: mxvlzcjrsqst
	while password:
		password_split = password.split(":")
	
		password_rule = password_split[0] # 3-7 r
		password_rule_2 = password_rule.split(" ")
		password_rule_3 = password_rule_2[0].split("-")
	
		password_rule_min = int(password_rule_3[0]) # 3
		password_rule_max = int(password_rule_3[1]) # 7
	
		password_rule_char = password_rule_2[1] # r
	
		password_code = password_split[1].strip() # mxvlzcjrsqst
		if (password_code[password_rule_min-1] == password_rule_char) and (password_code[password_rule_max-1] != password_rule_char):
			num_valid_passwords += 1
	
		if (password_code[password_rule_min-1] != password_rule_char) and (password_code[password_rule_max-1] == password_rule_char):
			num_valid_passwords += 1
	
		password = passwords.readline()
	
	print("Valid passwords: " + str(num_valid_passwords))

if __name__ == "__main__":
	main()