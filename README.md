# Quarto Template

My Quarto template for documents (articles, reports, etc.).

## Requirements

- [Quarto](https://quarto.org/docs/get-started)
- Optional: [entr](https://github.com/eradman/entr) (Linux only)

## Setup

If you don't have a [TeX](https://www.latex-project.org/get/#tex-distributions) installation present on your system the following needs to be exected once after the installation of Quarto:

`quarto install tinytex`

## Run

Render the entire project:

`quarto render`

### Live Reload

Automatically rerender the entire project if any *.qmd file changes
(requires *entr*).

`ls **/*.qmd | entr quarto render`

## Output

The output file (by default a PDF) is in the `_output` directory.
