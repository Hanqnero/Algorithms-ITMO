package parser

import (
	"strings"

	"github.com/PuerkitoBio/goquery"
)

type ProblemInfo struct {
	Title             string
	ProblemText       string
	InputDescription  string
	OutputDescription string
	Examples          []Example
}

type Example struct {
	Input  string
	Output string
}

// extractProblemInfo now accepts an io.Reader
func ExtractProblemInfo(body string) (ProblemInfo, error) {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(body))
	if err != nil {
		return ProblemInfo{}, err
	}

	info := ProblemInfo{}

	// Problem title
	info.Title = doc.Find("h2.problem_title").Text()

	// Problem text
	info.ProblemText = doc.Find("div#problem_text div.problem_par_normal").First().Text()

	// Sections: Input, Output, Example
	doc.Find("h3.problem_subtitle").Each(func(i int, s *goquery.Selection) {
		sectionTitle := s.Text()
		if sectionTitle == "Исходные данные" { // Input
			// Find the next div with class 'problem_par' and then get the text from 'problem_par_normal'
			problemPar := s.NextFiltered("div.problem_par")
			if problemPar.Length() > 0 {
				info.InputDescription = problemPar.Find("div.problem_par_normal").Text()
			}
		} else if sectionTitle == "Результат" { // Output
			// Find the next div with class 'problem_par' and then get the text from 'problem_par_normal'
			problemPar := s.NextFiltered("div.problem_par")
			if problemPar.Length() > 0 {
				info.OutputDescription = problemPar.Find("div.problem_par_normal").Text()
			}
		} else if sectionTitle == "Пример" { // Example
			table := s.NextFiltered("table.sample")
			if table.Length() > 0 {
				table.Find("tr").Each(func(i int, tr *goquery.Selection) {
					if i == 1 { // Skip header row
						input := tr.Find("td").Eq(0).Find("pre").Text()
						output := tr.Find("td").Eq(1).Find("pre").Text()
						info.Examples = append(info.Examples, Example{
							Input:  strings.TrimSpace(input),
							Output: strings.TrimSpace(output),
						})
					}
				})
			}
		}
	})

	return info, nil
}
