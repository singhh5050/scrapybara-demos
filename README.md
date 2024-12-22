<div id="toc" align="center">
  <ul style="list-style: none">
    <summary>
      <h1><img src="images/wow.gif" alt="Scrapybara" width="24"> Scrapybara Demos <img src="images/wow.gif" alt="Scrapybara" width="24"></h1>
    </summary>
  </ul>
</div>

<p align="center">
  Official Scrapybara demos as seen on <a href="https://x.com/scrapybara">X</a>
</p>

<p align="center">
  <a href="https://github.com/scrapybara/scrapybara-playground/blob/main/license"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue" /></a>
  <a href="https://discord.gg/s4bPUVFXqA"><img alt="Discord" src="https://img.shields.io/badge/Discord-Join%20the%20community-yellow.svg?logo=discord" /></a>
</p>

## Demos

### W25 - Dec 22, 2024

- Learn how to use the new agent endpoints (act, scrape).
- Scrape YC W25 companies, find the best way to contact them, and draft messages to them.

```bash
cd w25
poetry run python main.py
```

## Local Development

### Prerequisites

- Python 3.11 or higher
- Poetry

### Installation

1. Clone the repository

```bash
git clone https://github.com/scrapybara/scrapybara-playground.git
cd scrapybara-playground
```

2. Install dependencies using Poetry

```bash
poetry install
```

3. Set up environment variables

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration:

```env
SCRAPYBARA_API_KEY=""
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
