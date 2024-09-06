# Read the BVH file and parse it
with open("BVH-Recording1.bvh") as f:
    bvh_data = f.read().splitlines()

# Find the number of frames
num_frames = 0
frame_time = 0
for line in bvh_data:
    if line.startswith("Frames:"):
        num_frames = int(line.split()[1])
        break

# Print the number of frames
print(f"Number of frames: {num_frames}")
print(f"Frame time: {frame_time} seconds")