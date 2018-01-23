cmake_minimum_required( VERSION 3.10 )
project( Prime VERSION 1.0.0 )

add_library( Prime STATIC
  src/PrimeTest.cpp )

target_include_directories( Prime
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include> )

install( TARGETS Prime ARCHIVE DESTINATION lib )
install( DIRECTORY include/Prime DESTINATION include )
