# Scott Saenz Personal Site

This is the source code for [scottsaenz.com](https://scottsaenz.com), a personal website built using [MkDocs](https://www.mkdocs.org/).

## Features

- **Blog**: Weekly posts highlighting books, news, and ongoing projects.
- **Training Plans**: Advanced Python developer training plan and other resources.
- **About Me**: Learn more about Scott Saenz and his professional journey.

## Tech Stack

- **Framework**: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- **Hosting**: Amazon S3
- **CI/CD**: GitHub Actions

## Development

### Prerequisites

- [Python 3.7+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

### Getting Started

1. Install MkDocs and Material theme:
   ```bash
   pip install mkdocs-material
   ```
2. Serve the site locally:
   ```bash
   mkdocs serve
   ```
   The site will be available at `http://localhost:8000`
3. Build the site for production:
   ```bash
   mkdocs build
   ```
   The static files will be generated in the `site` directory.

**Deployment**  
The site is deployed to an Amazon S3 bucket using GitHub Actions. Any changes pushed to the main branch will trigger the deployment workflow.

**Contributing**
This is a personal project and not open for contributions at this time.

**License**
This project is licensed under the MIT License.

Built with ❤️ using MkDocs.