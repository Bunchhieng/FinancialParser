from django.contrib import admin

from .models import Symbol


class SymbolAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'IPOYear', 'sector', 'industry', 'summary_quote')

    search_fields = ['name', 'symbol']


admin.site.register(Symbol, SymbolAdmin)
