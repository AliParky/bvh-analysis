# bvh-analysis

BVH Analysis is a tool for analyzing and visualizing BVH files (Biovision Hierarchy), which are commonly used for motion capture data. This tool allows users to parse BVH files, extract motion capture data, and visualize joint rotations over time.

## Features

- Parse BVH files and extract motion capture data.
- Visualize joint rotations over time.
- Calculate angles between joints.

## Installation
To install BVH Analysis, follow these steps:

1. Clone the repository
    ```sh
    git clone https://github.com/yourusername/bvh-analysis.git
    ```
2. Navigate to the project directory
    ```sh
    cd bvh-analysis
    ```
3. Install the required dependencies
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To use BHV Analysis, follow these steps:

1. Place your BVH files in the project directory.
2. Run the `bvh_analysis.py` script
    ```sh
    python bvh_analysis.py
    ```

## Dependencies
- `bvh`: A library for parsing BVH files.
- `matplotlib`: A library for creating static, animated, and interactive visualizations in Python.
- `numpy`: A library for numerical computations in Python.