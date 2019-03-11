#This script aims to autogenerate pdfs of layouts contained in an arc pro project for Roskilde Festivals Map Service

#Thanks to 	Delynko for writing the base for this project: https://github.com/delynko/ArcProPythonScripts/tree/b157bdb357e181a5cd15ce09e6be2f314007b361

#Before running the script read it through to adjust paths to local folders etc. 


#Dependencies
import arcpy


#Defines the project that contains the layouts
aprx = arcpy.mp.ArcGISProject(r"C:\Users\Frederik\Documents\Roskilde Festival 2019\GenerationProject.aprx")

#List of layouts
lyts = aprx.listLayouts()

#Creates a pdf for each layout in the project. The layouts must be created beforehand and stored accordingly
for lyt in lyts:
    if lyt.name.startswith("_") == False:
        print(lyt.name)
        lyt.exportToPDF(r"C:\Users\Frederik\Documents\Roskilde Festival 2019\export\{}.pdf".format(lyt.name), resolution=300)

		
		
# Hurray 