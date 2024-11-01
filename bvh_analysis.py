from bvh import Bvh
import matplotlib.pyplot as plt
import numpy as np

# Read the BVH file and parse it
with open("BVH-Recording1.bvh") as f:
    bvh_data = f.read()

# Parse the BVH data
bvh_data = Bvh(bvh_data)

# Find the number of frames
num_frames = bvh_data.nframes
frame_time = bvh_data.frame_time

# Calculate the total duration
total_duration = num_frames * frame_time

# Print the number of frames
print(f"Number of frames: {num_frames}")
print(f"Frame time: {frame_time} seconds")
print(f"Total duration: {total_duration} seconds")

# Extract joint names
joint_names = [joint.name for joint in bvh_data.get_joints()]

# Print the hierarchy
print("\nHierarchy:")
for joint in bvh_data.get_joints():
    print(joint.name)
    if joint.parent.value:
        print(f"  Parent: {joint.parent.name}")

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

# Function to calculate the angle between two joints
def calculate_joint_angle(upper_x, upper_y, upper_z, lower_x, lower_y, lower_z):
    upper_vector = np.array([upper_x, upper_y, upper_z])
    lower_vector = np.array([lower_x, lower_y, lower_z])
    dot_product = np.dot(upper_vector, lower_vector)
    norm_upper = np.linalg.norm(upper_vector)
    norm_lower = np.linalg.norm(lower_vector)
    cos_angle = dot_product / (norm_upper * norm_lower)
    angle = np.arccos(cos_angle)
    return angle

# Extract rotations for RIGHT_UPPER_LEG and RIGHT_LOWER_LEG
upper_x_rot, upper_y_rot, upper_z_rot = extract_joint_rotations(bvh_data, 'RIGHT_UPPER_LEG')
lower_x_rot, lower_y_rot, lower_z_rot = extract_joint_rotations(bvh_data, 'RIGHT_LOWER_LEG')

# Convert frames to time (seconds)
time_axis = [frame * frame_time for frame in range(num_frames)]

# Plot the rotations for RIGHT_UPPER_LEG
plt.figure(figsize=(10, 5))
plt.plot(time_axis, upper_x_rot, label='X Rotation')
plt.plot(time_axis, upper_y_rot, label='Y Rotation')
plt.plot(time_axis, upper_z_rot, label='Z Rotation')
plt.xlabel('Frame')
plt.ylabel('Rotation (degrees)')
plt.title('RIGHT_UPPER_LEG Rotations')
plt.legend()
plt.show()