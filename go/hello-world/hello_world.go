// Package hello_world contains a function to return a generic or
// custom greating
package greeting

import "fmt"

// testVersion identifies the version of the test program that you are
// writing your code to. If the test program changes in the future --
// after you have posted this code to the Exercism site -- nitpickers
// will see that your code can't necessarily be expected to pass the
// current test suite because it was written to an earlier test version.
const testVersion = 3

// HelloWorld returns a generic greating if an empty string is passed in
// of a greating that includes the passed in string
func HelloWorld(name string) string {
	if name == "" {
		return "Hello, World!"
	} else {
		return fmt.Sprintf("Hello, %s!", name)
	}
}
