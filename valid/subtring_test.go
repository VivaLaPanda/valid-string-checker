//written by Jeff Booher-Kaeding
package valid

import "testing"

var validSubStrTests = []struct {
	inStr   string
	outBool bool
}{
	{"abcc", true},
	{"aaaa", false},
	{"bccc", false},
	{"bacb", true},
	{"bbba", false},
	{"bcca", true},
}

func TestSubStr(t *testing.T) {
	for _, test := range validSubStrTests {
		output := SubStr(test.inStr)
		if test.outBool != output {
			t.Errorf("The substring broke, SubStr(%v) => %v. Expected %v", test.inStr, output, test.outBool)
		}
	}
}
