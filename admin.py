from django.contrib import admin
from django import forms
from django.shortcuts import render
from .models import Agent, Region
from django.http import HttpResponseRedirect
from django.urls import path
import pandas as pd  # Corrected import statement

class ExcelImportForm(forms.Form):  # Corrected class name
    excel_file = forms.FileField()

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'agency', 'sales', 'experience', 'region')
    change_list_template = "entities/import_agents.html"
    actions = ["import_excel"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-excel/', self.import_excel),
        ]
        return my_urls + urls

    def import_excel(self, request):
        if request.method == "POST":
            excel_file = request.FILES["excel_file"]
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                region_name = row['region']
                region, _ = Region.objects.get_or_create(name=region_name)
                Agent.objects.update_or_create(
                    phone=row['phone'],  # Assuming 'phone' is a unique identifier
                    defaults={
                        'name': row['name'],
                        'phone': row['phone'],  # It's important to include the unique field here too if it might change
                        'agency': row['agency'],
                        'sales': row['sales'],
                        'experience': row['experience'],
                        'activity': row['activity'],
                        'region': region,
                    },
                )
            self.message_user(request, "Your excel file has been imported")
            return HttpResponseRedirect("../")
        else:
            form = ExcelImportForm()  # Corrected form class name
            payload = {"form": form}
            return render(request, "admin/excel_form.html", payload)

admin.site.register(Agent, AgentAdmin)
admin.site.register(Region)
