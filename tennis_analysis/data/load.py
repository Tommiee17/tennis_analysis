from roboflow import Roboflow
import sys
from pathlib import Path

sys.path.append("./..")

from dotenv import load_dotenv
load_dotenv()
import os 

api_key_robo_flow = os.environ("API_KEY_ROBO_FLOW")
workspace_robo_flow = os.environ("WORKSPACE_ROBO_FLOW")
project_robo_flow = os.environ("PROJECT_ROBO_FLOW")
version_robo_flow = os.environ("VERSION_ROBO_FLOW")


rf = Roboflow(api_key=api_key_robo_flow)
project = rf.workspace(workspace_robo_flow).project(project_robo_flow)
version = project.version(version_robo_flow)

# Resolve to "<project_root>/data/raw" no matter where this script is run from.
project_root = Path(__file__).resolve().parents[2]
download_dir = project_root / "data" / "raw"
download_dir.mkdir(parents=True, exist_ok=True)

dataset = version.download("yolo26", location=str(download_dir))
