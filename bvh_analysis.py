from bvh import Bvh
import matplotlib.pyplot as plt

# Read the BVH file and parse it
with open("BVH-Recording1.bvh") as f:
    bvh = f.read()

# Parse the BVH data
bvh = Bvh(bvh)

# Find the number of frames
num_frames = bvh.nframes
frame_time = bvh.frame_time

# Calculate the total duration
total_duration = num_frames * frame_time

# Print the number of frames
print(f"Number of frames: {num_frames}")
print(f"Frame time: {frame_time} seconds")
print(f"Total duration: {total_duration} seconds")

# Extract joint names
joint_names = [joint.name for joint in bvh.get_joints()]

# Print the hierarchy
print("\nHierarchy:")
for joint in bvh.get_joints():
    print(joint.name)
    if joint.parent:
        print(f"  Parent: {joint.parent.name}")
    print("  Channels:")
    for channel in joint.channels:
        print(f"    {channel}")

# Function to extract joint rotations
def extract_joint_rotations(bvh_data, joint_name):
    x_rotations = []
    y_rotations = []
    z_rotations = []
    for frame in range(bvh_data.nframes):
        try:
            x_rotations.append(float(bvh_data.frame_joint_channel(frame, joint_name, 'Xrotation')))
            y_rotations.append(float(bvh_data.frame_joint_channel(frame, joint_name, 'Yrotation')))
            z_rotations.append(float(bvh_data.frame_joint_channel(frame, joint_name, 'Zrotation')))
        except ValueError as e:
            print(f"Error: {e}")
            print(f"Available channels for joint '{joint_name}': {bvh_data.joint_channels(joint_name)}")
            break
    return x_rotations, y_rotations, z_rotations

# Extract rotations for RIGHT_UPPER_LEG and RIGHT_LOWER_LEG
upper_x_rot, upper_y_rot, upper_z_rot = extract_joint_rotations(bvh, 'RIGHT_UPPER_LEG')
lower_x_rot, lower_y_rot, lower_z_rot = extract_joint_rotations(bvh, 'RIGHT_LOWER_LEG')