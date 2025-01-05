# DCSS Game Agent

An AI-powered agent that autonomously plays Dungeon Crawl Stone Soup (DCSS) using Claude, Scrapybara, and virtual desktop automation. The agent creates characters, explores dungeons, fights monsters, and makes strategic decisions in real-time.

## Features

- Automated DCSS gameplay using Claude AI
- Real-time game state analysis
- Autonomous decision making
- Visual interface interaction
- Continuous gameplay loop with exit handling

## Prerequisites

- Python 3.8+
- Poetry
- Scrapybara API key (get one at [scrapybara.com](https://scrapybara.com))
- Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Scrapybara/scrapybara-demos.git
cd scrapybara-demos/dcss-agent
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

Or integrate the agent into your own project:

```python
from game_agent import GameAgent
import asyncio

async def main():
    agent = GameAgent(
        scrapybara_api_key=os.getenv('SCRAPYBARA_API_KEY'),
        anthropic_api_key=os.getenv('ANTHROPIC_API_KEY')
    )

    try:
        agent.start()
        await agent.play_game()
    finally:
        agent.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
```

## How It Works

1. **Instance Initialization**:

   - Creates a Scrapybara instance with a virtual desktop
   - Installs DCSS using apt-get
   - Launches the game with graphical interface

2. **Game Interaction**:

   - Uses keyboard commands for movement and actions
   - Analyzes game state through screenshots
   - Makes strategic decisions based on visual feedback

3. **AI Decision Making**:

   - Claude analyzes the game screen
   - Chooses appropriate actions based on context
   - Maintains game state awareness
   - Responds to events and combat situations

4. **Tool Integration**:
   - `ComputerTool`: Handles keyboard/mouse input and screenshots
   - `BashTool`: Manages game installation and launching
   - `EditTool`: Processes game text and output

## Game Controls

The AI agent understands and uses standard DCSS controls:

- Movement: yuhjklbn (8 directions)
- Actions:
  - `?` - Help
  - `i` - Inventory
  - `g` - Pick up items
  - `f` - Fire ranged weapon
  - `q` - Quaff potion
  - `r` - Read scroll

## Configuration

### Environment Variables

Required environment variables in `.env`:

```bash
SCRAPYBARA_API_KEY=your_scrapybara_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### Game Settings

The agent uses a large instance type for better performance:

```python
self.instance = self.scrapybara.start(instance_type="large")
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For support, please [create an issue](https://github.com/Scrapybara/scrapybara-demos/issues) in the repository.

## Game Information

[Dungeon Crawl Stone Soup](https://crawl.develz.org/) is a roguelike adventure game where players explore randomly generated dungeons, fight monsters, and attempt to retrieve the Orb of Zot. The game features:

- Turn-based gameplay
- Complex character development
- Procedurally generated levels
- Permadeath mechanics
- Rich tactical combat
