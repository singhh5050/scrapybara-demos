# Website Copycat

An AI-powered tool that automatically replicates websites by generating single-file HTML replicas using Claude, Scrapybara, and Playwright. The tool captures both the visual appearance and layout of target websites, creating simplified versions with internal CSS and vanilla JavaScript.

## Features

- Automated website capture and replication
- Single-file output with no external dependencies
- Visual similarity verification through screenshots
- Automated browser interaction and testing
- Support for dynamic content through scrolling and timeouts

## Prerequisites

- Python 3.8+
- Poetry
- Scrapybara API key (get one at [scrapybara.com](https://scrapybara.com))
- Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Scrapybara/scrapybara-demos.git
cd scrapybara-demos/website-copycat
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

## Usage

Run the project using Poetry:

```bash
poetry run python main.py
```

Or for custom website replication:

```python
from website_copycat import WebsiteCopycat
import asyncio

async def main():
    copycat = WebsiteCopycat(
        scrapybara_api_key=os.getenv('SCRAPYBARA_API_KEY'),
        anthropic_api_key=os.getenv('ANTHROPIC_API_KEY')
    )

    try:
        await copycat.start()
        content, screenshot = await copycat.capture_website("https://example.com")
        await copycat.replicate_website(content, screenshot)
    finally:
        await copycat.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
```

## How It Works

1. **Instance Initialization**: Creates a Scrapybara instance and initializes a browser session using Playwright.

2. **Website Capture**:

   - Navigates to the target URL
   - Waits for dynamic content to load
   - Captures full-page screenshot and HTML content

3. **AI Analysis**:

   - Claude analyzes the website structure and appearance
   - Generates a single HTML file with internal CSS/JS
   - Verifies visual similarity through screenshots

4. **Tool Integration**:
   - `ComputerTool`: Handles browser interaction and screenshots
   - `BashTool`: Executes system commands
   - `EditTool`: Manages file creation and editing

## Configuration

### Environment Variables

Required environment variables in `.env`:

```bash
SCRAPYBARA_API_KEY=your_scrapybara_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Roadmap

- [ ] Chunk HTML content and generate website incrementally
- [ ] Parse image sources and pass to Claude semantically
- [ ] Interactive elements

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For support, please [create an issue](https://github.com/Scrapybara/scrapybara-demos/issues) in the repository.
