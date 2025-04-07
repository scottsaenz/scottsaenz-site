# Scott Saenz Personal Site

This is the source code for [scottsaenz.com](https://scottsaenz.com), a personal website built using [Docusaurus](https://docusaurus.io). The site serves as a platform to share blog posts, training plans, and personal updates.

## Features

- **Blog**: Weekly posts highlighting books, news, and ongoing projects.
- **Training Plans**: Advanced Python developer training plan and other resources.
- **About Me**: Learn more about Scott Saenz and his professional journey.

## Tech Stack

- **Framework**: [Docusaurus 2](https://docusaurus.io/)
- **Hosting**: Amazon S3
- **CI/CD**: GitHub Actions

## Development

### Prerequisites

- [Node.js](https://nodejs.org/) (version 16 or higher)
- [npm](https://www.npmjs.com/)

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/scottsaenz/scottsaenz-site.git
   cd scottsaenz-site
   ```
2. Install dependencies
```bash
npm install
```
3. Start the development server
```bash
npm run start
```  
This site will be available at `http://localhost:3000`
4. Build the site for production
```bash
npm run build
```
The static files will be generated in the `build` directory

**Deployment**  
The site is deployed to an Amazon S3 bucket using GitHub Actions. Any changes pushed to the main branch will trigger the deployment workflow.

**Contributing**
This is a personal project and not open for contributions at this time.

**License**
This project is licensed under the MIT License.

Built with ❤️ using Docusaurus.