VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(0,0,0,1),
        prodvers=(0,0,0,1),
        mask=0x3f,
        flags=0x1,
        OS=0x4,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo(
            [
                StringTable(
                    '000004b0',
                    [StringStruct('CompanyName', 'OSx'), #Организация
                     StringStruct('FileDescription', 'AUser'), # Описание файла
                     StringStruct('FileVersion', 'None'), #
                     StringStruct('InternalName', 'No'), #
                     StringStruct('LegalCopyright',
                                  'Copyright © 2021-2022 OSx'), #
                     StringStruct('OriginalFilename', 'AUser'), #Исходное имя файла
                     StringStruct('ProductName', 'None'), #Название продукта
                     StringStruct('ProductVersion', 'None')]) #Версия продукта
            ]),
        VarFileInfo([VarStruct('Translation', [0, 1200])])
    ]
)
