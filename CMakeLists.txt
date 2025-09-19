cmake_minimum_required(VERSION 3.10)
project(multiscale-curvature-analysis)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find pybind11
set(pybind11_DIR "C:/Users/J/AppData/Local/Programs/Python/Python313/Lib/site-packages/pybind11/share/cmake/pybind11")
find_package(pybind11 CONFIG REQUIRED)
include_directories(${pybind11_INCLUDE_DIRS})


# Find OpenMP
find_package(OpenMP REQUIRED)

# Add your libraries
add_library(fileHandler fileHandler.cpp)
add_library(formula formula.cpp)
add_library(userData userData.cpp)
add_library(analysis analysis.cpp)
add_library(dataContainer dataContainer.cpp)
add_library(userInputCLI userInputCLI.cpp)
add_library(processor_lib processor.cpp)
target_include_directories(processor_lib PUBLIC ${pybind11_INCLUDE_DIRS})
# Link OpenMP to analysis
if (OpenMP_CXX_FOUND)
    target_link_libraries(analysis PRIVATE OpenMP::OpenMP_CXX)
endif()

# Add the pybind11 module
pybind11_add_module(curvature bindings.cpp)

# Link your libraries to the module
target_link_libraries(curvature PRIVATE 
    processor_lib
    fileHandler
    formula
    userData
    analysis
    dataContainer
    userInputCLI
)

# Optional: add include directories if needed
target_include_directories(curvature PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}  # for headers
)
