# views.py
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

from apps.tracker.services.cryptocurrency_parser import get_cryptocurrency_info


class CryptoCurrencyView(ListView):
    template_name = "tracker/cryptocurrency/cryptocurrency.html"
    context_object_name = "crypto_list"
    queryset = get_cryptocurrency_info()
    per_page = 15

    def get_queryset(self):
        query = self.request.GET.get("q")
        # filter the list by name or symbol if query is present
        if query:
            crypto_list = [
                crypto
                for crypto in self.queryset
                if query.lower() in (crypto["name"].lower() or crypto["symbol"].lower())
            ]
        else:
            crypto_list = self.queryset

        return crypto_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(context["crypto_list"], self.per_page)
        page = self.request.GET.get("page")

        try:
            crypto_list = paginator.page(page)
        except PageNotAnInteger:
            crypto_list = paginator.page(1)
        except EmptyPage:
            crypto_list = paginator.page(paginator.num_pages)

        context["crypto_list"] = crypto_list
        context["page"] = crypto_list

        return context
