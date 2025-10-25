cmake_minimum_required(VERSION 3.20)
project(multiscale-curvature-analysis LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ------------------------
# Fetch pybind11 automatically
# ------------------------
include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.11.1
)
FetchContent_MakeAvailable(pybind11)
include_directories(${pybind11_INCLUDE_DIRS})


# ------------------------
# Find OpenMP
# ------------------------
find_package(OpenMP REQUIRED)

# ------------------------
# Add your libraries
# ------------------------
add_library(fileHandler fileHandler.cpp)
add_library(formula formula.cpp)
add_library(userData userData.cpp)
add_library(analysis analysis.cpp)
add_library(dataContainer dataContainer.cpp)
add_library(userInputCLI userInputCLI.cpp)
add_library(processor_lib processor.cpp)

# Link OpenMP to analysis
if(OpenMP_CXX_FOUND)
    target_link_libraries(analysis PRIVATE OpenMP::OpenMP_CXX)
endif()

# ------------------------
# Create the pybind11 module
# ------------------------
pybind11_add_module(curvature bindings.cpp)

# Link your libraries to the Python module
target_link_libraries(curvature PRIVATE
    processor_lib
    fileHandler
    formula
    userData
    analysis
    dataContainer
    userInputCLI
)
# add_executable(curvature_exe main.cpp)
# Include directories for headers
target_include_directories(curvature PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
)
