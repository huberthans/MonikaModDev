## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False

## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Monika_After_Story"

## Name of the executables, we must keep it DDLC to obey the guidelines
define build.executable_name = "DDLC"

## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75


#define config.gl_resize = False
init 50 python:
    # For some reason it's not inported yet, so we do it now /shrug
    from __future__ import print_function

    config.lint_hooks = [
        lambda: print(),
        lambda: print("#"*5, "START MAS LINT HOOKS", "#"*5),
        # Print all deprecation warnings after lint
        lambda: print(
            "Known uses of deprecated functions/classes in initialisation:",
            (
                "\n".join([msg.rjust(len(msg) + 4) for msg in store.mas_utils.deprecated.__all_warnings__])
                if store.mas_utils.deprecated.__all_warnings__
                else "    None"
            ),
            "",
            sep="\n"
        ),
        lambda: print("#"*5, "END MAS LINT HOOKS", "#"*5)
    ]

init python:
    #Override the choose renderer screen
    mas_override_label("_choose_renderer", "mas_choose_renderer_override")

    #The rest
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') # em dash
        s = s.replace(' - ', u'\u2014') # em dash
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    #config.adjust_view_size = force_integer_multiplier
## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.
## These settings create a set of files suitable for distributing as a mod.

init python:

    ## By default, renpy looks for archive files in the game and common directories
    ## Mac needs to check in the install directory instead.
    #if renpy.mac:



    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    ##This tells Renpy to build an updater file
    build.include_update = True

    ## This is the archive of data for your mod
    #build.archive(build.name, "all")

    ## These files will be included in the package
    # Add mod assets
    build.classify("game/mod_assets/**", "all")
    build.classify("game/gui/**", "all")
    # Add scripts in the game folder
    # build.classify("game/*.rpy", "all") # Optional, includes source
    build.classify("game/*.rpyc", "all")
    # Add python packages
    build.classify("game/python-packages/**", "all")
    # Add README
    build.classify("README.html", "all")
    # Add icons
    build.classify("CustomIcon**.**", "all")

    # build.package(build.directory_name + "Mod", "zip", "all", description="DDLC Compatible Mod")

    ## These files will be excluded
    # Remove everything else from the game folder
    build.classify("game/**", None)
    # Remove cache
    # build.classify("game/cache/**", None)
    # build.classify("game/saves/**", None)
    # Remove logs
    build.classify("log/**", None)
    build.classify("*.log", None)

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('*.md')

    build.include_old_themes = False



## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "..."
