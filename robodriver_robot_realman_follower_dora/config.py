import abc
from dataclasses import dataclass, field
from typing import Sequence, Dict

import draccus

# from operating_platform.robot.robots.com_configs.cameras import (
#     CameraConfig,
#     OpenCVCameraConfig,
# )

# from operating_platform.robot.robots.com_configs.motors import (
#     FeetechMotorsBusConfig,
#     MotorsBusConfig,
# )

# from operating_platform.robot.robots.configs import RobotConfig, ManipulatorRobotConfig

from lerobot.robots.config import RobotConfig

from lerobot.cameras import CameraConfig
from lerobot.cameras.configs import ColorMode
from lerobot.cameras.opencv import OpenCVCameraConfig
from lerobot.motors import Motor, MotorNormMode


@RobotConfig.register_subclass("realman_follower_dora")
@dataclass
class RealManFollowerDoraRobotConfig(RobotConfig):
    use_degrees = True
    norm_mode_body = MotorNormMode.DEGREES if use_degrees else MotorNormMode.RANGE_M100_100
 
    motors: Dict[str, Motor] = field(
        default_factory=lambda norm_mode_body=norm_mode_body: {
            "left_joint_1": Motor(1, "realman", norm_mode_body),
            "left_joint_2": Motor(2, "realman", norm_mode_body),
            "left_joint_3": Motor(3, "realman", norm_mode_body),
            "left_joint_4": Motor(4, "realman", norm_mode_body),
            "left_joint_5": Motor(5, "realman", norm_mode_body),
            "left_joint_6": Motor(6, "realman", norm_mode_body),
            "left_joint_7": Motor(7, "realman", norm_mode_body),
            "left_gripper": Motor(8, "realman", MotorNormMode.RANGE_0_100),# 范围需要修改

            "right_joint_1": Motor(9, "realman", norm_mode_body),
            "right_joint_2": Motor(10, "realman", norm_mode_body),
            "right_joint_3": Motor(11, "realman", norm_mode_body),
            "right_joint_4": Motor(12, "realman", norm_mode_body),
            "right_joint_5": Motor(13, "realman", norm_mode_body),
            "right_joint_6": Motor(14, "realman", norm_mode_body),
            "right_joint_7": Motor(15, "realman", norm_mode_body),
            "right_gripper": Motor(16, "realman", MotorNormMode.RANGE_0_100),# 范围需要修改

        }
    )

    cameras: Dict[str, CameraConfig] = field(
        default_factory=lambda: {
            "image_top": OpenCVCameraConfig(
                index_or_path=1,
                fps=30,
                width=640,
                height=480,
            ),
            "image_top_dep": OpenCVCameraConfig(
                index_or_path=2,
                fps=30,
                width=640,
                height=480,
            ),
            "image_left_wrist": OpenCVCameraConfig(
                index_or_path=3,
                fps=30,
                width=640,
                height=480,
            ),
            
            "image_left_wrist_dep": OpenCVCameraConfig(
                index_or_path=4,
                fps=30,
                width=640,
                height=480,
            ),
            "image_right_wrist": OpenCVCameraConfig(
                index_or_path=5,
                fps=30,
                width=640,
                height=480,
            ),
            "image_right_wrist_dep": OpenCVCameraConfig(
                index_or_path=6,
                fps=30,
                width=640,
                height=480,
            ),
        }
    )

    use_videos: bool = False

    microphones: Dict[str, int] = field(
        default_factory=lambda: {
        }
    )
    
    # super().__post_init__()