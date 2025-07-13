[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,toml

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = 
    python3,
    kivy,
    sdl2_ttf,
    pillow

# (str) Application orientation
orientation = portrait

# (str) Presplash (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon (optional)
# icon.filename = %(source.dir)s/data/icon.png

[android]

# (list) Target Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (int) Android SDK version
android.sdk = 33

# (int) Android NDK version
android.ndk = 25b

# (int) Target Android API
android.api = 34

# (int) Minimum Android API
android.minapi = 21

# (bool) Enable Android backup
android.allow_backup = True

# (str) Android release artifact format
android.release_artifact = apk

# (list) Android permissions
android.permissions = 
    INTERNET,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Fullscreen mode
fullscreen = 0

# (bool) Enable androidx
android.enable_androidx = True

[p4a]

# (str) p4a branch to use
p4a.branch = master

# (str) p4a bootstrap
p4a.bootstrap = sdl2

[buildozer]

# (int) Log level
log_level = 2

# (str) Build directory
build_dir = ./.buildozer

# (str) Bin directory
bin_dir = ./bin
