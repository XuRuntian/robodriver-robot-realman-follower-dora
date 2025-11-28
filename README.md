# robodriver-robot-realman-follower-dora
## Get Start
Clone the repository
```
git clone --recurse-submodules https://github.com/BAAI-EI-DATA/robodriver-robot-realman-follower-dora.git && cd robodriver-robot-realman-follower-dora
```
Install uv:
```
pip install uv
```
Create and activate a virtual environment for realman dora node:
```
uv venv .venv -p 3.9
source .venv/bin/activate
```
Install dependencies
```
uv pip install -e .[hardware]
```
Install the project to Robodriver
```
cd /path/to/your/RoboDriver
source .venv/bin/activate
cd /path/to/your/robodriver-robot-realman-follower-dora
uv pip install -e .
source .venv/bin/activate
```
Configure the dataflow.yml
```
cd /path/to/your/robodriver-robot-realman-follower-dora
cd dora
```
Open the dataflow.yml file, then modify the VIRTUAL_ENV path, as well as DEVICE_SERIAL, ARM_IP, and ARM_PORT. 
### Parameter explanation:

- VIRTUAL_ENV: The path of the virtual environment used by the realman dora node
- DEVICE_SERIAL: Serial number of the RealSense camera
- ARM_IP: IP of the robotic arm
- ARM_PORT: PORT of the robotic arm

## Start collecting
Activate environment
```
cd /path/to/your/RoboDriver
source .venv/bin/activate
```
Start Dora
```
dora up
```
Start dataflow
```
cd /path/to/your/robodriver-robot-realman-follower-dora
dora start dora/dataflow.yml --uv
```
Launch RoboXStudio
```
cd /path/to/your/RoboDriver
source .venv/bin/activate
python robodriver/scripts/run.py \
  --robot.type=realman_follower_dora 
```