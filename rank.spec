# -*- mode: python -*-

block_cipher = None

added_files = [
            ('drivers/geckodriver-v0.11.1-macos.tar.gz', '.'),
            ('drivers/chromedriver_mac64.tar.gz', '.'),
            ('src/icon.ico', 'src')
            ]
a = Analysis(['rank.py'],
             pathex=['/Users/luca/PycharmProjects/Rank'],
             binaries=None,
             datas=added_files,
             hiddenimports=["selenium"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='rank',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='src/icon.ico')
app = BUNDLE(exe,
             name='rank.app',
             icon='src/icon.ico',
             bundle_identifier=None,
             info_plist={
                    'NSHighResolutionCapable': 'True'
                    },
             )
