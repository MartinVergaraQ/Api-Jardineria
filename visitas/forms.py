from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['cliente_nombre', 'direccion', 'tipo_servicio', 'disponibilidad', 'metros_cuadrados']

    def clean_cliente_nombre(self):
        nombre = self.cleaned_data.get('cliente_nombre')
        if not nombre:
            raise forms.ValidationError('El nombre del cliente es obligatorio.')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if not direccion:
            raise forms.ValidationError('La dirección es obligatoria.')
        if len(direccion) < 5:
            raise forms.ValidationError('La dirección debe tener al menos 5 caracteres.')
        return direccion

    def clean_tipo_servicio(self):
        tipo = self.cleaned_data.get('tipo_servicio')
        if not tipo:
            raise forms.ValidationError('El tipo de servicio es obligatorio.')
        return tipo

    def clean_disponibilidad(self):
        disponibilidad = self.cleaned_data.get('disponibilidad')
        if not disponibilidad:
            raise forms.ValidationError('La disponibilidad es obligatoria.')
        return disponibilidad

    def clean_metros_cuadrados(self):
        metros = self.cleaned_data.get('metros_cuadrados')
        if metros is None:
            raise forms.ValidationError('Debes ingresar los metros cuadrados.')
        if metros <= 0:
            raise forms.ValidationError('Los metros cuadrados deben ser mayores a 0.')
        return metros
