import bpy


class SubmitJobOperator(bpy.types.Operator):
    bl_idname = "submit.job"
    bl_label = "Submit Job"

    job_name = bpy.props.StringProperty(
        name="Job name",
        description="Enter some text",
        default=""
    )

    usr_name = bpy.props.StringProperty(
        name="User name",
        description="Enter some text",
        default=""
    )

    layer_name = bpy.props.StringProperty(
        name="Layer name",
        description="Enter some text",
        default=""
    )

    shot_name = bpy.props.StringProperty(
        name="Shot name",
        description="Enter some text",
        default=""
    )

    def execute(self, context):
        print(self.usr_name)

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.prop(context, "job_name")
        col.prop(context, "usr_name")
        col.prop(context, "layer_name")
        col.prop(context, "shot_name")
