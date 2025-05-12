package downloader

import (
	"fmt"
	"io"
	"net/http"
	"strings"
)

const urlTemplate = "https://acm.timus.ru/problem.aspx?space=1&num=%d&locale=ru"

func DownloadProblemText(num int) (string, error) {
	url := fmt.Sprintf(urlTemplate, num)

	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Failed to fetch HTML:", err)
	}
	defer resp.Body.Close()

	buf := new(strings.Builder)

	_, err = io.Copy(buf, resp.Body)
	if err != nil {
		return "", err
	}

	return buf.String(), err
}
