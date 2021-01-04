import math

def main():
    puzzle_input = open("day5_boarding_passes_1.txt", "r")
    boarding_passes = puzzle_input.read().splitlines()
    #boarding_passes = ["BBFFBBFRLL"]

    highest_seat_id = 0
    for seat_codes in boarding_passes:
        seat_row_id_min = 0
        seat_row_id_max = 127

        seat_column_id_min = 0
        seat_column_id_max = 7

        for seat_code in seat_codes:
            if seat_code == "F":
                seat_row_id_max = seat_row_id_max - math.floor((seat_row_id_max - seat_row_id_min) / 2)
            elif seat_code == "B":
                seat_row_id_min = seat_row_id_min + math.ceil((seat_row_id_max - seat_row_id_min) / 2)
            elif seat_code == "L":
                 seat_column_id_max = seat_column_id_max - math.floor((seat_column_id_max - seat_column_id_min) / 2)
            elif seat_code == "R":
                seat_column_id_min = seat_column_id_min + math.ceil((seat_column_id_max - seat_column_id_min) / 2)
        
        seat_id = (seat_row_id_min * 8) + seat_column_id_min
        if highest_seat_id < seat_id:
            highest_seat_id = seat_id

    print("Highest Seat Id: " + str(highest_seat_id))


if __name__ == "__main__":
	main()