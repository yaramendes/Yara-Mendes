INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_T126 t126)

FIND_PATH(
    T126_INCLUDE_DIRS
    NAMES t126/api.h
    HINTS $ENV{T126_DIR}/include
        ${PC_T126_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    T126_LIBRARIES
    NAMES gnuradio-t126
    HINTS $ENV{T126_DIR}/lib
        ${PC_T126_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(T126 DEFAULT_MSG T126_LIBRARIES T126_INCLUDE_DIRS)
MARK_AS_ADVANCED(T126_LIBRARIES T126_INCLUDE_DIRS)

