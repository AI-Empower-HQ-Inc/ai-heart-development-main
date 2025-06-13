# AI Empower Heart Development

![CI/CD Workflow](https://github.com/AI-Empower-HQ-360/ai-heart-development-main/actions/workflows/ci.yml/badge.svg)
![Enhanced CI/CD](https://github.com/AI-Empower-HQ-360/ai-heart-development-main/actions/workflows/enhanced-ci.yml/badge.svg)

## About

AI Empower Heart is a spiritual guidance platform powered by artificial intelligence. It provides personalized guidance through various AI gurus specializing in different aspects of spiritual development.

## Development

This project uses GitHub Actions for continuous integration and deployment.

### Setup

1. Clone the repository
2. Install dependencies
   - Python: `pip install -r requirements.txt`
   - Node.js (if applicable): `npm install`

### Testing

- Run Python tests: `pytest`
- Run linting: `flake8`

## Environment Setup

1. Copy the example environment file:

   ```bash
   cp backend/.env.example backend/.env
   ```

2. Configure your environment variables in `.env`:
   - Set your OpenAI API key
   - Set your secret key
   - Configure other environment-specific settings

3. For Google Cloud Services integration:

   ```bash
   cp key.example.json key.json
   ```

   Then update `key.json` with your Google Cloud service account credentials.

> ⚠️ Important: Never commit `.env` or `key.json` files to version control. These files contain sensitive information and are excluded in `.gitignore`.

## Security

This project uses Dependabot to keep dependencies up to date and secure.

## License

[Add your license information here]
