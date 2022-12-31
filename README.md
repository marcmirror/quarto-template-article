# Quarto Template

My Quarto template.

## Requirements

- [Quarto](https://quarto.org/docs/get-started)
- Optional: [entr](https://github.com/eradman/entr)

## Run

Render the entire project:

`quarto render`

### Live Reload

Automatically rerender the entire project if any *.qmd file changes
(requires *entr*).

`ls **/*.qmd | entr quarto render`

## Output

The output file (by default a PDF) is in the `_output` directory.
