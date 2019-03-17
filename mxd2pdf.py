

import glob, os, arcpy

mxd_list =[]

os.chdir("Y:\MXD_publish\MXD_PDFkort\ExportToPdf Frede")
for file in glob.glob("*.mxd"):
    print(file)
    mxd_list.append(file)


for mxdfile in mxd_list:
    mxd = arcpy.mapping.MapDocument(mxdfile)
    pathname = "Y:\MXD_publish\MXD_PDFkort\ExportToPdf Frede\Out\Kort_" + str(mxdfile) + ".pdf"
    pathname = pathname.replace(pathname[-7:-3],'')
    print(pathname)
    arcpy.mapping.ExportToPDF(mxd, pathname)



