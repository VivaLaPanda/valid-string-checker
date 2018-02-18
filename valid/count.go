package valid

import (
	"sync"
	"unicode/utf8"
)

func Count(strLength int) (numValid int) {
	if strLength < 4 {
		return 0
	}

	return 0
}

// Takes as input a known valid 4 character string and recursively adds
// characters to the string until we reach the max size
func validTree(substr string, maxLength int, depth int, numValid chan int, parentWg sync.WaitGroup) {
	defer parentWg.Done()
	if depth > maxLength {
		return
	}

	_, size := utf8.DecodeRuneInString(substr)
	lastThree := substr[size:]
	substrA := lastThree + "a"
	substrB := lastThree + "b"
	substrC := lastThree + "c"

	wg := sync.WaitGroup{}

	if SubStr(substrA) {
		wg.Add(1)
		numValid <- 1
		go validTree(substrA, maxLength, depth+1, numValid, wg)
	}

	if SubStr(substrB) {
		wg.Add(1)
		numValid <- 1
		go validTree(substrB, maxLength, depth+1, numValid, wg)
	}

	if SubStr(substrC) {
		wg.Add(1)
		numValid <- 1
		go validTree(substrC, maxLength, depth+1, numValid, wg)
	}

	wg.Wait()

	return
}
