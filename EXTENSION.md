# Box MCP Server - Gemini CLI Extension

This is an integration of [mcp-server-box](https://github.com/box-community/mcp-server-box) as a Gemini CLI built-in extension.

## Features

The Box MCP Server provides comprehensive Box cloud storage integration capabilities:

- **AI-Powered**: AI-powered file and hub queries
- **File Operations**: Read, upload, download files
- **Folder Management**: List, create, delete, update folders
- **Collaboration**: Manage file/folder collaborations
- **Document Generation**: Document generation and template management
- **Search**: Advanced search for files and folders
- **Metadata Management**: Metadata template and instance management
- **Shared Links**: Shared link management for files/folders/web-links
- **Tasks**: Task and task assignment management
- **Users & Groups**: User and group management
- **Web Links**: Web link creation and management

## How It Works

This extension integrates the Python-based Box MCP Server into Gemini CLI:

1. **Automatic Installation**: When you run `npm install`, the `postinstall` script automatically installs all Python dependencies using the embedded Python 3.13.7
2. **Zero Configuration**: The extension is automatically loaded by Gemini CLI's extension system
3. **MCP Server**: Runs as an MCP server using stdio transport for Box cloud operations

## File Structure

```
mcp-server-box/
├── src/
│   └── mcp_server_box.py      # Main Python server
├── docs/                       # Tool documentation
├── gemini-extension.json       # Extension configuration
├── package.json               # NPM package configuration
├── install-deps.js            # Automatic dependency installer
└── EXTENSION.md              # This file
```

## Usage

Once installed, you can use Box tools through Gemini CLI:

### Example Commands (via LLM)

- "List all files in my Box root folder"
- "Upload file.txt to my Box account"
- "Search for documents containing 'budget'"
- "Share folder with user@example.com"
- "Create a new folder called 'Q4 Reports'"

## Environment Variables

The extension requires Box authentication. Set the following environment variables:

### Using OAuth2.0 with a Box App
```
BOX_CLIENT_ID = YOUR_CLIENT_ID
BOX_CLIENT_SECRET = YOUR_CLIENT_SECRET
BOX_REDIRECT_URL = http://localhost:8000/callback
BOX_MCP_SERVER_AUTH_TOKEN = YOUR_BOX_MCP_SERVER_AUTH_TOKEN
```

### Using CCG with a Box App
```
BOX_CLIENT_ID = YOUR_CLIENT_ID
BOX_CLIENT_SECRET = YOUR_CLIENT_SECRET
BOX_SUBJECT_TYPE = user_or_enterprise
BOX_SUBJECT_ID = YOUR_USER_OR_ENTERPRISE_ID
BOX_MCP_SERVER_AUTH_TOKEN = YOUR_BOX_MCP_SERVER_AUTH_TOKEN
```

## Available Tools

The extension provides the following tool categories:

- **box_tools_ai**: AI-powered file and hub queries
- **box_tools_collaboration**: Manage file/folder collaborations
- **box_tools_docgen**: Document generation and template management
- **box_tools_files**: File operations (read, upload, download)
- **box_tools_folders**: Folder operations (list, create, delete, update)
- **box_tools_generic**: Generic Box API utilities
- **box_tools_groups**: Group management and queries
- **box_tools_metadata**: Metadata template and instance management
- **box_tools_search**: Search files and folders
- **box_tools_shared_links**: Shared link management
- **box_tools_tasks**: Task and task assignment management
- **box_tools_users**: User management and queries
- **box_tools_web_link**: Web link creation and management

See [docs/](docs/) for complete documentation of all available tools.

## Dependencies

Python dependencies (automatically installed):
- box-ai-agents-toolkit >= 0.1.1
- fastapi >= 0.119.1
- mcp[cli] >= 1.18.0
- python-dotenv >= 1.1.1
- tomli >= 2.3.0

## Platform Support

- ✅ Windows (win32)
- ✅ macOS (darwin)
- ✅ Linux

## License

This extension integrates the original mcp-server-box which is licensed under MIT License.
