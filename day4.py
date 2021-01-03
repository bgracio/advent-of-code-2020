import re

def get_passport(passports_file):
	passport = ""
	passport_read = passports_file.readline()
	
	while passport_read != "\n" and passport_read:
		passport += passport_read
		passport_read = passports_file.readline()

	return passport


def is_valid(fields):
	valid_byr = False
	valid_iyr = False
	valid_eyr = False
	valid_hgt = False
	valid_hcl = False
	valid_ecl = False
	valid_pid = False
	
	for elem in fields:
		field = elem.split(":")
		
		if field[0] == "byr":
			valid_byr = int(field[1]) >= 1920 and int(field[1]) <= 2002
		elif field[0] == "iyr":
			valid_iyr = int(field[1]) >= 2010 and int(field[1]) <= 2020
		elif field[0] == "eyr":
			valid_eyr = int(field[1]) >= 2020 and int(field[1]) <= 2030
		elif field[0] == "hgt" and field[1].endswith("cm"):
			hgt_value = int(field[1][0:-2])
			valid_hgt = hgt_value >= 150 and hgt_value <= 193
		elif field[0] == "hgt" and field[1].endswith("in"):
			hgt_value = int(field[1][0:-2])
			valid_hgt = hgt_value >= 59 and hgt_value <= 76
		elif field[0] == "hcl":
			valid_hcl = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', field[1])
		elif field[0] == "ecl":
			valid_ecl = field[1] == "amb" or field[1] == "blu" or field[1] == "brn" or field[1] == "gry" or field[1] == "grn" or field[1] == "hzl" or field[1] == "oth"
		elif field[0] == "pid":
			valid_pid = len(field[1]) == 9 and int(field[1]) >= 0 and int(field[1]) <= 999999999
		else:
			pass

	return valid_byr and valid_iyr and valid_eyr and valid_hgt and valid_hcl and valid_ecl and valid_pid


def main():
	passports_file = open("day4_passports_1.txt", "r")
	passport = get_passport(passports_file)
	passports_valid = 0
	
	while passport:
		if is_valid(passport.replace(" ", "\n").split("\n")):
			passports_valid += 1

		passport = get_passport(passports_file)
	
	print("Valid passports: " + str(passports_valid))


if __name__ == "__main__":
	main()