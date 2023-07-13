#stolen from table muthafluffin rus

import pygame

def renderText(text, font, color, x, y, screen, allowed_width, align="center", shadow=(0, 0)):
	if allowed_width > 0:
		words = text.split()

		lines = []
		while len(words) > 0:
			line_words = []
			while len(words) > 0:
				line_words.append(words.pop(0))
				fw, fh = font.size(" ".join(line_words + words[:1]))
				if fw > allowed_width:
					break

			line = " ".join(line_words)
			lines.append(line)

		max_w = 0
		y_offset = 0
		for line in lines:
			fw, fh = font.size(line)

			if align == "center":
				tx = x - fw / 2
			elif align == "left":
				tx = x
			elif align == "right":
				tx = x - fw
			ty = y + y_offset

			max_w = max(max_w, fw)	

			font_surface = font.render(line, True, color)
			if shadow != (0, 0):
				font_shadow = font.render(line, True, (0, 0, 1))
				font_shadow.set_alpha(128)
				screen.blit(font_shadow, (tx + shadow[0], ty + shadow[1]))
			screen.blit(font_surface, (tx, ty))

			y_offset += fh
		if align == "center":
			tx = x - max_w / 2
		elif align == "left":
			tx = x
		elif align == "right":
			tx = x - max_w
		return pygame.Rect((tx, y), (max_w, y_offset))
	else:
		fw, fh = font.size(text)

		if align == "center":
			tx = x - fw / 2
		elif align == "left":
			tx = x
		elif align == "right":
			tx = x - fw
		ty = y

		font_surface = font.render(text, True, color)
		if shadow != (0, 0):
				font_shadow = font.render(text, True, (0, 0, 1))
				font_shadow.set_alpha(128)
				screen.blit(font_shadow, (tx + shadow[0], ty + shadow[1]))
		screen.blit(font_surface, (tx, ty))

		return font_surface.get_clip()