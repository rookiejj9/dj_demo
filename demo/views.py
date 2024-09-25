from django.views import generic
from .models import ProvinceList,CityList

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'demo/index.html'
    context_object_name = 'Provinces'

    def get_queryset(self):
        """
        重写get_queryset，只返回省份名称
        :return:
        """
        return ProvinceList.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Cities'] = CityList.objects.filter(Province_id = 1)
        return context