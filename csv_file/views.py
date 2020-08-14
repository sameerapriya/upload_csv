from django.shortcuts import render
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
import pandas as pd
from pandas.errors import EmptyDataError
from .models import CsvData


def upload(request):
    """ Function for uploading CSV file"""
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            if not file.name.endswith(('.txt', '.csv', '.xlsx', '.xls')):
                # Passing all possible extensions that could be CSV files.
                return render(request, 'csv_file/upload.html',
                              {'form': FileUploadForm(), 'error': 'Please upload a file with correct format.',
                               'submit': 'Upload File'})
            fs = FileSystemStorage()
            # Saving the file into MEDIA folder ,
            # this function by default stores a file to MEDIA if location is not passed.
            filename = fs.save(file.name, file)
            uploaded_url = fs.url(file.name)
            df = store_csv_data('media/'+filename)  # Passing the data ,that has been read.
            return render(request, 'csv_file/upload.html', {'uploaded_url': uploaded_url, 'df': df})
        else:
            # if an empty file is uploaded or an invalid file is uploaded , error is passed
            return render(request, 'csv_file/upload.html',
                          {'form': FileUploadForm(), 'error': 'Please upload a file which is not empty.',
                           'submit': 'Upload File'})
    else:  # GET request
        return render(request, 'csv_file/upload.html', {'form': FileUploadForm(), 'submit': 'Upload File'})


def store_csv_data(filepath):
    """Function to read and save the csv data into the POSTGRES DB """
    name = filepath.split('/')[-1]  # to obtain the name of the file
    try:
        df = pd.read_csv(filepath)  # reading the csv file
        dh = df.to_html()  # Displaying the data
        data = df.to_json()  # Converting the DataFrame to JSON before saving.
        CsvData.objects.create(file_name=name, data=data)
    except EmptyDataError:
        df = pd.DataFrame()
        dh = df.to_html()
    return dh
