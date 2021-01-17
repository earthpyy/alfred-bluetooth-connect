# IMPORTANT NOTICE
### This plugin is not updated anymore, please consider use [bmunoz89's Bluetooth Manager](https://github.com/bmunoz89/alfred-wf-bluetooth-manager) instead. Thanks for your support!

# alfred-bluetooth-connect
Alfred plugin that allowed to connect/disconnect to paired bluetooth device


## Requirements
- Alfred 3
- Powerpack
- Python 2+


## Installation
1. Download latest release [here](https://github.com/earthpyy/alfred-bluetooth-connect/releases/latest)
2. Double-click to add to **Alfred**


## Usage
### Toggle bluetooth device
```
bt [alias | device name]
```

### Set alias for easy access
- Full syntax
```
btset [alias] > [device name]
```

- Short syntax (alias **must** not contain any space)
```
btset [alias] [device name]
```


### Unset alias
```
btunset [alias]
```

### Mark/Unmark as favorite
`Command + Enter` on selected device, then you can easily connect it with just
```
bt
```
**Note:** It will automatically toggle device when mark as favorite but not with unmark


## TODO
- Load device list from system profiler
- Detect which one should connect or disconnect to use as text in items
- Turn on automatic toggle when mark as favorite and only connect to device
- Connect bluetooth device without using UI


## Author
Preeti Yuankrathok ([@earthpyy](https://github.com/earthpyy))
