from django.shortcuts import render, redirect
import requests
import json
from .models import Stock
from django.contrib import messages
from .forms import StockForm


# Create your views here.


def home(request):
    # pk_ff5fca1be5324607b9d56d21f60bce94

    if request.method == "POST":
        ticker = request.POST["ticker"]
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+ ticker +"/quote?token=pk_ff5fca1be5324607b9d56d21f60bce94")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'newApp/home.html', {"api": api})

    else:
        return render(request, 'newApp/home.html', {"ticker": "Enter a Ticker Symbol Above..."})







def about(request):
    return render(request, 'newApp/about.html', {})


def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been Added!")
            return redirect("addstockurl")

    else:

        ticker = Stock.objects.all()
        output = list()

        for ticker_item in ticker:
            api_request = requests.get(
                "https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_ff5fca1be5324607b9d56d21f60bce94")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'newApp/add_stock.html', {"ticker" : ticker, 'output' : output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been deleted!")
    return redirect("deletestockurl")


def delete_stock(request):
    ticker = Stock.objects.all()

    return render(request, 'newApp/delete_stock.html', {"ticker" : ticker})
