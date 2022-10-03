from django.shortcuts import render
from . import translator
# Create your views here.


def Translator_view(request):
    if request.method == "POST":
        original_text = request.POST["my_textarea"]
        output = translator.tranlation(str(original_text))
        return render(request, "translator.html", {"output_text": output, "original_text": original_text})
    else:
        return render(request, template_name="translator.html")