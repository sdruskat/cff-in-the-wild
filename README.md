# cff-in-the-wild

Analysis of Citation File Format files on GitHub.

This is an [SSI Collaborations Workshop 2022](https://software.ac.uk/cw22) hack day project 😍.

## Repository structure 🗂️

```
. (root)/                    You are here.
├─ code/                     
│  ├─ data-retrieval/        Code/software for data retrieval from GitHub
├─ data/                     The data we analyse
│  ├─ raw/                   NEVER MAKE THIS PUBLIC! DATA PRIVACY!
├─ output/
│  ├─ figures/               Figures for the presentation
```


## Introduction

The [Citation File Format](https://citation-file-format.github.io/) enables you to provide the citation metadata for your software in easy-to-read YAML files. There are now several thousand `CITATION.cff` files on GitHub alone.

This project looks at how these files are actually used: 

- Are they used correctly (i.e., do they conform to the format specifications)?
- Which versions of the format are used?
- What context are they used in, with what programming languages, licenses, etc.?

## Usage

A dataset with some thousand links to repositories containing `CITATION.cff` files are in [`data/cff_repositories`](data/cff_repositories.csv).

Some of the analyses are run in R, some in Python.

## Contributing ✏️

This is a collaborative project and we welcome suggestions and contributions. We hope one of the invitations below works for you, but if not, please let us know!

🏃 I'm busy, I only have 1 minute

- Tell a friend about the project!

⏳ I've got 5 minutes - tell me what I should do

- Suggest research ideas: what do you want to know about how Citation File Format files are used?

💻 I've got a few hours to work on this

- Take a look at the issues and see if there are any you can contribute to

🎉 I really want to help increase the community

- Organise a hackday to use or improve the code, documentation, or data in this project

Please [open a GitHub issue](https://github.com/sdruskat/cff-in-the-wild/issues/new/choose) to suggest a new idea or let us know about bugs.

## Licenses ⚖️

Software code and notebooks from this project are licensed under the open source [Apache License, v2.0](LICENSE) license. Project documentation and images are licensed under CC BY 4.0. Data produced by this project in the data/outputs directory is licensed under CC0. Other data included in this project from other sources remains licensed under its original license.

## Contributors 💖

See the [`CITATION.cff` file](CITATION.cff) :tada:.
