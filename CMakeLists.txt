cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
project(multiscale-curvature-analysis)



include(FetchContent)
# Fetch Dear ImGui
# FetchContent_Declare(
#     imgui
#     GIT_REPOSITORY https://github.com/ocornut/imgui.git
#     GIT_TAG v1.91.9b # Use the latest or a specific version
# )
# FetchContent_MakeAvailable(imgui)

# # Add ImGui to your project
# add_library(imgui STATIC
#     ${imgui_SOURCE_DIR}/imgui.cpp
#     ${imgui_SOURCE_DIR}/imgui_draw.cpp
#     ${imgui_SOURCE_DIR}/imgui_tables.cpp
#     ${imgui_SOURCE_DIR}/imgui_widgets.cpp
#     ${imgui_SOURCE_DIR}/backends/imgui_impl_glfw.cpp  # If using GLFW
#     ${imgui_SOURCE_DIR}/backends/imgui_impl_opengl3.cpp  # If using OpenGL
# )

# target_include_directories(imgui PUBLIC ${imgui_SOURCE_DIR} ${imgui_SOURCE_DIR}/backends)

add_executable(main main.cpp)

add_library(fileHandler fileHandler.cpp)
add_library(formula formula.cpp)
add_library(userData userData.cpp)
add_library(analysis analysis.cpp)
add_library(dataContainer dataContainer.cpp)
add_library(userInputCLI userInputCLI.cpp)

find_package(OpenMP REQUIRED)
if (OpenMP_CXX_FOUND)
    target_link_libraries(analysis PRIVATE OpenMP::OpenMP_CXX)
endif()



target_link_libraries(main PRIVATE fileHandler formula userData analysis dataContainer userInputCLI)



if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static-libgcc -static-libstdc++ -pthread")
endif()