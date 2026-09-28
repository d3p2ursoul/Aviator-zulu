
[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = com.wonderboy.aviatorpredictor

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# p4a.port =

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
