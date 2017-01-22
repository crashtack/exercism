// Leap
// A function to determine if a year is a leap year or not

// The package name is expected by the test program.
package leap

// testVersion should match the targetTestVersion in the test file.
const testVersion = 3

// Returns true if the inputted year is a leap year
func IsLeapYear(year int) bool {
	if year%400 == 0 {
		return true
	} else if year%4 == 0 && year%100 != 0 {
		return true
	} else {
		return false
	}
}
