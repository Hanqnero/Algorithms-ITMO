package parser

import (
	"fmt"
	"strings"
)

func FormatToTypst(info ProblemInfo) string {
	var builder strings.Builder

	// Title
	builder.WriteString(fmt.Sprintf("= %s\n\n", info.Title))

	// Problem Text
	builder.WriteString(fmt.Sprintf("== Условие\n%s\n\n", info.ProblemText))

	// Input Description
	builder.WriteString(fmt.Sprintf("== Входные данные\n%s\n\n", info.InputDescription))

	// Output Description
	builder.WriteString(fmt.Sprintf("== Результат\n%s\n\n", info.OutputDescription))

	// Examples
	if len(info.Examples) > 0 {
		builder.WriteString("== Примеры\n")
		for _, example := range info.Examples {
			builder.WriteString(fmt.Sprintf("=== исходные данные\n```\n%s\n```\n\n", example.Input))
			builder.WriteString(fmt.Sprintf("=== результат\n```\n%s\n```\n\n", example.Output))
		}
	}

	builder.WriteString("== Успешная попытка\n")
	builder.WriteString("image(\"AC.jpg\")\n")

	return builder.String()
}
