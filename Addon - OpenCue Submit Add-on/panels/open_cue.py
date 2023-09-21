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
        col.operator("submit.job")
