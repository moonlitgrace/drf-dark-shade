from rest_framework.renderers import BrowsableAPIRenderer

class DeepForestBrowsableAPIRenderer(BrowsableAPIRenderer):
	template = "deep-forest.html"