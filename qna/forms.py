from django.forms import ModelForm
from .models import Post, Comment


class FileUploadForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_image', 'contents', 'top_fixed']
