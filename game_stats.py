filename = 'topscore.txt'


class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an active state.
		self.game_active = False

		# High score should never be reset.

		self.high_score = 0
		#print(self.high_score)

		with open(filename) as file_object:
			self.high_score= int (file_object.read())
		#print(self.high_score)


	def reset_stats(self):
		"""Initialize statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def new_high_score_check(self):	
		"""write the high score in the topscore file"""	
		with open(filename) as file_object:
			top_score= int (file_object.read())
		print(top_score, self.high_score)		
		if self.high_score > top_score:	
			with open(filename, 'w') as file_object:
				file_object.write(str(self.high_score))