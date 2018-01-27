# Raven PDF Generator

This project aims to facilitate the creation of Raven stylized PDF files from Markdown.

It uses Pandoc with a modified template from [this one](https://github.com/Wandmalfarbe/pandoc-latex-template).

## Requirement

Dependencies:

* Python3
* Pandoc

Run the following command to download the required python modules:

```bash
pip install -r ./requirement.txt
```

## Howto

To generate a pdf document from a markdown file:

```bash
./doc-generator.py -f input.md output.pdf
```

To generate a pdf document from an an url:

```bash
./doc-generator.py -u http://input.md output.pdf
```

The document must start with some metadata that must follow this pattern:

```yaml
---
title: "Document Title"
accountant: [John Doe]
version: 1.0.0
history: [
        {
                author: "John Doe",
                date: "27 Oct 2017",
                version: "1.0.0",
                sections: "All document",
                comments: "Fixed some typos",
        },
        {
                author: "John Doe",
                date: "28 Oct 2018",
                version: "1.1.0",
                sections: "1.3",
                comments: "Added section 1.3: installation guide",
        },
]
lang: fr-FR
...

```

The document can contain an abstract between the `Abstract` and `EndAbstract` headers:

```markdown
#Abstract

This is the abstract of the document

#EndAbstract

#1. Part One

Content of part one
```

## Bugs?

Did you find any bugs? Feel free to fill an issue!
