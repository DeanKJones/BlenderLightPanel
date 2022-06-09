
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

########################################
##           Create Panel             ##
########################################

class VIEW3D_PT_light_panel(bpy.types.Panel):
    """Creates a light editing panel"""
    
    bl_idname = "OBJECT_PT_lights"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lights"
    bl_label = "Lightsss"

    def draw(self, context):
        
        layout = self.layout
        scene = bpy.context.scene
        render = bpy.data.scenes["Scene"].render
        panel_props = scene.props_light_panel

        
        box = layout.box()
        
        box.prop(panel_props, "checkbox", text="Advanced")

        # Loop lights and display parameters
        lights = [ob for ob in scene.objects if ob.type == 'LIGHT']
        for light in lights:
            
            light_d = light.data
            
            l_box = box.box()
            l_row = l_box.row(align=True)
            l_col = l_box.column()
            
            l_row.label(text=light.name, icon='LIGHT')
            
            vis = bpy.data.objects[f"{light.name}"]
            l_row.prop(vis, "hide_viewport", text="")
            l_row.prop(vis, "hide_render", text="")
            
            # Base Parameters
            l_col.row().prop(light_d, "color")
            l_col.prop(light_d, "energy")
            l_col.prop(light_d, "type")
            
            
            if panel_props.checkbox == True:
                
                # Cycles
                if bpy.data.scenes["Scene"].render.engine == 'CYCLES':
                    l_col.separator()
                    l_col.prop(light_d.cycles, "cast_shadow")
                    l_col.prop(light_d.cycles, 
                                        "use_multiple_importance_sampling")
                    l_col.prop(light_d.cycles, "max_bounces")
                    # Split for light types
                    if light_d.type in {'POINT', 'SPOT'}:
                        l_col.prop(light_d, "shadow_soft_size", text="Radius")
                    elif light_d.type == 'SUN':
                        l_col.prop(light_d, "angle")
                    elif light_d.type == 'AREA':
                        l_col.prop(light_d, "shape", text="Shape")
                        sub = l_col.column(align=True)
                        
                        if light_d.shape in {'SQUARE', 'DISK'}:
                            sub.prop(light_d, "size")
                        elif light_d.shape in {'RECTANGLE', 'ELLIPSE'}:
                            sub.prop(light_d, "size", text="Size X")
                            sub.prop(light_d, "size_y", text="Y")
                
                
                # Eevee               
                if bpy.data.scenes["Scene"].render.engine == 'BLENDER_EEVEE':
                    l_col.separator()
                    l_col.prop(light_d, "diffuse_factor")
                    l_col.prop(light_d, "specular_factor")
                    l_col.prop(light_d, "volume_factor")
                    
                    if light_d == bpy.data.lights["Sun"]:
                        l_col.prop(light_d, "angle")
            
        # Add engine toggle
        if panel_props.checkbox == True:
            layout.column().prop(render, "engine")

########################################
##           Property Group           ##
########################################

class PROPERTIES_light_panel(bpy.types.PropertyGroup):
    checkbox : bpy.props.BoolProperty(
        name="Enable or Disable",
        description="Show extra parameters for each light",
        default = False,
    )

########################################
##              Register              ##
########################################

classes = (
    VIEW3D_PT_light_panel,
    PROPERTIES_light_panel,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Scene.props_light_panel = bpy.props.PointerProperty(
                                                    type=PROPERTIES_light_panel)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.props_light_panel

if __name__ == "__main__":
    register()
