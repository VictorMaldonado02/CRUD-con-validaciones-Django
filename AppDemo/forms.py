#from wsgiref.validate import validator
from django import forms
from AppDemo.models import Producto,Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 4:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 4:
            raise forms.ValidationError('El apellido debe tener al menos 2 caracteres')
        return last_name

class FormUsu(forms.Form):

    nombre = forms.CharField(required= True)
    email = forms.CharField(required= True)
    contraseña = forms.CharField(widget=forms.PasswordInput())

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    contraseña.widget.attrs['class'] = 'form-control'

    def save(self):
        usuario = Usuario()
        usuario.nombre = self.cleaned_data['nombre']
        usuario.email = self.cleaned_data['email']
        usuario.contraseña = self.cleaned_data['contraseña']
        usuario.save()

    def clean_nombre(self):
        inputNombre = self.cleaned_data ['nombre']
        if len(inputNombre) > 40 :
            raise forms.ValidationError('El NOMBRE del producto es muy LARGO')
        if len(inputNombre) < 4 :
            raise forms.ValidationError('El NOMBRE del producto es muy CORTO')
        return inputNombre
    def clean_email(self):
        inputEmail = self.cleaned_data ['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError("Correo debe contener un @")
        return inputEmail
    def clean_contraseña(self):
        inputContraseña = self.cleaned_data ['contraseña']
        if len(inputContraseña)<8:
            raise forms.ValidationError('La CONTRASEÑA debe ser de al menos 8 caracteres')
        caracteres_especiales = "!@#$%^&*()_+<>?{}[]|\/"
        if not any(char in caracteres_especiales for char in inputContraseña):
            raise forms.ValidationError("La contraseña debe contener al menos un carácter especial")
        return inputContraseña


class FormUsua(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('__all__')

    nombre = forms.CharField(required= True)
    email = forms.CharField(required= True)
    contraseña = forms.CharField(widget=forms.PasswordInput())

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    contraseña.widget.attrs['class'] = 'form-control'

    def clean(self):
        user_clean_data = super().clean()

        inputNombre = user_clean_data['nombre']
        if len(inputNombre) > 40 :
            raise forms.ValidationError('El NOMBRE del producto es muy LARGO')
        if len(inputNombre) < 4 :
            raise forms.ValidationError('El NOMBRE del producto es muy CORTO')
        inputEmail = user_clean_data['email']
        if inputEmail.find('@') == -1 :
            raise forms.ValidationError("Correo debe contener un @")
        inputContraseña = user_clean_data ['contraseña']
        if len(inputContraseña) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres")
        caracteres_especiales = "!@#$%^&*()_+<>?{}[]|\/"
        if not any(char in caracteres_especiales for char in inputContraseña):
            raise forms.ValidationError("La contraseña debe contener al menos un carácter especial")
        return user_clean_data

    

class FormProducto(forms.Form):

    nombre = forms.CharField(required= True)
    marca = forms.CharField(required= True)
    talla = forms.CharField(required= True)
    color = forms.CharField(required= True)
    email = forms.CharField(required=True)

    estado = [
    ('Disponible', 'DISPONIBLE'),
    ('No Disponible', 'NO DISPONIBLE'),
    ('Descontinuado', 'DESCONTINUADO')
    ]

    estado = forms.CharField(widget=forms.Select(choices=estado))

    nombre.widget.attrs['class'] = 'form-control'
    marca.widget.attrs['class'] = 'form-control'
    talla.widget.attrs['class'] = 'form-control'
    color.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    
    def clean_nombre(self):
        inputNombre = self.cleaned_data ['nombre']
        if len(inputNombre) > 10 :
            raise forms.ValidationError('El NOMBRE del producto es muy LARGO')
        if len(inputNombre) < 5 :
            raise forms.ValidationError('El NOMBRE del producto es muy CORTO')
        return inputNombre
    
    def clean_marca(self):
        inputMarca = self.cleaned_data ['marca']
        if len(inputMarca) > 15 :
            raise forms.ValidationError('La MARCA del producto es muy LARGO')
        if len(inputMarca) < 3 :
            raise forms.ValidationError('La MARCA del producto es muy CORTO')
        return inputMarca
    
    def clean_talla(self):
        inputTalla = self.cleaned_data ['talla']
        if len(inputTalla) > 3 :
            raise forms.ValidationError('La TALLA del producto es muy LARGO')
        if len(inputTalla) < 1 :
            raise forms.ValidationError('La TALLA del producto es muy CORTO')
        return inputTalla
        
    def clean_color(self):
        inputColor = self.cleaned_data ['color']
        if len(inputColor) > 10 :
            raise forms.ValidationError('El COLOR del producto es muy LARGO')
        if len(inputColor) < 3 :
            raise forms.ValidationError('El COLOR del producto es muy CORTO')
        return inputColor
    
    def clean_email(self):
        inputEmail = self.cleaned_data ['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError("Correo debe contener un @")
        return inputEmail
        
    def save(self):
        producto = Producto()
        producto.nombre = self.cleaned_data['nombre']
        producto.marca = self.cleaned_data['marca']
        producto.talla = self.cleaned_data['talla']
        producto.color = self.cleaned_data['color']
        producto.email = self.cleaned_data['email']
        producto.estado = self.cleaned_data['estado']
        producto.save()

class FormProduct(forms.ModelForm):

    class Meta:
        model = Producto
            
        fields = ('__all__')

    nombre = forms.CharField(required= True)
    talla = forms.CharField(required= True)
    color = forms.CharField(required= True)
    marca = forms.CharField(required= True)
    email = forms.CharField(required=True)
    

    estado = [
    ('Disponible', 'DISPONIBLE'),
    ('No Disponible', 'NO DISPONIBLE'),
    ('Descontinuado', 'DESCONTINUADO')
    ]

    estado = forms.CharField(widget=forms.Select(choices=estado))

    nombre.widget.attrs['class'] = 'form-control'
    marca.widget.attrs['class'] = 'form-control'
    talla.widget.attrs['class'] = 'form-control'
    color.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    
    def clean(self):
        user_clean_data = super().clean()

        inputNombre = user_clean_data['nombre']
        if len(inputNombre) > 10 :
            raise forms.ValidationError('El NOMBRE del producto es muy LARGO')
        if len(inputNombre) < 5 :
            raise forms.ValidationError('El NOMBRE del producto es muy CORTO')
        inputMarca = user_clean_data['marca']
        if len(inputMarca) > 15 :
            raise forms.ValidationError('La MARCA del producto es muy LARGO')
        if len(inputMarca) < 4 :
            raise forms.ValidationError('La MARCA del producto es muy CORTO')
        inputTalla = user_clean_data['talla']
        if len(inputTalla) > 3 :
            raise forms.ValidationError('La TALLA del producto es muy LARGO')
        if len(inputTalla) < 1 :
            raise forms.ValidationError('La TALLA del producto es muy CORTO')
        inputColor = user_clean_data['color']
        if len(inputColor) > 10 :
            raise forms.ValidationError('El COLOR del producto es muy LARGO')
        if len(inputColor) < 3 :
            raise forms.ValidationError('El COLOR del producto es muy CORTO')
        inputEmail = user_clean_data['email']
        if inputEmail.find('@') == -1 :
            raise forms.ValidationError("Correo debe contener un @")
        return user_clean_data
    