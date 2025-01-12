# AI Resume Builder

An automated resume tailoring system that uses LinkedIn job postings to generate customized resumes. The tool uses Scrapybara, Playwright, and Claude to analyze job requirements and create professionally formatted resumes optimized for ATS systems.

## Features

- Automated LinkedIn job posting analysis
- AI-powered resume customization
- ATS-friendly resume generation
- LaTeX output compatible with Overleaf

## Prerequisites

- Python 3.8+
- Poetry
- Scrapybara API key (get one at [scrapybara.com](https://scrapybara.com))
- Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))
- LinkedIn account

## Installation

1. Clone the repository:

```bash
git clone https://github.com/scrapybara/scrapybara-demos
cd resume-builder
```

2. Install dependencies with Poetry:

```bash
poetry install
```

3. Create a `.env` file in the root directory:

```bash
SCRAPYBARA_API_KEY=your_scrapybara_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## LinkedIn Authentication

To use LinkedIn job search functionality, you need to authenticate your session.

You can set up authentication by going to the Auth section in your Scrapybara dashboard.

Save this auth_state_id for future use in your .env file:

```bash
AUTH_STATE_ID=your_auth_state_id_here
```

## Usage

Run the project using Poetry:

```bash
poetry run python main.py
```

The script will:

1. Start a Scrapybara instance
2. Initialize an authenticated LinkedIn session
3. Scrape a software engineering job posting
4. Generate a tailored resume using Claude
5. Output the resume in LaTeX format

### Using the Generated Resume

1. The script generates `tailored_resume.tex` in the output directory
2. Upload this file to [Overleaf](https://www.overleaf.com)
3. Compile the LaTeX document to create a professionally formatted PDF
4. Make any desired adjustments to the formatting or content

### Custom Job Search

You can modify the job search URL in the code:

```python
await page.goto("https://www.linkedin.com/jobs/search/?keywords=your+search+terms")
```

## How It Works

1. **Instance Initialization**: Creates a Scrapybara instance and starts a browser session with authenticated LinkedIn access.

2. **Job Analysis**:

   - Navigates to LinkedIn jobs
   - Captures job posting content
   - Extracts key requirements and skills

3. **Resume Generation**:

   - Claude analyzes job requirements
   - Creates tailored resume content
   - Formats output in LaTeX

4. **Tool Integration**:
   - Playwright: Handles browser automation
   - Scrapybara: Manages virtual desktop instance
   - Claude: Performs job analysis and resume generation

## Configuration

### Environment Variables

Required in `.env`:

```bash
SCRAPYBARA_API_KEY=your_scrapybara_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
AUTH_STATE_ID=your_auth_state_id
```

### Instance Settings

The script uses a small instance type by default:

```python
instance = scrapybara.start(instance_type="small")
```

## Customization

### LaTeX Template

The generated LaTeX uses a professional template optimized for ATS systems. You can customize the template by modifying the prompt sent to Claude in the code:

```python
prompt = """Analyze this job posting and create a professional resume in LaTeX format..."""
```

## Support

For support, please create an issue in the repository or reach out on Discord.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT
