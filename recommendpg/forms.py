from django import forms


class ArtistForm(forms.Form):
    artist = forms.CharField(max_length=100,label='Enter genre name')
