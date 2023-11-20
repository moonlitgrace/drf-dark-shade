from rest_framework.renderers import BrowsableAPIRenderer

class DarkHorizonBrowsableAPIRenderer(BrowsableAPIRenderer):
	template = "dark-horizon.html"