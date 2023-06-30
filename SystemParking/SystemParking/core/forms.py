from django import forms
from django.utils.timezone import datetime
from .models import AutoEspacio, Automovil, Tarifa, EspacioEstacionamiento

class AutoEspacioForm(forms.ModelForm):
    placa = forms.CharField(max_length=10)
    marca = forms.CharField(max_length=15)
    modelo = forms.CharField(max_length=20)

    class Meta:
        model = AutoEspacio
        fields = ('espacio', 'tarifa')

    def save(self, commit=True):
        auto = Automovil.objects.create(
            placa=self.cleaned_data['placa'],
            marca=self.cleaned_data['marca'],
            modelo=self.cleaned_data['modelo']
        )
        auto_espacio = super().save(commit=False)
        auto_espacio.auto = auto
        auto_espacio.horaIngreso = datetime.now()  # Establecer la hora actual
        if commit:
            auto_espacio.save()
        return auto_espacio


class TarifaForm(forms.ModelForm):
    class Meta:
        model = Tarifa
        fields = ('nombreTarifa', 'precioTarifa', 'descripcionTarifa')


class EspacioForm(forms.ModelForm):
    class Meta:
        model = EspacioEstacionamiento
        fields = ('codigoIdentificativo','estadoEstacionamiento')
