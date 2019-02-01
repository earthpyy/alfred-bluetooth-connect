on run argv
    set device_name to (system attribute "device_name")
    tell application "System Events"
        tell process "SystemUIServer"
            tell (menu bar item 1 of menu bar 1 where description is "bluetooth")
                click
                if menu item device_name of menu 1 exists then
                    tell (menu item device_name of menu 1)
                        click
                        set menu_name to name of menu item 1 of menu 1
                        click menu item 1 of menu 1
                        return menu_name & "ing " & device_name & "..."
                    end tell
                else
                    key code 53  -- ESC
                    return
                end if
            end tell
        end tell
    end tell
end run