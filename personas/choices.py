from django.utils.translation import ugettext_lazy as _

GRUPO_SANGUINEO = (
    ('', _('Grupo Saguineo')),
    ('AB', _('Grupo AB')),
    ('A', _('Grupo A')),
    ('B', _('Grupo B')),
    ('O', _('Grupo O')),
)

FACTOR_SANGUINEO = (
    ('', _('Factor Saguineo')),
    ('+', _('RH+')),
    ('-', _('RH-')),
)

ESTADO_CIVIL = (
    ('', _('Estado Civil')),
    ('Casado', _('Casado/a')),
    ('Soltero', _('Soltero/a')),
    ('Divorciado', _('Divorciado/a')),
    ('Viudo', _('Viudo/a')),
    ('Concubino', _('Concubino/a')),
)
