"""

"""

import os; os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
from typing import Callable


class TileEngine:

	colors = {
        'red': (255, 0, 0),
        'yellow': (255, 255, 0),
        'blue': (0, 0, 255),

		'green': (0, 255, 0),
		'purple': (200, 100, 200),
        'orange': (255, 165, 0),
		
		'black': (0, 0, 0),
        'grey': (127, 127, 127),
		'white': (255, 255, 255),
	}

	def __init__(
			self,
            screen_size: tuple,
            num_grids: tuple,
			title: str,
            target_fps: int = 60,
            font_style: str = 'impact',
            record = False,
        ) -> None:
		"""
		Initializes engine, calculates aspect ratio and fits active window to screen.
		"""
		self.target_fps = target_fps
		self.font_style = font_style

		pygame.init()
		pygame.font.init()

		self.clock = pygame.time.Clock()
		self.dt = None
		self.running = True
		pygame.display.set_caption(title)
		
		self.record = record
		self.t = 0        

		self.font_cache: dict[tuple[int, int], pygame.font.Font] = {}
		self.surface_cache: dict[tuple[int, int], pygame.Surface] = {}

		self.screen_size = screen_size
		self.num_grids = num_grids

		self.offset: tuple[float, float] = None  # type: ignore[assignment]
		self.screen: pygame.Surface = None  # type: ignore[assignment]
		self.background: pygame.Surface = None  # type: ignore[assignment]
		self.grid_size: tuple[int, int] = None  # type: ignore[assignment]
		self.padded_grid_size: tuple[int, int] = None  # type: ignore[assignment]

		self._initialize_screen()

	
	def _initialize_screen(self) -> None:
		screen_size = self.screen_size
		num_grids = self.num_grids
		# aspect ratios
		screen_ar, grids_ar = screen_size[0] / screen_size[1], num_grids[0] / num_grids[1]

		# position active window to fit on screen
		if grids_ar == screen_ar:
			self.offset = (0, 0)
			bg_size = screen_size
		elif grids_ar > screen_ar:
			compression = screen_size[0] / num_grids[0]
			bg_size = (num_grids[0] * compression, num_grids[1] * compression)
			self.offset = (0, 0.5 * (screen_size[1] - bg_size[1]))
		else:
			compression = screen_size[1] / num_grids[1]
			bg_size = (num_grids[0] * compression, num_grids[1] * compression)
			self.offset = (0.5 * (screen_size[0] - bg_size[0]), 0)

		self.screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
		# self.screen = pygame.display.set_mode(screen_size)
		self.surface_cache[bg_size] = pygame.Surface(bg_size)
		self.background = self.surface_cache[bg_size]

		self.grid_size = tuple([int(bg_size[0] / num_grids[0]), int(bg_size[1] / num_grids[1])])
		self.padded_grid_size = (self.grid_size[0] + 1, self.grid_size[1] + 1)

		# calculate clipping due to discrepancy of integer rounding
		clipping = (0.5 * (bg_size[0] % num_grids[0]), 0.5 * (bg_size[1] % num_grids[1]))
		self.offset = (self.offset[0] + clipping[0], self.offset[1] + clipping[1])
		self.screen.set_clip(pygame.Rect(*self.offset, bg_size[0] - clipping[0] * 2, bg_size[1] - clipping[1] * 2))
			

	def should_run(self) -> bool:
		"""
		Determines if engine should keep running.

		Returns
		-------
		bool: if engine is now running after checks
		"""
		if not self.running:
			return False
		self._handle_events()
		self.dt = self.clock.tick(self.target_fps) / 1000 * self.target_fps
		return self.running

	def clear_screen(self) -> None:
		"""Removes everything blitted on screen by covering everything with background."""
		self.screen.blit(self.background, self.offset)

	def update_screen(self) -> None:
		"""Renders necessary components to screen."""
		pygame.display.flip()
		if self.record:
			pygame.image.save(self.screen, "frames/screen_" + str(self.t) + ".png")
		self.t += 1

	def exit(self) -> None:
		"""Has engine exit."""
		if self.running:
			pygame.quit()

	def scale_up(self, coord: tuple[int, int]) -> tuple[int, int]:
		"""
		Scales (x, y) coords to fit resolution of screen.

		Parameters
		----------
		coord: tuple
			(x, y) coord to scale up

		Returns
		-------
		tuple: scaled coord
		"""
		return coord[0] * self.grid_size[0] + self.offset[0], coord[1] * self.grid_size[1] + self.offset[1]

	def render_scene(self, func: Callable, *args) -> None:
		"""
		Renders custom scene defined outside of this class in the form of customScene(engine: graphics.Engine...

		Parameters
		----------
		func: callable
			Function describing how to render custom scene
		*args
			Arguments to pass into func
		"""
		func(self, *args)

	def render_text(self, text: str, pos: tuple, font_size: int, text_color: tuple, bg_color: tuple = None) -> None:
		"""
		Blits text to screen.

		Parameters
		----------
		text: str
			Text to display
		pos: tuple
			(x, y) pos on screen to display text
		fontSize: int
			Size of font
		text_color: tuple
			RGB color value
		bg_color: tuple, optional
			RGB color value for rect behind text
		"""
		if font_size not in self.font_cache:
			self.font_cache[font_size] = pygame.font.SysFont(self.font_style, font_size)

		font = self.font_cache[font_size]
		paddedOutput = " " + text + " "

		if bg_color is not None:
			text = font.render(paddedOutput, True, text_color, bg_color)
		else:
			text = font.render(paddedOutput, True, text_color)

		textRect = text.get_rect()
		textRect.center = pos
		self.screen.blit(text, textRect)

	def render_rect(self, pos: tuple, size: tuple, fill_color: tuple, alpha: int = 255) -> None:
		"""
		Blits rect to screen.

		Parameters
		----------
		pos: tuple
			(x, y) pos to blit rect to screen
		size: tuple
			(x, y) size of rect
		fill_color: tuple
			RGB values for color of rect
		alpha: int, default=255
			Transparency value (0-255) of rect
		"""
		if size not in self.surface_cache:
			self.surface_cache[size] = pygame.Surface(size)

		surface = self.surface_cache[size]
		surface.set_alpha(alpha)
		surface.fill(fill_color)
		self.screen.blit(surface, pos)

	def render_circle(self, pos: tuple, radius: float, fill_color: tuple, alpha: int = 255) -> None:
		"""
		Blits circle to screen.

		Parameters
		----------
		pos: tuple
			(x, y) pos to blit rect to screen
		radius: float
			Radius of circle
		fill_color: tuple
			RGB values for color of rect
		alpha: int, default=255
			Transparency value (0-255) of rect
		"""
		frameSize = (radius * 2, radius * 2)
		rel_x = radius
		rel_y = radius

		if frameSize not in self.surface_cache:
			self.surface_cache[frameSize] = pygame.Surface(frameSize)

		surface = self.surface_cache[frameSize]
		surface.fill(TileEngine.colors['white'])
		surface.set_colorkey(TileEngine.colors['white'])
		surface.set_alpha(alpha)

		pygame.draw.circle(surface, fill_color, (rel_x, rel_y), radius)
		self.screen.blit(surface, pos)

	def render_line(self, start: tuple, end: tuple, width: int, fill_color: tuple) -> None:
		"""
		Blits line to screen.

		Parameters
		----------
		start: tuple
			(x, y) pos for start point of line
		end: tuple
			(x, y) pos for end point of line
		width: int
			Value denoting width of line
		fill_color: tuple
			RGB values for color of rect
		"""
		pygame.draw.line(self.screen, fill_color, start, end, width)

	def _handle_events(self) -> None:
		"""Handles events from Pygame's event queue. pygame.QUIT occurs when "X" on top right corner is clicked."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.display.quit()
				pygame.quit()
			if event.type == pygame.VIDEORESIZE:
				self.screen_size = (event.w, event.h)
				self._initialize_screen()
