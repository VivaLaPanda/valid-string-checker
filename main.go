package main

import (
	"fmt"
)

func main() {
	for true {
		fmt.Printf("Would you like to solve problem 1, or porblem 2 \nProblem #:")
		var i int
		fmt.Scan(&i)
		if 0 > i && i > 3 {
			fmt.Printf("invalid Problem number, please chose 1 or 2")
			return
		}
		fmt.Println("you chose to solve problem ", i)

		if i == 1 {
			fmt.Printf("please pick a number between the rang of 1 and 300 for n")
			fmt.Scan(&i)
			if 0 > i && i >= 300 {
				fmt.Printf("invalid n number, please chose a number between 1 and 300")
				return

			}

		}
		if i == 2 {
			//

		}

	}
}
