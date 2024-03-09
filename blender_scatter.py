import bpy

bl_info = {
    "name": "Blender Scatter",
    "author": "Amey Kurade",
    "version": (1, 0, 0),
    "blender": (4, 0, 2),  # Adjust based on Blender version you target
    "category": "Object"
}

def register():
  class ScatterObjectsOperator(bpy.types.Operator):
    bl_idname = "object.scatter_objects"
    bl_label = "Scatter Objects"

  def execute(self, context):
    # Get user-selected objects and target mesh
    selected_objects = bpy.context.selected_objects
    target_mesh = bpy.context.active_object.data  # Assuming active object is the target

    # Call your scatter_objects function with selected objects and target mesh
    scatter_objects(selected_objects, target_mesh)

    return {'FINISHED'}

  pass

def unregister():
  # Unregister your operator class (if applicable)
  pass
