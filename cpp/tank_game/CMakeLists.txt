cmake_minimum_required(VERSION 3.7)
SET (CMAKE_VERBOSE_MAKEFILE ON)

project(foo)


# find_package(SDL2 REQUIRED)
# include_directories(${SDL2_INCLUDE_DIRS})

# add_executable(foo main_move_sprite.cpp)
# target_link_libraries(foo ${SDL2_LIBRARIES})


find_package(SDL REQUIRED)
include_directories(${SDL_INCLUDE_DIRS})

add_executable(foo main_move_sprite.cpp)
target_link_libraries(foo ${SDL_LIBRARY})
