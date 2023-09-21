import bpy


class SubmitJobOperator(bpy.types.Operator):
    bl_idname = "submit.job"
    bl_label = "Submit Job"


class SubmitJob(bpy.types.Operator):
    bl_idname = "object.submit_job"
    bl_label = "My Operator"

    def execute(self, context):
        layerData = {
            'name': context.scene.layer_name,
            'layerType': 'Blender',
            'cmd': {
                'blenderFile': '/home/nuwan/Documents/Projects/OpenCue/blender-demos/test/test.blend',
                'outputPath': '',
                'outputFormat': 'PNG'
            },
            'layerRange': '1',
            'chunk': '1',
            'cores': '0',
            'env': {},
            'services': [],
            'limits': [],
            'dependType': '',
            'dependsOne': None
        }

        jobData = {
            'name': context.scene.job_name,
            'username': context.scene.usr_name,
            'show': "testing",
            'shot': context.scene.shot_name,
            'layers': layerData
        }

        # from . import Submission
        # Submission.submit(jobData)
