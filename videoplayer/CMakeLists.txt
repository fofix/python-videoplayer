# Steps:
# - compile the external lib
# - cythonize the pyx file (to get a C file)
# - compile the extension
# - install the module

# cythonize the pyx file
add_cython_target(_VideoPlayer _VideoPlayer.pyx)

# compile the extension with the lib
add_library(_VideoPlayer MODULE ${_VideoPlayer} VideoPlayer.c)
target_include_directories(_VideoPlayer
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}
    PRIVATE ${GLIB2_INCLUDE_DIRS}
)
target_link_libraries(_VideoPlayer
    ${GLIB2_LIBRARIES}
    ${OGG_LIBRARIES}
    ${THEORADEC_LIBRARIES}
    ${OPENGL_LIBRARIES}
    ${LIBSWSCALE_LIBRARIES}
)
python_extension_module(_VideoPlayer)

# install the module
# skbuild: add_python_extension
install(TARGETS _VideoPlayer
    LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/videoplayer
    PRIVATE_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

# Copy dlls on windows
if (WIN32)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/avutil-56.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/glib-2.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/libcharset.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/libiconv.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/libintl.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/ogg.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/pcre.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/swscale-5.dll)
    list(APPEND DEPENDENCIES_DLL ${CMAKE_CURRENT_BINARY_DIR}/theoradec.dll)
    install(FILES ${DEPENDENCIES_DLL}
            DESTINATION ${CMAKE_INSTALL_PREFIX}/videoplayer)
endif()
