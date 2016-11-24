package main

import "fmt"

func main() {
	n := 10

	sum := 0
	for i := 1; i < n; i++ {
		if (i%3 == 0) || (i%5 == 0) {
			sum += i
		}
	}
	fmt.Printf("Answer for problem 1 is %d\n", sum)
}
