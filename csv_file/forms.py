from django.forms import forms


class FileUploadForm(forms.Form):
    """ Form for uploading a file """
    file = forms.FileField(required=True)

