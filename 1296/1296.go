package main

import (
	"fmt"
	"math"
)

func Kadane(arr []int) (best_sum int) {
	var current_sum int
	for _, x := range arr {
		current_sum = math.Max(x, current_sum+x)
		best_sum = math.Max(best_sum, current_sum)
	}
	return
}

func main() {
	var n, x int
	fmt.Scan(&n)
	arr := make([]int, n)
	for ; n > 0; n-- {
		fmt.Scan(&x)
		arr = append(arr, x)
	}
	fmt.Println(Kadane(arr))
}
