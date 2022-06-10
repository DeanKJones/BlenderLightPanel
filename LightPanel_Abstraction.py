
# Plugin Info
bl_info = {
    "name": "Light editor",
    "author": "D Jones <dhkjones@gmail.com>",
    "version": (0, 5, 0),
    "blender": (3, 1, 2),
    "category": "Light Panel",
    "location": "View 3D > Tool Shelf",
    "description": "List all available lights in a given scene for ease of access for lighting artists",
}

# Imports
import bpy

# Gather Lights
class LightPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_lightTest"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "TEST"
    bl_label = "LIGHTS"

    def draw(self, context):
        
        layout = self.layout
        scene = bpy.context.scene
        
        box = layout.box()
        
        lights = [ob for ob in scene.objects if ob.type == 'LIGHT']
        for light in lights:
            pass

        data = {
            'bl_label': "MyNewType",
            'bl_idname': "test.MyNewType",
            'bl_parent_id': "LightPanel",
            '__annotations__': {
                "MyIntVal": bpy.props.IntProperty(name="MyIntVal",default=42),
            }
        }
        return data


def get_data(self, arg):
        pass


my_new_type = type("MyNewType", 
                  (bpy.types.Panel, LightPanel), 
                   LightPanel.data)

obj = my_new_type(bpy.types.Panel, LightPanel)
obj.get_data()

bpy.utils.register_class(LightPanel)
bpy.utils.register_class(my_new_type)

bpy.types.Object.my_prop_grp = bpy.props.PointerProperty(type=my_new_type)
print(bpy.data.objects[0].my_prop_grp.MyIntVal)