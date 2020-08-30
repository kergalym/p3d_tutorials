from panda3d.core import TextureStage
from direct.showbase.ShowBase import ShowBase


class MainApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        scene = base.loader.load_model('lightmap.test.egg')
        scene.set_x(1)
        scene.set_z(0)
        scene.set_scale(10)
        scene.reparent_to(render)

        render.set_shader_auto()

        ts = TextureStage("lightmap")
        lightmap = base.loader.load_texture("tex/ligtmap.png")
        ts.setTexcoordName("lightmap")

        scene.set_texture(ts, lightmap)


MainApp().run()
