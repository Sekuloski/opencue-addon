import bpy


class OpenCuePanel(bpy.types.Panel):
    bl_idname = "OPEN_CUE_PT_Panel"
    bl_label = "OpenCue"
    bl_category = ""
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.prop(context.scene, "job_name")
        col.prop(context.scene, "usr_name")
        col.prop(context.scene, "layer_name")
        col.prop(context.scene, "shot_name")

        col = layout.column()
        col.operator("submit.job", text="Submit Job")
