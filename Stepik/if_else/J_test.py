import J

ROW = COL = 4
test_attemps = [J.attempt_1, J.attempt_2]

for func in test_attemps:
	print(f'TEST {func.__name__}')
	for row in range(ROW - 2, ROW + 3):
		if row < 0 or row > 8:
			continue
		for col in range(COL - 2, COL + 3):
			if col < 0 or col > 8:
				continue
			result = func(COL, ROW, col, row)
			expected = "YES" if abs(col - COL) <= 1 and abs(row - ROW) <= 1 else "NO"
			print(f'{COL}{ROW}{col}{row} {"FAILED" if result != expected else "OK"} expected: {expected}, actual: {result}')
	print()
