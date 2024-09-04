# Read the BVH file and parse it
bvh_data = open("BVH-Recording1.bvh").read().splitlines()

# Find the number of frames
num_frames = 0
for line in bvh_data:
    if line.startswith("Frames:"):
        num_frames = int(line.split()[1])
        break

# Print the number of frames
print(f"Number of frames: {num_frames}")