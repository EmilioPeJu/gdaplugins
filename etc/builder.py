from iocbuilder import Device, AutoSubstitution, SetSimulation, Xml
from iocbuilder.arginfo import *

from iocbuilder.modules.ADCore import ADCore, ADBaseTemplate, NDPluginBaseTemplate, includesTemplates, makeTemplateInstance
from iocbuilder.modules.asyn import AsynIP, AsynPort

class gdaPlugins(Xml):
    """This plugin instantiates a standard set of plugins for use by GDA:"""
    TemplateFile = 'gdaPlugins.xml'
gdaPlugins.ArgInfo.descriptions["CAM"] = Ident("Areadetecor camera to connect to", ADCore)
