#!/usr/bin/env -S uv run --script


import random  # Testing to Loop Fireworks
import sys

import numpy as np
import OpenGL.GL as gl
from ncca.ngl import (
    FirstPersonCamera,
    Primitives,
    Prims,
    ShaderLib,
    Transform,
    VAOFactory,
    VAOType,
    Vec3,
    VertexData,
    look_at,
    perspective,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QApplication

from Emitter import Emitter


class PyNGLScene(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.animate = True
        self.keys_pressed = set()
        self.rotate: bool = False
        self.original_x_pos: int = 0
        self.original_y_pos: int = 0
        self.max_alive = 2500                                                   ##Active and Alive Firework Particle Test
        self.emitter_speed = 0.03                                               ##Emitter Max Speed Value Test
        self.camera_fov = 20.0                                                  ##Camera Field of View(fov) Test
        self.zoom_numbers = 0.0                                                 ##Camera Operation Zoom Test
        self.current_ColourPicker = np.array([1.0, 1.0, 1.0], dtype=np.float32) ##rgb Restart Colour Test
        self.particle_size = 2000                                               ##Particle's Self.Alive/Number size 
        self.current_growNumbers = 10                                           ##Number of Growing Particles
        
        
    ##UI Control Connection Test
    def set_max_alive(self, value):                 
        self.max_alive = value

    def pause(self):                                ##Pause Button Definition Task
        self.animate = False
    
    def resume(self):                               ##Continue Button Definition Task
        self.animate = True

    def reset(self):                                ##Reset Button Definition Task
        self.animate = True
        self.max_alive = 2500       
        self.emitter_speed = 0.03   
        self.camera_fov = 20.0      
        self.zoom_numbers = 0.0     
        self.current_ColourPicker = np.array([1.0, 1.0, 1.0], dtype=np.float32)   
        self.particle_size = 2000 
        self.current_growNumbers = 10    
        
        
        

    def set_Particle_Run(self, value):          ##Adjust Emission's speed of Particle System for Max Speed Input
        self.emitter_speed = value / 1000.0
        #print("Test Firework Speed Working to: ", self.emitter_speed) #it's working Yay
        
        
    def set_Particle_Resize(self, value):       ##Update Numbers of Alive Particle Spawn for Max Alive Input 
        self.particle_size = value


    def RestartTime(self):                      ## Spawns Respawn Emitters randomly using Numpy tools
        x = np.random.uniform(-5, 10)
        y = np.random.uniform(0.5, 3.0)
        z = np.random.uniform(-5, 10)
        
        Emission = Emitter(Vec3(x, y + 5.0, z), 5000, self.particle_size, 200, (50, 200))
        Emission.set_AdvancedColour(self.current_ColourPicker)
        Emission.set_EmitterSize(self.current_growNumbers)
        self.emitters.append(Emission)
        


    ##Changing Emitter to One Colour and Connecting to ColorDialog Process
    def set_ColourPicker(self, rgb):
        """ rgb: np.array([r, g, b]) in 0–1 range"""
        self.current_ColourPicker = rgb
        # Applying to all emitters
        for emitter in self.emitters:
            emitter.set_AdvancedColour(rgb)
        self.update()


    ##Changing Emitter's Growth Shape using Emitter's Size Definition
    def set_GrowParticle(self, value):
        for emitter in self.emitters:
            emitter.set_EmitterSize(value)




    def initializeGL(self):
    ##Background Colours and Camera Arrangements
        gl.glClearColor(0.1, 0.1, 0.16, 1.0)  # Change colours
        ShaderLib.load_shader("Pass", "shaders/Vertex.glsl", "shaders/Fragment.glsl")
        ShaderLib.use("Pass")
        self.camera = FirstPersonCamera(Vec3(0, 5, 50), Vec3(0, 0, 90), Vec3(0, 1, 0), self.camera_fov,) #Camera View
        w, h = self.width(), self.height()
        self.camera.set_projection(self.camera_fov, (w / max(1.0, h)), 0.05, 200)


    ## Adding Multiple Emitters
        self.emitters = []
        self.emitters.append(Emitter(Vec3(1, 4, 0), 5000, 2500, 200, (30, 200)))         #Particle 1
        self.emitters.append(Emitter(Vec3(-9.0, 9.0, 0.0), 5000, 2500, 200, (30, 200)))  #Particle 2


    ## Updating OpenGL tests and Particle Attributes
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_MULTISAMPLE)
        self.vao = VAOFactory.create_vao(VAOType.MULTI_BUFFER, gl.GL_POINTS)
        with self.vao as vao:
            data = VertexData(data=[], size=0)
            vao.set_data(data, index=0)  # index 0 is positions
            vao.set_data(data, index=1)  # index 1 is colours
        self.startTimer(16)



    ##Camera Zoom In and Out for Viewport Slider Input
    def resizeGL(self, w: int, h: int):
        pass

    ##Camera Initialized Operation Test
    def set_Camera_ZoomView(self, value:int):
        if not hasattr(self, "camera"):
            return
    
        # Mapping Slider to Zoom Delta Variable
        max_zoom = 5.0
        min_zoom = -5.0
        target_slider = 1.0 - (value / 100.0)       #Inputting for Viewport Slider Needed
        target_zoom = min_zoom + target_slider * (max_zoom - min_zoom)
        delta = target_zoom - self.zoom_numbers     
        self.zoom_numbers = target_zoom
    
        ## Moving camera forward/backward with (x, y, speed)
        self.camera.move(delta, 0.0, 1.0) 
        self.update()




    ## Learning Useful Key Events and Special Guide for MainWindow
    def keyReleaseEvent(self, event):
        key = event.key()
        self.keys_pressed.discard(key)
        self.update()

    ## Normal Input Key Guidelines Tool
    def keyPressEvent(self, event):
        key = event.key()
        self.keys_pressed.add(key)
        if key == Qt.Key_Escape:
            self.close()
        elif key == Qt.Key_W:
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        elif key == Qt.Key_S:
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        elif key == Qt.Key_A:
            self.animate ^= False
        elif key == Qt.Key_1:
            for emitter in self.emitters:# Changing Emitter self to Update
                emitter.update(0.01)
        elif key == Qt.Key_R:            # Original Change #1 Restart and Useful Tool for Firework Burst Test
            self.RestartTime()
            #print(f"Restart Particles Again {self.RestartTime}")  # Debug Test Time
        self.update()

    ## Normal Camera Position Input Keys
    def _process_camera_movements(self):
        x_dir = 0.0
        y_dir = 0.0
        for key in self.keys_pressed:
            if key == Qt.Key_Left:
                y_dir = -1.0
            elif key == Qt.Key_Right:
                y_dir = 1.0
            elif key == Qt.Key_Up:
                x_dir = 1.0
            elif key == Qt.Key_Down:
                x_dir = -1.0
        if x_dir != 0.0 or y_dir != 0.0:
            self.camera.move(x_dir, y_dir, 0.1)

 
 
 
    ## Updating OpenGL Rendering resources with Initialized Checks 
    def paintGL(self):
        if not hasattr(self, "vao"):
            return
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glViewport(0, 0, self.width(), self.height())
        gl.glEnable(gl.GL_PROGRAM_POINT_SIZE)
        gl.glEnable(gl.GL_BLEND)                    # ADDING BLENDING for Fragment Shader
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE)  # ADDING BLENDING for Fragment Shader
        self._process_camera_movements()


    ## Updating Vertex Emitter attributes to connect Multiple Emitters
        ShaderLib.use("Pass")        
        ShaderLib.set_uniform("MVP", self.camera.get_vp())
        with self.vao as vao:
            for emitter in self.emitters:
                pos_size = np.concatenate([emitter.position, emitter.size[:, np.newaxis]], axis=1)
                data = VertexData(data=pos_size.flatten(), size=pos_size.nbytes)
                vao.set_data(data, index=0)
                vao.set_vertex_attribute_pointer(0, 4, gl.GL_FLOAT, 0, 0)

                data = VertexData(data=emitter.colour.astype(np.float32).flatten(), size=emitter.colour.nbytes)
                vao.set_data(data, index=1)
                vao.set_vertex_attribute_pointer(1, 3, gl.GL_FLOAT, 0, 0)

                vao.set_num_indices(len(emitter.position))
                vao.draw()

    
    def timerEvent(self, event):
    ##Pause and Continue(Self.Animate Option) Test 
        if not self.animate:
            return

    ##Update Emitter Particles and their Emitter's Max Speed Value
        for emitter in self.emitters[:]:  
            emitter.update(self.emitter_speed)


    
    ## Spawn New Firework Emitter Particles Again
        if emitter.finished:
            self.emitters.remove(emitter)
            self.RestartTime() 
        self.update()

