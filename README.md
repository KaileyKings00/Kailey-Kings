  # Kyle Galenzoga s5418946@bournemouth.ac.uk

  
# Firework Particle Project 
  One of MSc Computer Animation and Visual Effect's Project from the ASE course Semester 1.
  ### How to Use:
  - Run main.py and the Firework Project Application will appear.
  - Click buttons to spawn, colour, resize and reset Fireworks. Change their speed and pause/continue their animation view. 
  - Press Quit button to Exit the Application.
  - (Important Note: Install Python, numpy and NCCA Library Code to run this project)
  - Firework Application Image Link: [Fireworks Demo Application Design Image](https://file.notion.so/f/f/141e73cf-03aa-426f-9a97-9f886e7c7733/44e2cda3-c973-4475-8d53-9f303b82ba9c/Firework_Panel.png?table=block&id=2f369366-a955-808d-a865-c622bc9cec26&spaceId=141e73cf-03aa-426f-9a97-9f886e7c7733&expirationTimestamp=1769464800000&signature=3TRys7i8jEa-s9nxpFdeRP3wZikjHkXFVq60zz9OP48&downloadName=Firework+Panel.png)
  - Image Display: ![alt text](https://file.notion.so/f/f/141e73cf-03aa-426f-9a97-9f886e7c7733/44e2cda3-c973-4475-8d53-9f303b82ba9c/Firework_Panel.png?table=block&id=2f369366-a955-808d-a865-c622bc9cec26&spaceId=141e73cf-03aa-426f-9a97-9f886e7c7733&expirationTimestamp=1769371200000&signature=d2a6j4hDVvM3hra14agYvDyJLcwBnaaJKYccbd1nBMQ&downloadName=Firework+Panel.png "Final Firework Design Application")
  
  


  Real Project Link: [Firework GUI Project Github Link](https://github.com/NCCA/aseassignment25-26-KaileyKings00)



  ## Where do I Start Developing this Project: 

  ### Project Idea:  

  For my development project, I am going to create Simple Fireworks from small points to scattered particles that Users can change their size, speed, group and colours in their User Interface. To start with, 

  - Using Jon Macey's NumPy Particle System project examples and connecting with Qt/Pyside GUI Widget.  

  - Changing Normal Light particles to any random colours 

  - Developing the Particle System first before designing their GUI Application controls 

 
  ### Software and Other System Requirements: 
  - **"Core API and Python Setups"**
    - Python Programming Language 
    - OpenGL and GLSL Shaders 
    - PySide6 and Qt Application 
    - NCCA Graphics Library code 

  - Software Application Tools
    - **Zed Application at Linux** (For Developing Particle Numpy System)
    - **QtCreator Application at Linux** (For Designing GUI controls)
    - **Visual Studio Code 2018 at Windows** (For Project Management Lists)

 

## How It's Made:

### Initial Problem Statement
- Most Important Question = "How to Develop, test and Implement this Project Efficiently?"
- What are the things needed to add and develop Particle NumPy System
- How to Edit Particles and add Lighting/Emissive effects?
- How to remove the Infinite Loop Particles and turn them into Firework Animation view?
- How do I add this Particle System inside the Application using PySide6 and QWidget tools?


### Initial Design:
- 2D Simulation Style.
- Must be an Easy User Interface to navigate Firework Project Controls
    - Control Buttons like QPushButtons, QSpinBox and QSlider
    - Colour Palette Style like "QColorDialog"

### Classes, Algorithms and 3rd Party Libraries:

#### All Classes and Functions:
- **#main.py	= class MainWindow**
    | Functions  | Descriptions | Status |
    | ------------- | --------------------------------- | ---------|
    | def _init_  | Initialize Main Window Application and their Signal and Slots Functions | Update |
    | def set_ColourDialogs  | Create QColorDialog and assigning Particle's ColourPicker function  | New Update |
    | def closeEvent | Close Firework Project Application.| New Update |
    | def load_io | Loads and Runs UI, QWidget, QApplication and etc. | Normal |
    | def main()| Set up and format the Main Window and QApplications | Normal |
 
  - Starts the Project Application, allowing Users to use their GUI Controls to play the Particle System(Fireworks)
  
  

- **#Random.py = class Random**
    | Functions  | Descriptions | Status |
    | ------------- | --------------------------------- | ---------|
    | def random_float |  Returns a random float in the range [-1, 1], scaled by `mult` | Normal|
    | def random_positive_float | Returns a random float in the range [0, 1], scaled by `mult` | Normal|
    | def random_vec3|   Returns a Vec3 with each component in the range [-1, 1], scaled by `mult`| Normal|
    | def random_positive_vec3 | Returns a Vec3 with each component in the range [0, 1], scaled by `mult` | Normal|
    | def random_vector_on_sphere | Returns random Vec3 located on the surface of a sphere with given radius. | Normal|

    - It generates random floats and vectors. Useful import tool for NumPy features and Emitter class.

- **#Emitter.py = class Emitter**
    | Functions  | Descriptions | Status |
    | ------------- | ----| ---------|
    | def _init_ | Initialise Emitter's position, life, size, directions, colour and etc. | Update |
    | def set_AdvancedColour |Emitter particle to one colour assigned by self.base_colour  | New Update |
    | def set_EmitterSize | Emitter size using Emitter Grow value(Max Grow Input Box) | New Update |
    | def _init_particles| Creating number of particles and using Respawn Particles for indices | Normal |
    | def _respawn_particles | Using Math Formulae and Colour Method to face Respawn Particles | Update |
    | def update | Multiplying by floats and dt. Change and measure gravity, speed and dir | Update |
    | def FinishedLoop | Adding Respawning new Particles after dead particles fade  | New Update |
    | def num_particles | returns the current number of particles back to the Emitter process | Normal |
  

    - It generates Emitter Particle and develop its size, direction, colour and numbers of alive/dead particles variables.


- **#PyNGLScene = class PyNGLSCene(QOpenGLWidget)**
    | Functions  | Descriptions | Status |
    | ------------- | --------------------------------- |  ---------|
    | def _init_ | initialize lists of variables needed for the funtions to operate| Update |
    | def set_max_alive | turns Alive particle into a value | New Update |
    | def pause | stops the Particle System's animation process and assigns to connect with GUI Pause Button | New Update |
    | def resume | plays the Particle system's animation process from pausing and connects with GUI Continue Button. | New Update |
    | def reset | resets the Emitter Particle Variables back to its origin and it uses to connect GUI Reset Fireworks Button | New Update |
    | def set_Particle_Run | measures the Emitter Particle Speed using "value/total value" and it uses for GUI Max Speed Input Value | New Update |
    | def set_Particle_Resize | adds or subtracts the number of Alive Particles spawning in the Application view. It connects with GUI Max Alive Input Value. |  New Update |
    | def RestartTime | restarts the particle system by respawning new emitter(with NumPy Math Operations) to a random position. It connects with GUI Spawn Fireworks Button | New Update |
    | def set_ColourPicker | sets Particle Colours with RGB and NumPy Array. It stores the Selected Colour as Updated Particle colour using GUI Fill Colour Button | New Update |
    | def set_GrowParticle | connects Emitter's self size and controls Particle's Shape using GUI Max Grow Input Value | New Update |
    | def initializeGL | uses GLSL Shader language tools and connect Vertex/Fragment Shader to render the Particle System | Update |
    | def resizeGL | former function to resize Camera view and projection view management but it's currently been deactivate and replaced by setCamera Zoomview function | Lost update |
    | def set_Camera_ZoomView | used for controlling Particle System's Camera and zooming in and out. It connects with GUI Viewport Slider | New Update |
    | def keyReleaseEvent | activates list of Assigned Key buttons to press in KeyPress Function and adds them to the Window | Normal |
    | def keyPressEvent | records lists of input keys to activate their features like Closing Application, changing Particle's Structure and Pausing/Playing their Animated Scene | Normal |
    | def _process_camera_movements | records left/right/up/down arrow input key buttons for moving camera view in 3D Test | Normal |
    | def paintGL | access OpenGL features and rendering one frame of Particle System's scene. Using hasattr to check if Vao exists or not, solving error issues. | Update |
    | def timerEvent | updates Emitter's animation boolean process, timeframe and speed. Applying RestartTime function to continue the Restart/Fading loop process. | Update |
    
    - Initialised a group of Emitters and turning them into a Final Particle System with their Functions and Useful attributes. 


##### **#Vertex GLSL Shader**
    1. Assigns colour to the out_Colour and connect them to Fragment shader
    2. Compute the point size, convert the particle's position using MVP matrix

##### **#Fragment GLSL Shader**
    1. Use the Vertex points(gl_PointCoord) and adjust their coordinates using math operations.
    2. Start creating glow Intensity effects and place them towards the middle centre by adding alpha variable
    3. Add Smoothstep function to smooth their edge and add Alpha variable to the Fragment Colour 



#### 3rd Party Libraries:
- OpenGL and GLSL Shading Language
- Adding Vertex and Fragment GLSL Shaders
- PySide6 and QtWidgets/QtApplications with more tools
- Importing sys
- Import Math and Random
- Adding NumPy
- Adding NCCA-NGL Library Available Code

#### Final Algorithm of Firework Project with Control Applications:
  1. There are 10 controls for Users to explore this Project Interface. Open the Firework GUI Application Project and ensure the Particle System(Firework Animation) is active.
  2. Click the Spawn Firework button and the Output will spawn a new particle scatter in a random position.
  3. Click the Pause button and the Animate variable will turn off, stopping the Firework Animation Process.
  4. Click the Continue button and the Animate variable will turn on, resuming the Firework Scatter Animation.
  5. Click the Fill Colour button and a New Window of Colour Palette will appear. Users can only choose one colour and the Firework's colour will automatically change.
  6. Add 0-100 value to Max Speed Spin Integer Box, output from Slow to Fast Speed Firework Animation. 30 Value is commonly suitable for Particle Speed.
  7. Add 200-2500 value to Max Alive Spin Integer Box, resulting with number of Alive Particles display on the Firework Animation. 2000 value serves as a normal Firework Appearance.
  8. Add 1-5 value on Max Grow Spin Integer Box, showing a number of Particles change from Shrink(1) to Grow(5) point size. 
  9. Use the Viewpoint Slider from Left(1) to Right(100), controlling the Camera's Offset view of the Particle System
  10. Press Reset Fireworks button and the Particle System will restor their colour, size, animation, alive numbers and speed back to its origin.
  11. Press the Quit button and the Main Window Application will be closed, including the Particle System and its controls.




### Final Files Added to Assignment Repository:
- Project Folder called **"AFireworkGUI"**
    - **main.py**        
    - **Emitter.py** 
    - **PyNGLScene.py**
    - **Random.py**
    - **Fragment.glsl**
    - **Vertex.glsl**



## Implementation:

### Initial Design System
  After all the new functions added, the previous Particle System Example has been evolved into new Firework Animation process where particles only scatter once and respawn another. This actual program changed its (self emitter) to (self emitters) for adding Multiple Emitters method. 
  - I also created a new Angle Direction using Azimuthal and Polar formula to face their direction like a Firework Movement. I removed the Infinite Loop, Multiple Colours and Group Emitters Spawn that I replaced them with new variables like:
  
  | Emitter Variables  | Descriptions |
  | ------------- | --------------------------------- |
  | self.base_colour| stores and converts the colour variable to NumPy array, then apply the Colour to Alive Particles |
  | self emitters| "True" boolean variable serves to detect and give permission to spawn Particles and fade them when it reached its density size |
  | self finished| "False" boolean variable that detects Alive Particle turning to Zero and marks the end of Emitter Life Cycle. |
  
  
### List of Designed Assets
  1. MainWidget.ui
        - Normal Windows Application Design
        - Adding Particle System(PyNGLScene.py) on the left
        - GUI Controls on the right
  2. Qtcreator's GUI Controls
        - 1 QSlider Control
        - 6 QPushbuttons Control
        - 3 QSpinbox value button controls
  3. Emitter Particles
        - with colour, size, alive, direction variables
        - with NumPy and Random Import tools
  4. Title Test Image
      
      
### Codings Demonstration Examples

#### Applying Glow Effect in Fragment Shader with Math Operations from "Fragment Shader"
``` GLSL
    ////  Super Glowing Alpha Process, Getting Flash Outline
    float glow = exp(dot(circle_cord,circle_cord) * 2.0);
    float edge = smoothstep(1.0, 0.6, sqrt(dot(circle_cord,circle_cord)));

    vec3 color = out_colour * (0.2 + glow);
    float alpha = glow * edge;

    fragment_colour = vec4(color, alpha);
```
  - Apply Smooth Edge and Alpha effects to the Fragment Shader test, turning Particles into Firework glow form. Discarding dot circle can still changing both Alpha and Smoothstep process. (Leese & Baldwin, n.d.)

#### Creating Emitter Particle's Direction Facing View from "Emitter.py"
``` Python
  ## Creating Angle Direction Vectors: Azimuthal(theta) and Polar(phi)
        theta = np.random.uniform(0, 2 * np.pi, count)
        phi = np.random.uniform(0, np.pi, count)
        normal_speed = np.random.uniform(9.0, 7.0, count)

        ## Build our Particle Mixed Directions/ From spherical to Cartesian coordinate formulas 
        directions = np.zeros((count, 3), dtype=np.float32)
        directions[:, 0] = (normal_speed * 1.9) * np.sin(phi) * np.cos(theta)
        directions[:, 1] = (normal_speed * 2.0) * np.sin(phi) * np.sin(theta)
        directions[:, 2] = normal_speed * np.cos(phi)
```
  - Using Azimuthal Angle with x,y plane and Polar Angle with z axis can combined by adding Notations and Math coordinates that will convert from Spherical Coordinates to Cartesian coordinates. (Weisstein, n.d.) This will change the Particle's movements when scattering in front high before falling and fading their remaining points.

#### Using Numpy Array to Particle Size from "Emitter.py"
``` Python
   ##Emitter Growing and Speed Test ##2   
    def set_EmitterSize(self, size):
        self.size[:] = size
```
  - A Numpy Array Operation and sets the Particle Size to all Size that keeps them update.

#### Detecting Dead/Alive Emitter Particles Code from "Emitter.py"
``` Python
        ### Detecting Dead/Alive Particles and ensuring they show and fade
        if self.emitters and np.count_nonzero(self.alive) < self.max_alive:
            spawn_number = min(self.max_per_frame, self.max_alive - np.count_nonzero(self.alive))
            fade_indices = np.where(self.alive == False)[0][:spawn_number]

            # Revives some Dead Particles
            self.alive[fade_indices] = True
            self._respawn_particles(fade_indices)

            # Starts fading emitters
            if np.count_nonzero(self.alive) >= self.max_alive:
                self.emitters = False

        # Decided that Emitter fading cycle is done
        if not self.emitters and np.count_nonzero(self.alive) == 0:
            self.finished = True
```
  - To remove the Infinite Particle Scatter loop from example project, I changed their Lifetime Cycle to spawn Alive Particles and removing them after scattering once. This code accessed a Particle Lifetime Cycle where Two Boolean Variables, (self.emitters and self.finished), marks the process of spawning Particles and fading them completely. 
  - It ensures that all remaining hidden particles must be completely erased and triggering self.finished that all Alive Particles are gone to Zero.
  - cites OpenAI, *ChatGPT(GPT-5.2)*, Examples of changing Infinite Particle System Spawn back to Dead Particles, December 22, 2025.


#### Random Emitter Particle Positions with Math Formula from "PyNGL Scene.py"
``` Python
    def RestartTime(self):                  ## Spawns Respawn Emitters randomly using Numpy tools
        x = np.random.uniform(-5, 10)
        y = np.random.uniform(0.5, 3.0)
        z = np.random.uniform(-5, 10)
        
        Emission = Emitter(Vec3(x, y + 5.0, z), 5000, self.particle_size, 200, (50, 200))
```
  - This Function used variables to select random coordinates of X and Z axis while vertically operates Y axis in high/low and then, it distributes their values and drawn by NumPy Uniform tools (Numpy.org, 2024).
  - When spawning new Emitters, these coordinates will be used for placing them in any random position in a system.

#### Using Math Operations and Transformations for GUI Viewport Camera Slider from "PyNGL Scene.py"
``` Python
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
```
  - The process of implementing Camera Zoom mechanic applies input values bounded by target zoom range and compute to transform from one interval to another. Using hasattr argument type checks whether the Camera connects this function or not.
  - With the value and zoom range numbers connected to one variable(delta), I used the Particle's Camera Movement and update the X offset position to input zoom in and out slider view transformation for 2D Interface.
  - cites OpenAI, *ChatGPT(GPT-5.2)*, Attaching QSlider to adjust Camera Zoom Attributes, January 22, 2026.










#### Useful For Accessing Particle Libraries, PySide6 tools for Particle in the Terminal for my Project:
``` Python
    uv add ncca-ngl
```
  - Thanks to this code, I was able to access the PySide tools and their examples in my GitHub Resporitory testing version.

### Flowcharts
  - Emitter Process of Spawning and Fading Particles with Loop: ![alt text](https://file.notion.so/f/f/141e73cf-03aa-426f-9a97-9f886e7c7733/e7ebeb80-53c5-41d2-a0b1-c9948a740fde/image.png?table=block&id=2f369366-a955-8029-aeec-de0e06ee16e6&spaceId=141e73cf-03aa-426f-9a97-9f886e7c7733&expirationTimestamp=1769378400000&signature=wxei_7b1vN_seWoLTippa70WUhDrod3j5NTwgCcqyAY&downloadName=image.png "Final Firework Flowchart Design")
  - Flowchart Image: [Emitter Lifetime Spawn and Fade Cycle Flowchart Link](https://file.notion.so/f/f/141e73cf-03aa-426f-9a97-9f886e7c7733/e7ebeb80-53c5-41d2-a0b1-c9948a740fde/image.png?table=block&id=2f369366-a955-8029-aeec-de0e06ee16e6&spaceId=141e73cf-03aa-426f-9a97-9f886e7c7733&expirationTimestamp=1769464800000&signature=nsX2gZbm95F0Lm3Bir2ZuChMSC1CVRJdD3zxwUVlEEA&downloadName=image.png)
## What I've Learned:
  - Developing the Particle System into Fireworks form is very challenging that brings new experience of using OpenGL shaders, QApplications and more Python tools to work efficiently. 
  - It gave me a chance to understand how Object Oriented Programming works and how it needs GPU processing and Importing useful Python library codes to access their system. Just like how Functions and Variables can connect GUI Buttons and, using Shaders to render all the Particle Systems to make them accessible. 
  - If there was time for improvement, I recommend adding advanced glow effects with small particles followed behind the Vertex point to develop a real Firework scatter. Another improvement would be adding a background sound effect to trigger when the particle scatter. With sound effects, Users will immerse this Firework program project.

### Reference Lists:
- Jon Macey’s WebPages. (2020). Lecture 1 Introduction to ASE and Python | Jon Macey’s WebPages. [online] Available at: https://nccastaff.bournemouth.ac.uk/jmacey/msc/ase/lectures/Lecture1/ [Accessed 25 Jan. 2026].
- Jon Macey’s WebPages. (2020). Lab 6 Introduction to Particle Systems | Jon Macey’s WebPages. [online] Available at: https://nccastaff.bournemouth.ac.uk/jmacey/msc/ase/labs/lab6/lab6/ [Accessed 25 Jan. 2026].
- De Vries, J. (2019). LearnOpenGL - Basic Lighting. [online] Learnopengl.com. Available at: https://learnopengl.com/Lighting/Basic-Lighting.
- Leese, G., Kessenich, J., & Baldwin, D. (n.d.). The OpenGL ® Shading Language, Version 4.60.8. Retrieved April 30, 2025, from https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.60.pdf
- Weisstein, E.W. (n.d.). Spherical Coordinates. [online] mathworld.wolfram.com. Available at: https://mathworld.wolfram.com/SphericalCoordinates.html.
- “ChatGPT.” 2025. ChatGPT. 2025. https://chatgpt.com/c/69725d20-1824-832e-b58d-39a1fcad5b7e.
- Numpy.org. (2024). numpy.random.uniform — NumPy v2.2 Manual. [online] Available at: https://numpy.org/doc/2.2/reference/random/generated/numpy.random.uniform.html?utm_source=chatgpt.com [Accessed 26 Jan. 2026].
- Python documentation. (2025). Built-in Functions. [online] Available at: https://docs.python.org/3/library/functions.html#hasattr.
- Github.com. (2026). Securly - Geolocation sharing. [online] Available at: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images [Accessed 25 Jan. 2026].

