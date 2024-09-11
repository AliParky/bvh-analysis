from bvh import Bvh

# Read the BVH file and parse it
with open("BVH-Recording1.bvh") as f:
    bvh_data = f.read().splitlines()
    bvh = f.read()

# Parse the BVH data
bvh = Bvh(bvh)

# Find the number of frames
num_frames = 0
frame_time = 0
for line in bvh_data:
    if line.startswith("Frames:"):
        num_frames = int(line.split()[1])
    elif line.startswith("Frame Time:"):
        frame_time = float(line.split()[2])
        break

# Calculate the total duration
total_duration = num_frames * frame_time

# Print the number of frames
print(f"Number of frames: {num_frames}")
print(f"Frame time: {frame_time} seconds")
print(f"Total duration: {total_duration} seconds")