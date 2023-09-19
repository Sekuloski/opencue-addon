import bpy

bl_info = {
    "name": "OpenCue Submit Add-on",
    "author": "Bojan Sekuloski",
    "description": "An add-on to submit jobs to OpenCue from Blender",
    "blender": (3, 6, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

classes = (
)

register, unregister = bpy.utils.register_classes_factory(classes)
