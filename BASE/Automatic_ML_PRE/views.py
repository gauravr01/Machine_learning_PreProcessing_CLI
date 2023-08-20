from django.shortcuts import render
from django.http import HttpResponse
from forapp import run_preprocessing_cli, save_preprocessed_data
from django.http import JsonResponse
import pandas as pd
import json
from django.http import JsonResponse
from django.shortcuts import render

def get_columns(request):
    if request.method == 'POST':
        dataset_file = request.FILES.get('dataset')

        if dataset_file:
            try:
                dataset = pd.read_csv(dataset_file)
                columns = dataset.columns.tolist()
                dataset.to_csv('data.csv',index=False)
                return render(request, 'prepro.html', {'columns': columns})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'columns': []})

# def get_columns(request):
    # if request.method == 'POST' and request.FILES.get('dataset'):
    #     dataset_file = request.FILES['dataset']
    #     dataset = pd.read_csv(dataset_file)
    #     columns = dataset.columns.tolist()
    #     return JsonResponse({'columns': columns})
    # return JsonResponse({'columns': []})

# def preprocessing_form_view(request):
#     if request.method == 'POST':
#         target_variable = request.POST['target']
#         # Call the preprocessing function
        
#         preprocessed_data = run_preprocessing_cli('data.csv', target_variable)

#         if preprocessed_data is not None:
#             # Do something with the preprocessed_data (e.g., save to DB)
#             # Prepare context for rendering success message or results page
#             context = {'preprocess_data': preprocessed_data}
#             return JsonResponse(context)
#             #return render(request, 'preprocessing_results.html', preprocessed_data)
#         else:
#             error_message = "Error during preprocessing"
#             context = {'error_message': error_message}
#             return render(request, 'prepro.html', context)
#     else:
#         columns = []  # Fetch available columns or provide defaults
#         context = {'columns': columns}
#         return render(request, 'prepro.html', context)

def preprocessing_form_view(request):
    if request.method == 'POST':

        target_variable = request.POST['target']

        preprocessing_steps = request.POST.getlist('preprocessing_steps')

        # Call the preprocessing function
        preprocessed_data = run_preprocessing_cli('data.csv', target_variable, preprocessing_steps)
        #save_preprocessed_data(self=preprocessed_data)
        if preprocessed_data is not None:
            # Prepare context for rendering success message or results page
            context = {'preprocess_data': preprocessed_data}
            return JsonResponse(context)
            # output_filename = 'preprocessed_data.csv'
            # preprocessed_data_df = pd.DataFrame(preprocessed_data)
            # preprocessed_data_df.to_csv(output_filename, index=False)

            # # Provide a link to download the preprocessed CSV
            # download_link = f"/path/to/{output_filename}"
            # download_text = "Download Preprocessed CSV"

            # # Prepare context for rendering results page
            # context = {
            #     'preprocess_data': preprocessed_data,
            #     'download_link': download_link,
            #     'download_text': download_text
            # }
            # return JsonResponse(context)
        
            #return render(request, 'preprocessing_results.html', context)
        else:
            error_message = "Error during preprocessing"
            context = {'error_message': error_message}
            return render(request, 'prepro.html', context)
    else:
        columns = []  # Fetch available columns or provide defaults
        context = {'columns': columns}
        return render(request, 'prepro.html', context)

#create one more view function fom target..
#fetch all the temp.csv ka column and store it and then write the above new view fn 
#add action in the form we created in prepro.html