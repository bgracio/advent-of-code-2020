def main():
	map_file = open("day3_trees_1.txt", "r")
	map = map_file.read().split()

	right_jump_1 = 1
	num_trees_1 = 0

	right_jump_2 = 3
	num_trees_2 = 0

	right_jump_3 = 5
	num_trees_3 = 0

	right_jump_4 = 7
	num_trees_4 = 0

	right_jump_5 = 1
	num_trees_5 = 0
	down_jump_5 = 2
	count_jump_5 = 0

	map.pop(0)

	for map_level in map:
		count_jump_5 += 1
	
		map_char_1 = map_level[right_jump_1 % len(map_level)]
		map_char_2 = map_level[right_jump_2 % len(map_level)]
		map_char_3 = map_level[right_jump_3 % len(map_level)]
		map_char_4 = map_level[right_jump_4 % len(map_level)]
		map_char_5 = map_level[right_jump_5 % len(map_level)]
	
		if map_char_1 == "#":
			num_trees_1 += 1
	
		if map_char_2 == "#":
			num_trees_2 += 1
	
		if map_char_3 == "#":
			num_trees_3 += 1
	
		if map_char_4 == "#":
			num_trees_4 += 1
	
		if (count_jump_5 % down_jump_5) == 0:
			right_jump_5 += 1
			if (map_char_5 == "#"):
				num_trees_5 += 1
	
		right_jump_1 += 1
		right_jump_2 += 3
		right_jump_3 += 5
		right_jump_4 += 7
	
	print("Number of trees: " + str(num_trees_1*num_trees_2*num_trees_3*num_trees_4*num_trees_5))

if __name__ == "__main__":
	main()