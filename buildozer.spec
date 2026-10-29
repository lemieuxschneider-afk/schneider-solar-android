[app]
title = SCHNEIDER SOLAR
package.name = schneidersolar
package.domain = ht.schneider
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Les calculs sont locaux : l'application ne demande pas d'accès Internet.
android.permissions =
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
