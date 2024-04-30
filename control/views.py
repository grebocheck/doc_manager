from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import RequestDocumentForm, UpdateRequestForm
from .models import RequestDocument, RequestEvent


# Create your views here.
def index(request):

    doc_list = RequestDocument.objects.filter(status__it_end=False).order_by('-created_at')

    paginator = Paginator(doc_list, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    total_num = page_obj.paginator.num_pages
    context = {"page_obj": page_obj, "range": range(1, total_num + 1), "doc_list": page_obj.object_list}
    print(context)

    return render(request, "control/index.html", context)


def create_request(request):
    if request.method == 'POST':
        form = RequestDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'control/create_request_success.html')
    else:
        form = RequestDocumentForm()
    return render(request, 'control/create_request.html', {'form': form})


def view_request(request, doc_id):

    request_document = get_object_or_404(RequestDocument, pk=doc_id)

    if request.method == 'POST':
        form = UpdateRequestForm(request.POST)
        if form.is_valid():
            new_price = form.cleaned_data['new_price']
            new_date_conclusion = form.cleaned_data['new_date_conclusion']
            new_date_payment = form.cleaned_data['new_date_payment']
            new_status = form.cleaned_data['new_status']
            title = form.cleaned_data['title']
            detail = form.cleaned_data['detail']
            old_status = request_document.status
            # Внесення змін до RequestDocument
            if new_price:
                request_document.price = new_price
            if new_date_conclusion:
                request_document.date_conclusion = new_date_conclusion
            if new_date_payment:
                request_document.date_payment = new_date_payment
            if new_status:
                request_document.status = new_status
            request_document.save()
            # Створення нового RequestEvent
            if not new_status:
                new_status = old_status
            RequestEvent.objects.create(document=request_document, author=request.user, title=title, detail=detail,
                                        old_status=old_status, new_status=new_status)
            return redirect('view_request', doc_id=doc_id)
    else:
        form = UpdateRequestForm()

    event_list = RequestEvent.objects.filter(document__id=doc_id).order_by('-created_at')
    context = {"request_document": request_document, "form": form, "event_list": event_list}

    return render(request, 'control/view_request.html', context=context)
