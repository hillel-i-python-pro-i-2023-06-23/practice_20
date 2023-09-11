from django.http import HttpResponseRedirect
from django.views.generic import FormView

from apps.tracker.forms.converter import CurrencyConversionForm


class CurrencyConversionView(FormView):
    template_name = "tracker/converter/currency_converter.html"
    form_class = CurrencyConversionForm

    def form_valid(self, form):
        if "clear" in self.request.POST:
            return HttpResponseRedirect(self.request.path_info)

        # Call the base implementation first to get a context
        context = self.get_context_data()
        # Get the data from the form
        amount = form.cleaned_data["amount"]
        from_currency = form.cleaned_data["from_currency"]
        to_currency = form.cleaned_data["to_currency"]
        converted_amount = form.cleaned_data["converted_amount"]
        # Add the data to the context
        context["amount"] = amount
        context["from_currency"] = from_currency
        context["to_currency"] = to_currency
        context["converted_amount"] = converted_amount

        return self.render_to_response(context)
