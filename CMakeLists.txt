cmake_minimum_required( VERSION 3.10 )
project( Prime VERSION 1.0.0 )

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)

add_library( Prime STATIC
  src/PrimeTest.cpp )
set_target_properties( Prime PROPERTIES DEBUG_POSTFIX _debug )

target_include_directories( Prime
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include> )

install( TARGETS Prime EXPORT PrimeExport ARCHIVE DESTINATION lib )
install( DIRECTORY include/Prime DESTINATION include )
install( EXPORT PrimeExport NAMESPACE Prime:: CONFIGURATIONS Release Debug DESTINATION cmake )

configure_file( PrimeConfig.cmake.in PrimeConfig.cmake @ONLY )
configure_file( PrimeConfigVersion.cmake.in PrimeConfigVersion.cmake @ONLY )
install(
  FILES
    ${CMAKE_CURRENT_BINARY_DIR}/PrimeConfig.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/PrimeConfigVersion.cmake
  DESTINATION cmake )
            
set( CPACK_PACKAGE_VERSION ${PROJECT_VERSION} )
include( CPack )
