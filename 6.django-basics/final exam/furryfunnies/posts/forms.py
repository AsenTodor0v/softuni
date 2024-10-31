from django import forms

from furryfunnies.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Put an attractive and unique title...",
            }),
            'content': forms.Textarea(attrs={
                'placeholder': "Share some interesting facts about your adorable pets...",
            }),
        }
    image_url = forms.URLField(
        label='Post Image URL',
        help_text = 'Share your funniest furry photo URL!',
        )
    
   


    
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
    image_url = forms.URLField(
        label='Post Image URL',)

        
class DeletePostForm(EditPostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
