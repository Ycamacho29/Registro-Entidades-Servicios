from datetime import datetime, timedelta
from django.shortcuts import render
from django.db.models import Count, Avg, Q
from django.contrib.auth.decorators import login_required
from core_models.models import *


# Create your views here.

@login_required
def index(request):
    # Conteo de entidades por tipo
    # conteo = Entidad.objects.values('tipo__nombre').annotate(
    #     total=Count('id')
    # )

    # Obtener conteo de entidades por tipo
    tipos_con_conteo = TipoEntidad.objects.annotate(
        total_entidades=Count('entidad'),
        ultimo_mes=Count('entidad', filter=Q(
            entidad__creado_en__gte=datetime.now() - timedelta(days=30)
        ))
    ).filter(estatus=True).order_by('-total_entidades')

    treinta_dias_atras = datetime.now() - timedelta(days=30)
    entidades_recientes = Entidad.objects.filter(
        creado_en__gte=treinta_dias_atras).order_by('-creado_en')

    context = {
        'segment': 'dashboard',
        'tipos_entidad': tipos_con_conteo,
        'entidades_recientes': entidades_recientes,
    }

    return render(request, 'pages/index.html', context=context)


@login_required
def tables(request):
    context = {
        'segment': 'tables'
    }
    return render(request, 'pages/tables.html', context)


@login_required
def billing(request):
    context = {
        'segment': 'billing'
    }
    return render(request, 'pages/billing.html', context)


@login_required
def notifications(request):
    context = {
        'segment': 'notifications'
    }
    return render(request, 'pages/notifications.html', context)


@login_required
def profile(request):
    context = {
        'segment': 'profile'
    }
    return render(request, 'pages/profile.html', context)


@login_required
def map(request):
    context = {
        'segment': 'map'
    }
    return render(request, 'pages/map.html', context)


@login_required
def typography(request):
    context = {
        'segment': 'typography'
    }
    return render(request, 'pages/typography.html', context)


@login_required
def icons(request):
    context = {
        'segment': 'icons'
    }
    return render(request, 'pages/icons.html', context)


@login_required
def template(request):
    context = {
        'segment': 'template'
    }
    return render(request, 'pages/template.html', context)
