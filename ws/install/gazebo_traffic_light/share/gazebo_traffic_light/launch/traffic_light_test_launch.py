from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Include the empty world from gazebo_ros
    gazebo_ros_launch_dir = PathJoinSubstitution([
        FindPackageShare('gazebo_ros'),
        'launch'
    ])
    empty_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            gazebo_ros_launch_dir, '/gazebo.launch.py'
        ]),
        launch_arguments={
            'world': PathJoinSubstitution([
                FindPackageShare('gazebo_traffic_light'),
                'worlds', 'plugin_test.world'
            ]),
            'verbose': 'true',
        }.items()
    )

    return LaunchDescription([
        empty_world_launch
    ])
