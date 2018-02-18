package valid

import (
	"sync"
	"testing"
)

var validTreeTests = []struct {
	inStr string
	inLen int
	out   int
}{
	{"aabc", 5, 3},
}

func TestValidTree(t *testing.T) {
	for _, test := range validTreeTests {
		validCount := make(chan int, 100)
		wg := sync.WaitGroup{}
		wg.Add(1)
		go validTree(test.inStr, test.inLen, 4, validCount, wg)
		numValid := 0
		for valid := range validCount {
			numValid += valid
		}
		if numValid != test.out {
			t.Errorf("validtree(%v, %v) => %v. Expected %v\n", test.inStr, test.inLen, numValid, test.out)
		}
	}
}
