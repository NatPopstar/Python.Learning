def attempt_1(col_1, row_1, col_2, row_2):
	if row_1 == row_2 and col_1 == col_2 - 1:
		return "YES"
	elif row_1 == row_2 - 1 and col_1 == col_2 - 1:
		return "YES"
	elif row_1 == row_2 - 1 and col_1 == col_2:
		return "YES"
	elif row_1 == row_2 - 1 and col_1 == col_2 + 1:
		return "YES"
	elif row_1 == row_2 and col_1 == col_2 + 1:
		return "YES"
	elif row_1 == row_2 + 1 and col_1 == col_2 + 1:
		return "YES"
	elif row_1 == row_2 + 1 and col_1 == col_2:
		return "YES"
	elif row_1 == row_2 + 1 and col_1 == col_2 -1:
		return "YES"
	else:
		return "NO"


def attempt_2(col_1, row_1, col_2, row_2):
	if col_1 - 1 <= col_2 <= col_1 + 1 and row_1 - 1 <= row_2 <= row_1 + 1:
		return "YES"
	else:
		return "NO"


if __name__ == '__main__':
	col_1 = int(input())
	row_1 = int(input())
	col_2 = int(input())
	row_2 = int(input())
	print(attempt_2(col_1, row_1, col_2, row_2))
