# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=[],
    datas=[('static','static'),('media','media'),('templates','templates'),('karaoke','karaoke'),('manage.py','manage.py'),('karaoke_generator','karaoke_generator'),('generate-karaoke.ico','generate-karaoke.ico')],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['ctypes'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Karaoke-Generator.exe',
    debug=False, bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['generate-karaoke.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Karaoke-Generator',
)
