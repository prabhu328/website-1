##
#    Copyright (C) 2013 Jessica Tallon & Matt Molyneaux
#   
#    This file is part of Inboxen front-end.
#
#    Inboxen front-end is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Inboxen front-end is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Inboxen front-end.  If not, see <http://www.gnu.org/licenses/>.
##

from inboxen.models import BlogPost

from django.shortcuts import render
from django.http import HttpResponseRedirect


def view(request):
	posts = BlogPost.objects.all().order_by("-date")

	context = {
		"page":"Blog",
		"posts":posts,
	}

	return render(request, "blog/blog.html", context)

def post(request, postid):
	try:
		p = BlogPost.objects.get(id=postid)
	except BlogPost.DoesNotExist:
		return HttpResponseRedirect("/blog/")

	context = {
		"page":p.subject,
		"post":p,
	}

	return render(request, "blog/post.html", context)