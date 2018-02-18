package valid

func SubStr(str string) bool {
	//check for valid substring

	//DFA statetable, -1 is our ending/return state
	//a -1 would mean that the substring is valid
	state := 0
	if len(str) != 4 {
		panic("Length of str is invalid")
	}
	for _, ele := range str { //ele = the char
		switch ele {
		case 'a':
			state = stateTable[state][0]
		case 'b':
			state = stateTable[state][1]
		case 'c':
			state = stateTable[state][2]
		}
		if state == -1 {
			return true
		}
	}

	return false
}

var stateTable = [][]int{
	//inputs
	//	A,	B,	C		//current state
	{1, 4, 7},  //0
	{1, 2, 3},  //1
	{2, 2, -1}, //2
	{3, -1, 3}, //3
	{5, 4, 6},  //4
	{5, 5, -1}, //5
	{-1, 6, 6}, //6
	{8, 9, 7},  //7
	{8, -1, 8}, //8
	{-1, 9, 9}, //9
}
