# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage

from .models import CadEstimates

import csv
from io import StringIO

import json as simplejson

from tasks import queue

from .count_words import count_words_at_url

def upload_csv(request):
    if(request.method == 'POST'):
        arr = []
        upload_file = request.FILES['csv_file']
        if not upload_file.name.endswith('.csv'):
            return HttpResponse(simplejson.dumps({ 'message' : 'File is not in csv format.'  }))

        # decoded_file = upload_file.read().decode('utf-8').splitlines()
        content = StringIO(upload_file.read().decode('utf-8'))
        reader = csv.reader(content)

        # reader = csv.DictReader(decoded_file)

        for i, r in enumerate(reader):
            try:
                a = 'test'
            except Exception as e:
                print(e)
            if(i%4==0):
                queue.enqueue('cad.count_words_at_url', arr)
                arr = []
            else:
                queue.enqueue('cad.count_words_at_url', arr)


        # for r in reader:
        #     arr.append(formatDataPart(r))
        
        # Create the HttpResponse object with the appropriate CSV header.
        # response = HttpResponse(content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="CAD_Estimates.csv"'
        
        # fieldnames = [
        #     "Manufacturer", "Part", "Category","Package",
        #     "In DB?", "Base Part Number", "Datasheet",
        #     "E-CAD on SnapEDA?", "Date E-CAD Added (most recent date)",
        #     "UGC Available IF staff content not available",
        #     "Pin Count", "Part Page URL", "Duplicate or Unique?",
        #     "Symbol price", "3D price"]
        # writer = csv.DictWriter(response, fieldnames=fieldnames)
        # writer.writeheader()
        # for d in arr:
        #     writer.writerow(d)
        # return response

        # cs = CadEstimates(
        #     name=request.POST.get('name'),
        #     file=request.POST.get('name')
        # )
        # cs.save()
        return HttpResponse(simplejson.dumps({ 'message': 'Success' }))

    return render(request, 'cad_generator.html')