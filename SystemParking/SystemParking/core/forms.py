from django import forms
from django.utils.timezone import datetime
from .models import AutoEspacio, Automovil, Tarifa, EspacioEstacionamiento, Ingreso, Egreso

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


class IngresoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingresa la descripción','class':'form-control','autocomplete': 'off'}))
    monto = forms.DecimalField(widget=forms.NumberInput(attrs={'step': '0.01','placeholder': 'Total del monto','class':'form-control small'}))
    class Meta:
        model = Ingreso
        fields = ('monto','descripcion')
        exclude = ['fechaCreacion']


class EgresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ('monto', 'descripcion', 'fechaCreacion')


