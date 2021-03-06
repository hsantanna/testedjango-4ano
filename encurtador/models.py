from django.db import models

from .validators import validar_url, validar_ponto_com
from .utils import criar_shortcode


# Create your models here.

# Classe usada para sobrepor URL.objects.all()
class URLManager(models.Manager):
    def all(self, *args, **kwargs):
        consulta_principal = super(URLManager, 
                                   self).all(*args, **kwargs)
        # filtra a consulta pelo campo "ativo"
        consulta = consulta_principal.filter(ativo=True)
        return consulta

    # não precisa dos args pq não sobrepõe nada:
    @staticmethod
    def atualizar_shortcodes():
        consulta = URL.objects.filter(id__gte=1)
        # gte: "greater to" e "equal" ( >= )
        novos_codigos = 0
        for c in consulta:
            c.shortcode = criar_shortcode(c)
            print(c.shortcode)
            c.save()
            novos_codigos += 1
        return "Novos códigos criados: {i}".format(i=novos_codigos)


class URL(models.Model):
    # cria campo url, do tipo CharField, tamanho máximo 220:
    url = models.CharField(max_length=220, validators=[validar_url, validar_ponto_com])
    shortcode = models.CharField(max_length=15, null=True,
                                 blank=True, unique=True,
                                 #default="codigopadrao",
                                 )
    atualizado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # testa se o shortcode é nulo ou está em branco
        # mesmo que: if self.shortcode in (None,""):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = criar_shortcode(self)
        super(URL, self).save(*args, **kwargs)

    # método que retorna string com identificação do objeto
    def __str__(self):
        return str(self.url)
