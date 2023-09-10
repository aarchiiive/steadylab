# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_steadylab_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED steadylab_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(steadylab_FOUND FALSE)
  elseif(NOT steadylab_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(steadylab_FOUND FALSE)
  endif()
  return()
endif()
set(_steadylab_CONFIG_INCLUDED TRUE)

# output package information
if(NOT steadylab_FIND_QUIETLY)
  message(STATUS "Found steadylab: 0.0.0 (${steadylab_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'steadylab' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${steadylab_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(steadylab_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${steadylab_DIR}/${_extra}")
endforeach()
