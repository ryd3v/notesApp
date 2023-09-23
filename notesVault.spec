# -*- mode: python ; coding: utf-8 -*-
specpath = os.path.dirname(os.path.abspath(SPEC))

block_cipher = None


a = Analysis(
    ['notesVault.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.'), ('./icons/open.png', '.'), ('./icons/preview.png', '.'), ('./icons/save.png', '.'), ('./icons/single.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='notesVault',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
   icon='./icon.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)