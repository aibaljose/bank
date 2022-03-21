# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['dist/obf/temp', '/home/mallucid/bank/App_Bank_GUI_v01_PySide_Or_PyQt_Qt_Quick_QML'],
             binaries=[],
             datas=[],
             hiddenimports=['pytransform'],
             hookspath=['dist/obf/temp'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# Patched by PyArmor
_src = '/home/mallucid/bank/App_Bank_GUI_v01_PySide_Or_PyQt_Qt_Quick_QML'
_obf = 0
for i in range(len(a.scripts)):
    if a.scripts[i][1].startswith(_src):
        x = a.scripts[i][1].replace(_src, r'/home/mallucid/bank/App_Bank_GUI_v01_PySide_Or_PyQt_Qt_Quick_QML/dist/obf')
        if os.path.exists(x):
            a.scripts[i] = a.scripts[i][0], x, a.scripts[i][2]
            _obf += 1
if _obf == 0:
    raise RuntimeError('No obfuscated script found')
for i in range(len(a.pure)):
    if a.pure[i][1].startswith(_src):
        x = a.pure[i][1].replace(_src, r'/home/mallucid/bank/App_Bank_GUI_v01_PySide_Or_PyQt_Qt_Quick_QML/dist/obf')
        if os.path.exists(x):
            if hasattr(a.pure, '_code_cache'):
                with open(x) as f:
                    a.pure._code_cache[a.pure[i][0]] = compile(f.read(), a.pure[i][1], 'exec')
            a.pure[i] = a.pure[i][0], x, a.pure[i][2]
# Patch end.

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
