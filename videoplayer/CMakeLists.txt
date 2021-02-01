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
    PRIVATE ${MSINTTYPES_INCLUDE_DIRS}  # for windows
    PRIVATE ${GLIB2_INCLUDE_DIRS}
    PRIVATE ${OGG_INCLUDE_DIRS}         # for osx 10.9
    PRIVATE ${THEORADEC_INCLUDE_DIRS}   # for osx 10.9
    PRIVATE ${LIBSWSCALE_INCLUDE_DIRS}  # for osx
)
target_link_libraries(_VideoPlayer
    ${GLIB2_LINK_LIBRARIES}
    ${OGG_LINK_LIBRARIES}
    ${THEORADEC_LINK_LIBRARIES}
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
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/avutil-56.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/glib-2.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/libglib-2.0-0.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/libcharset.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/libiconv.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/libintl.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/ogg.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/libogg-0.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/pcre.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/swscale-5.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/theoradec-1.dll)
    list(APPEND DEPENDENCIES_DLL ${DEPENDENCY_FOLDER}/bin/theoradec.dll)
    foreach(DEP IN LISTS ${DEPENDENCIES_DLL})
        if (EXISTS ${DEP})
            install(FILES ${DEP} DESTINATION ${CMAKE_INSTALL_PREFIX}/videoplayer)
        else()
            message(STATUS "${DEP} not found")
        endif()
    endforeach()
endif()
