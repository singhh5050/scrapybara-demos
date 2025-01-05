# Teleo

A lightweight desktop application that provides an interface for interacting with AI agents in virtual desktop environments. Teleo features a sleek, minimal UI with a command input system and integrated VNC viewer for real-time observation of agent actions.

## Features

- Transparent, frameless window design
- Always-on-top functionality for easy access
- WebSocket-based communication with AI agents
- Integrated VNC viewer for real-time desktop visualization
- Dynamic window resizing based on content
- Command input system for agent control

## Prerequisites

- Node.js (v14 or higher recommended)
- npm or yarn
- Scrapybara API key (get one at [scrapybara.com](https://scrapybara.com))

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Scrapybara/scrapybara-demos.git
cd scrapybara-demos/teleo
```

2. Install dependencies:

```bash
npm install
```

3. Create a `.env` file in the root directory:

```bash
SCRAPYBARA_API_KEY=your_api_key_here
```

## Development

To start the application in development mode:

```bash
npm start
```

## Building

To create a distributable package:

```bash
npm run make
```

This will create platform-specific packages in the `out` directory.

## Project Structure

- `index.js` - Main Electron process
- `index.html` - Application UI
- `package.json` - Project configuration and dependencies

## Technical Details

### Main Process (`index.js`)

The main process handles:

- Window management
- WebSocket connections
- IPC (Inter-Process Communication) between main and renderer processes
- Dynamic window resizing

### Renderer Process (`index.html`)

The renderer contains:

- User interface components
- Command input handling
- VNC viewer integration
- Status updates

## WebSocket Communication

The application communicates with AI agents through a WebSocket connection to `wss://api.playground.scrapybara.com/ws/chat`. Messages are exchanged in JSON format:

```javascript
{
  type: "stream_url" | "text" | "tool_result",
  content?: string,
  url?: string,
  output?: string,
  error?: string
}
```

## Configuration

Window configuration can be modified in `index.js`:

```javascript
{
  width: 400,
  height: 80,
  frame: false,
  transparent: true,
  webPreferences: {
    nodeIntegration: true,
    contextIsolation: false,
    devTools: true,
  }
}
```

## Roadmap

- [ ] Agent pause/resume
- [ ] Send screenshots
- [ ] Browse and upload local files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For support, please [create an issue](https://github.com/Scrapybara/scrapybara-demos/issues) in the repository.
