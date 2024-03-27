from rest_framework.renderers import BrowsableAPIRenderer

class DeepForestBrowsableAPIRenderer(BrowsableAPIRenderer):
	template = "drf_dark_shade/deep-forest.html"