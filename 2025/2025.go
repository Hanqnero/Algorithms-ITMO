package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	for ; N > 0; N-- {
		var n, k int
		fmt.Scan(&n, &k)
		fmt.Println(solve1(n, k))
	}
}

func solve1(n, k int) int {
	bigTeams := n % k
	smallTeams := k - bigTeams
	// smallTeamSize
	m := n / k
	// C_(n)^(2)
	totalFights := (n - 1) * n / 2
	interTeamsSmall := m * (m - 1) / 2
	interTeamBig := (m + 1) * (m) / 2
	totalFights -= interTeamBig*bigTeams + interTeamsSmall*smallTeams
	return totalFights
}
