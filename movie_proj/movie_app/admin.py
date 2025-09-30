from django.contrib import admin, messages
from .models import Movie, Directors
from django.db.models import QuerySet
# Register your models here.


admin.site.register(Directors)

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий рейтинг'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<=40':
            return queryset.filter(rating__lt =40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=79)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)

        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'rating', 'budget', 'currency', 'ratin_status']
    list_editable = ['currency', 'budget', 'rating']
    ordering = ['-rating', '-name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='Статус')
    def ratin_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Зачем это смотреть?'
        if movie.rating < 70:
            return 'Разок можно глянуть'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в долларах')
    def set_dollars(self, request, qs:QuerySet ):
        qs.update(currency= Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs:QuerySet ):
        count_updated = qs.update(currency= Movie.EUR)
        self.message_user(request,f'Было обновлено {count_updated}',
                          messages.ERROR)