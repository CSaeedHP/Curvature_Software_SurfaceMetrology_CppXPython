# test_curvature.py
import sys
import os

# If your .pyd is in a build folder, add it to sys.path
build_path = os.path.join(os.path.dirname(__file__), "build", "Release")
if build_path not in sys.path:
    sys.path.insert(0, build_path)

try:
    import curvature
except ImportError as e:
    print("Failed to import curvature:", e)
    sys.exit(1)

print("Successfully imported curvature!")

# If you have a fetchData function returning a NumPy array
try:
    proc = curvature.Processor()
    print(dir(proc))
except AttributeError:
    print("curvature.Processor() not found. Make sure you bound it in PYBIND11_MODULE.")
