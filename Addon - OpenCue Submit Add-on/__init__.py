import bpy
from .operators import submit_job
from .panels import open_cue

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
    open_cue.OpenCuePanel,
    submit_job.SubmitJobOperator
)


def register():
    bpy.utils.register_class(open_cue.OpenCuePanel)
    bpy.utils.register_class(submit_job.SubmitJobOperator)

    bpy.types.Scene.job_name = bpy.props.StringProperty(
        name="Job name",
        description="Enter some text",
        default=""
    )

    bpy.types.Scene.usr_name = bpy.props.StringProperty(
        name="User name",
        description="Enter some text",
        default=""
    )

    bpy.types.Scene.layer_name = bpy.props.StringProperty(
        name="Layer name",
        description="Enter some text",
        default=""
    )

    bpy.types.Scene.shot_name = bpy.props.StringProperty(
        name="Shot name",
        description="Enter some text",
        default=""
    )


_, unregister = bpy.utils.register_classes_factory(classes)
