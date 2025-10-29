"""Main entry point when running as a module (python -m src)."""

import sys
from .mcp_server_box import main

if __name__ == "__main__":
    sys.exit(main())
