package main

import (
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/hanqnero/timusformat/internal/downloader"
	"github.com/hanqnero/timusformat/internal/parser"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: formatter <problem>")
		return
	}

	num, err := strconv.Atoi(os.Args[1])
	if err != nil {
		panic(err)
	}

	body, err := downloader.DownloadProblemText(num)
	if err != nil {
		panic(err)
	}

	problemData, err := parser.ExtractProblemInfo(body)
	if err != nil {
		log.Fatal("Failed to extract problem info:", err)
	}

	typstText := parser.FormatToTypst(problemData)

	fmt.Println(typstText)
}
