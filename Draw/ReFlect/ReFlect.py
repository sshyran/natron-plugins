# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named ReFlectExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from ReFlectExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.comunity.plugin.ReFlect"

def getLabel():
    return "ReFlect"

def getVersion():
    return 1

def getIconPath():
    return "ReFlect.png"

def getGrouping():
    return "Draw"

def getPluginDescription():
    return "this plugin take a Normal Pass and a reflection image as an input and generate fake reflections , like when using a matcap.\n\nYou can then set the roughness / glossiness and Fresnel value.\n\nThis can be used with the Reshade plugin to add detail or metallic look to a relighted object.\n\nFew tips : \n-You don\'t need big images for the reflection map. Generally 512*512 is way enough and will render faster.\n\n- The impulse filter is the fastest and will work in many cases.\n\n- you may have to set very low Gamma (~0.18) and very High Gain (70)  for the fresnel to look good.\n\n-The reflection image can be any image , try with different images to see what effect they provide. You can search for ZBrush matcaps to get nice images to play with.\n"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.userNatron = lastNode.createPageParam("userNatron", "Controls")
    param = lastNode.createDouble2DParam("GLOSSsize", "Glossiness")
    param.setMinimum(0, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setMinimum(0, 1)
    param.setMaximum(1000, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(100, 1)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Glossiness factor (blur the reflections)")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(10, 0)
    param.setValue(10, 1)
    lastNode.GLOSSsize = param
    del param

    param = lastNode.createChoiceParam("STMap1filter", "Filter")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Filtering algorithm - Impulse work in most cases , and is way faster than the others")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("Impulse")
    lastNode.STMap1filter = param
    del param

    param = lastNode.createSeparatorParam("sep", "")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistant(False)
    param.setEvaluateOnChange(False)
    lastNode.sep = param
    del param

    param = lastNode.createStringParam("fresnel_label", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("Fresnel")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.fresnel_label = param
    del param

    param = lastNode.createBooleanParam("show_fresnel", "Display")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Display the fresnel max for better tweaking")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.show_fresnel = param
    del param

    param = lastNode.createDoubleParam("Fgamma", "Gamma")
    param.setMinimum(0, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.2, 0)
    lastNode.Fgamma = param
    del param

    param = lastNode.createDoubleParam("Fgain", "Gain")
    param.setMinimum(0, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(100, 0)
    lastNode.Fgain = param
    del param

    param = lastNode.createDoubleParam("Merge1mix", "Mix")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.98, 0)
    lastNode.Merge1mix = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['userNatron', 'Node', 'Settings', 'Info'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output1")
    lastNode.setLabel("Output1")
    lastNode.setPosition(733, 1152)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Normal"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Normal")
    lastNode.setLabel("Normal")
    lastNode.setPosition(1036, 80)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupNormal = lastNode

    del lastNode
    # End of node "Normal"

    # Start of node "remapValues"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("remapValues")
    lastNode.setLabel("remapValues")
    lastNode.setPosition(1036, 346)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupremapValues = lastNode

    param = lastNode.getParam("blackPoint")
    if param is not None:
        param.setValue(-1, 0)
        param.setValue(-1, 1)
        param.setValue(-1, 2)
        param.setValue(-1, 3)
        del param

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "remapValues"

    # Start of node "STMap1"
    lastNode = app.createNode("net.sf.openfx.STMap", 2, group)
    lastNode.setScriptName("STMap1")
    lastNode.setLabel("STMap1")
    lastNode.setPosition(1038, 665)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupSTMap1 = lastNode

    param = lastNode.getParam("channelU")
    if param is not None:
        param.set("UV.g")
        del param

    param = lastNode.getParam("channelUChoice")
    if param is not None:
        param.setValue("UV.g")
        del param

    param = lastNode.getParam("channelV")
    if param is not None:
        param.set("UV.b")
        del param

    param = lastNode.getParam("channelVChoice")
    if param is not None:
        param.setValue("UV.b")
        del param

    param = lastNode.getParam("channelAChoice")
    if param is not None:
        param.setValue("UV.a")
        del param

    param = lastNode.getParam("wrapV")
    if param is not None:
        param.set("Repeat")
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("Impulse")
        del param

    del lastNode
    # End of node "STMap1"

    # Start of node "GLOSS"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 3, group)
    lastNode.setScriptName("GLOSS")
    lastNode.setLabel("GLOSS")
    lastNode.setPosition(1239, 348)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupGLOSS = lastNode

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(10, 0)
        param.setValue(10, 1)
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("Quasi-Gaussian")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "GLOSS"

    # Start of node "Mirror1"
    lastNode = app.createNode("net.sf.openfx.Mirror", 1, group)
    lastNode.setScriptName("Mirror1")
    lastNode.setLabel("Mirror1")
    lastNode.setPosition(1239, 666)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupMirror1 = lastNode

    param = lastNode.getParam("flip")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("flop")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("sourceChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Mirror1"

    # Start of node "Fresnel"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Fresnel")
    lastNode.setLabel("Fresnel")
    lastNode.setPosition(606, 344)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupFresnel = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("A.r")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("A.a")
        del param

    del lastNode
    # End of node "Fresnel"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(870, 653)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("multiply")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0.98, 0)
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "FresnelGamma"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("FresnelGamma")
    lastNode.setLabel("FresnelGamma")
    lastNode.setPosition(606, 435)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupFresnelGamma = lastNode

    param = lastNode.getParam("gamma")
    if param is not None:
        param.setValue(0.2, 0)
        param.setValue(0.2, 1)
        param.setValue(0.2, 2)
        param.setValue(0.2, 3)
        del param

    param = lastNode.getParam("clampWhite")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "FresnelGamma"

    # Start of node "Reflection_Map"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Reflection_Map")
    lastNode.setLabel("Reflection_Map")
    lastNode.setPosition(1239, 76)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupReflection_Map = lastNode

    del lastNode
    # End of node "Reflection_Map"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(733, 849)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch1"

    # Start of node "Grade1"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade1")
    lastNode.setLabel("Grade1")
    lastNode.setPosition(606, 665)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade1 = lastNode

    param = lastNode.getParam("white")
    if param is not None:
        param.setValue(100, 0)
        param.setValue(100, 1)
        param.setValue(100, 2)
        del param

    param = lastNode.getParam("clampWhite")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupSwitch1)
    groupremapValues.connectInput(0, groupNormal)
    groupSTMap1.connectInput(0, groupremapValues)
    groupSTMap1.connectInput(1, groupMirror1)
    groupGLOSS.connectInput(0, groupReflection_Map)
    groupMirror1.connectInput(0, groupGLOSS)
    groupFresnel.connectInput(1, groupremapValues)
    groupMerge1.connectInput(0, groupSTMap1)
    groupMerge1.connectInput(1, groupGrade1)
    groupFresnelGamma.connectInput(0, groupFresnel)
    groupSwitch1.connectInput(0, groupMerge1)
    groupSwitch1.connectInput(1, groupGrade1)
    groupGrade1.connectInput(0, groupFresnelGamma)

    param = groupSTMap1.getParam("filter")
    group.getParam("STMap1filter").setAsAlias(param)
    del param
    param = groupGLOSS.getParam("size")
    group.getParam("GLOSSsize").setAsAlias(param)
    del param
    param = groupMerge1.getParam("mix")
    group.getParam("Merge1mix").setAsAlias(param)
    del param
    param = groupFresnelGamma.getParam("gamma")
    param.setExpression("thisGroup.Fgamma.get()", False, 0)
    param.setExpression("thisGroup.Fgamma.get()", False, 1)
    param.setExpression("thisGroup.Fgamma.get()", False, 2)
    param.setExpression("thisGroup.Fgamma.get()", False, 3)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("thisGroup.show_fresnel.get()", False, 0)
    del param
    param = groupGrade1.getParam("white")
    param.setExpression("thisGroup.Fgain.get()", False, 0)
    param.setExpression("thisGroup.Fgain.get()", False, 1)
    param.setExpression("thisGroup.Fgain.get()", False, 2)
    del param

    try:
        extModule = sys.modules["ReFlectExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
