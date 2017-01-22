// Leap stub file

// The package name is expected by the test program.
package leap

// testVersion should match the targetTestVersion in the test file.
const testVersion = 3

// It's good style to write a comment here documenting IsLeapYear.
func IsLeapYear(year int) bool {
	// Write some code here to pass the test suite.
	if year % 400 == 0 {
		return true
	} else if year % 4 == 0 && year % 100 != 0 {
		return true
	}	else {
		return false
	}
}
