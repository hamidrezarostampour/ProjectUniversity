from django.shortcuts import redirect, get_object_or_404
from django.http import Http404

from gallery.models import Post

class LoggedInRedirectMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('gallery:home')
		return super().dispatch(request, *args, **kwargs)


class AccessUserMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		post = get_object_or_404(Post, pk=pk)
		if post.user == request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page")