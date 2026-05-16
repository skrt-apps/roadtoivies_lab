import os
import sys
import streamlit.web.cli as stcli

# Force streamlit to read the correct absolute paths for the pages directory
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
    sys.exit(stcli.main())
