import random
from typing import Tuple

import numpy as np
from ncca.ngl import Vec3

from Random import Random


class Emitter:
    _GRAVITY = np.array((0.0, -9.81, 0.0), dtype=np.float32)

    def __init__(
        self, position: Vec3, num_particles: int, max_alive: int, max_per_frame: int, life_range: Tuple[int, int]
    ):
        self.max_per_frame = max_per_frame
        self.life_range = life_range
        self._position = position
        self._position_np = position.to_numpy()
        self._num_particles = num_particles
        self.position = np.zeros((self._num_particles, 3), dtype=np.float32)  # x,y,z
        self.direction = np.zeros((self._num_particles, 3), dtype=np.float32)  # x,y,z
        self.colour = np.zeros((self._num_particles, 3), dtype=np.float32)  # r,g,b
        self.base_colour = np.array([1., 1.0, 1.0], dtype=np.float32)       #New Testing Colour


        self.life = np.zeros((self._num_particles,), dtype=int)  # r,g,b
        self.max_life = np.zeros((self._num_particles,), dtype=int)  # r,g,b
        self.size = np.zeros((self._num_particles,), dtype=np.float32)  # r,g,b
        self.alive = np.full(self.num_particles, False, dtype=np.bool)
        self.max_alive = max_alive
        self._init_particles()
        self.emitters = True    ## New Variable added for Fading Process
        self.finished = False   ## New Variable added for Looping Process


    ## Changing Emitter Particles back to One Colour Test 
    def set_AdvancedColour(self, colour_rgb):
        self.base_colour = np.array(colour_rgb, dtype=np.float32)
        self.colour[self.alive] = self.base_colour
        
    ##Emitter Growing and Speed Test ##2   
    def set_EmitterSize(self, size):
        self.size[:] = size
        
        
        
    def _init_particles(self):
        num_to_create = random.randint(10, 50)
        indices = np.arange(num_to_create)
        self._respawn_particles(indices)


    def _respawn_particles(self, indices):
        # init particles vectorized.
        if len(indices) == 0:
            return

        idx = np.asarray(indices, dtype=int)
        count = idx.size


        ## Creating Angle Direction Vectors: Azimuthal(theta) and Polar(phi)
        theta = np.random.uniform(0, 2 * np.pi, count)
        phi = np.random.uniform(0, np.pi, count)
        normal_speed = np.random.uniform(9.0, 7.0, count)

        ## Build our Particle Mixed Directions/ From spherical to Cartesian coordinate formulas 
        directions = np.zeros((count, 3), dtype=np.float32)
        directions[:, 0] = (normal_speed * 1.9) * np.sin(phi) * np.cos(theta)
        directions[:, 1] = (normal_speed * 2.0) * np.sin(phi) * np.sin(theta)
        directions[:, 2] = normal_speed * np.cos(phi)


        ##Emitter's Improvement Arrays List 
        positions = np.tile(self._position_np.reshape(1, 3), (count, 1))    # positions at start so from pos
        colours = np.tile([self.base_colour], (count, 1))                   # using base_colour for One Assigned Colour
        #colours = np.random.rand(count, 3)                                 #Results of Multiple Colours 
        life = np.zeros(count, dtype=int)
        max_life = np.random.randint(self.life_range[0], self.life_range[1], size=count, dtype=int)
        size = np.full(count, 0.01, dtype=np.float32)

        # The Attributes
        self.position[idx] = positions
        self.direction[idx] = directions
        self.colour[idx] = colours
        self.life[idx] = life
        self.max_life[idx] = max_life
        self.size[idx] = size

    def update(self, dt: float):
        ## Changing Gravity and Direction Speed, especially Physical Size of Emitter to measure
        self.direction += Emitter._GRAVITY * dt
        self.position += self.direction * (dt * 0.3)
        self.life += 1
        self.size += dt * 0.3                               # Size Particles Measurement

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



        ## Fade Effects for Dead Particles
        dead_mask = self.life > self.max_life

        if np.any(dead_mask) and np.any(self.alive):
            self.colour[dead_mask] *= 0.01  # Test if they gone
            self.size[dead_mask] *= 0.01  # Test if they gone
            self.alive[dead_mask] = False  # False to Death
        print(f"Num Alive {np.count_nonzero(self.alive)}")  # Debug Test #1



    ### Detecting how Dead/Alive Particles is fully done and ready to spawn another Emitter
    def FinishedLoop(self):
        return self.finished
        # return (not self.emitters) and np.count_nonzero(self.alive) == 0 (Previous)

    @property
    def num_particles(self):
        return self._num_particles
