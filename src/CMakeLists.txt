project ( kcoloredit )

find_package ( KDE4 REQUIRED )
include ( KDE4Defaults )
include ( MacroLibrary )

ADD_SUBDIRECTORY ( src )
ADD_SUBDIRECTORY ( desktop )
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
add_subdirectory( doc-translations )
add_subdirectory( doc )
